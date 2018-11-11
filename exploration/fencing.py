import snap
#import pickle
import utils.overview as ov
import utils.structural_role as sr
import utils.bfs as bsf
import utils.similarity as sim
import utils.motif_detection as md
import utils.load as ld
import imp

preprocessing = imp.load_source('preprocessing', '../preprocessing/fencing.py')

if __name__ == '__main__':
    G, name_map = preprocessing.get_fencing_graph_and_name_map()
    ov.quick_properties(G, "Fencing", "../datasets/tennis/men_ids.pkl")
