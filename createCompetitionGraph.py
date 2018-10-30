import math
import collections
import sys

seeding = ["a", "b", "c", "d", "e"]
results = ["d", "c", "a", "b", "e"]


def createHierarchy(seeding, results):
    seeding_dict = {}
    results_dict = collections.defaultdict(lambda: sys.maxint)
    pos_to_name_dict = collections.defaultdict(lambda: "BYE") #mapping (actual value : representative value)
    hierarchy_list = []

    for place, name in enumerate(seeding):
        seeding_dict[name] = place
        pos_to_name_dict[place] = name

    for place, name in enumerate(results):
        results_dict[name] = place

    remaining_rounds = int(math.ceil(math.sqrt(len(seeding))))
    for round_num in range(0, remaining_rounds):
        round_size = 2**(remaining_rounds - round_num)
        print("Round size: {}").format(round_size)
        for expected_winner_num in range(0, round_size/2):
            expected_winner_name = pos_to_name_dict[expected_winner_num]
            expected_loser_num = round_size - (expected_winner_num + 1)
            expected_loser_name = pos_to_name_dict[expected_loser_num]
            if results_dict[expected_winner_name] > results_dict[expected_loser_name]:
                print("Upset! Our expected_winner {} just lost to {}").format(expected_winner_name, expected_loser_name)
                pos_to_name_dict[expected_winner_num] = expected_loser_name
                pos_to_name_dict[expected_loser_num] = expected_winner_name
            else:
                print("Our expected_winner {} just beat {}").format(expected_winner_name, expected_loser_name)

createHierarchy(seeding, results)
