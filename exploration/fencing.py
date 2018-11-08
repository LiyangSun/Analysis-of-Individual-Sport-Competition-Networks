import imp
preprocessing = imp.load_source('preprocessing', '../preprocessing/fencing.py')

if __name__ == '__main__':
    G, name_map = preprocessing.get_fencing_graph_and_name_map()
