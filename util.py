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


def general_info(csv_path='fencingNetworkTest.csv'):
    results = []
    with open(csv_path) as f:

        csv_f = csv.reader(f)
        for i, row in enumerate(csv_f):
            print "{}:{} placed {}".format(i + 1, row[1], row[0])
            results.append(row[1])

    num_participants = len(results)
    place = 1
    print("Looking at participant who placed {}/{}".format(place, num_participants))
    i = place * 2
    while i < num_participants:
        print("{} beat {}".format(results[place], results[i]))
        i *= 2
