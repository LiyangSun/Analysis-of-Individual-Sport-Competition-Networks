import util

seeding = util.getOrderedNameList('oct_nac_2017_seeding.csv')#["a", "b", "c", "d", "e"]
results = util.getOrderedNameList('oct_nac_2017_results.csv')#["d", "c", "a", "b", "e"]
G = util.createCompetitionGraph(seeding, results)
print 'nodes: ', G.GetNodes()
print 'edges: ', G.GetEdges()
