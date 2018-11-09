import pandas as pd
from os import listdir
import pickle
from pathlib import Path
import utils
import math
import collections
import sys
import csv
import snap


def getOrderedNameList(path):
    """Get the players by ranking order from csv file path"""
    results = []
    with open(path) as f:
        csv_f = csv.reader(f)
        for i, row in enumerate(csv_f):
            results.append(row[1])
    return results


def createCompetitionGraph(seeding, results, G=None, name_to_node_map=None, verbose=False):
    """Create competitions graph from seeding and results"""
    seeding_dict = {}
    results_dict = collections.defaultdict(lambda: sys.maxint)
    pos_to_name_dict = collections.defaultdict(lambda: "BYE")  # mapping (actual value : representative value)
    match_win_list = []

    for place, name in enumerate(seeding):
        seeding_dict[name.lower()] = place
        pos_to_name_dict[place] = name.lower()

    for place, name in enumerate(results):
        results_dict[name.lower()] = place

    remaining_rounds = int(math.ceil(math.log(len(seeding), 2)))

    for round_num in range(0, remaining_rounds):
        round_size = 2 ** (remaining_rounds - round_num)
        if verbose:
            print("Round size: {}".format(round_size))
        for expected_winner_num in range(0, round_size / 2):
            expected_winner_name = pos_to_name_dict[expected_winner_num]
            expected_loser_num = round_size - (expected_winner_num + 1)
            expected_loser_name = pos_to_name_dict[expected_loser_num]
            if results_dict[expected_winner_name] > results_dict[expected_loser_name]:
                if verbose:
                    print("\tUpset! {} just beat our expected_winner {}".format(expected_loser_name,
                                                                                expected_winner_name))
                pos_to_name_dict[expected_winner_num] = expected_loser_name
                pos_to_name_dict[expected_loser_num] = expected_winner_name
            else:
                if verbose:
                    print("\tOur expected_winner {} just beat {}".format(expected_winner_name, expected_loser_name))
            winner_name = pos_to_name_dict[expected_winner_num]
            loser_name = pos_to_name_dict[expected_loser_num]
            match_win_list.append((loser_name, winner_name))
    if name_to_node_map is None:
        name_to_node_map = {}
    if G is None:
        G = snap.TNEANet.New()
    for loser, winner in match_win_list:
        if loser == "BYE":
            continue
        if loser not in name_to_node_map:
            nid = G.AddNode(-1)
            name_to_node_map[loser] = nid
        if winner not in name_to_node_map:
            nid = G.AddNode(-1)
            name_to_node_map[winner] = nid
        G.AddEdge(name_to_node_map[loser], name_to_node_map[winner])
    return G, name_to_node_map


def get_fencing_graph_and_name_map():
    G = snap.PNEANet.New()
    name_map = {}
    for month, year in [('oct', '2017'), ('april', '2018'), ('dec', '2017'), ('jan', '2018'), ('jul', '2018')]:
        seeding = getOrderedNameList(
            '../datasets/fencing/csv/' + month + '_nac_' + year + '_seeding.csv')  # ["a", "b", "c", "d", "e"]
        results = getOrderedNameList(
            '../datasets/fencing/csv/' + month + '_nac_' + year + '_results.csv')  # ["d", "c", "a", "b", "e"]
        createCompetitionGraph(seeding, results, G, name_map)
    return G, name_map


def save_edges_txt():
    graph, name_map = get_fencing_graph_and_name_map()
    with open("../datasets/fencing/edges.txt", 'w') as edges:
        for edge in graph.Edges():
            x = edge.GetSrcNId()
            y = edge.GetDstNId()
            edges.write(str(x) + ";" + str(y) + "\n")


def save_dict():
    graph, name_map = get_fencing_graph_and_name_map()
    with open("../datasets/fencing/fencing_ids.pkl", 'wb') as f:
        pickle.dump(name_map, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    save_dict()