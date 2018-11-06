import util
import snap
# first approach: use multiple edges instead of weighted edges
G = snap.TNEANet.New()
name_map = {}

for month, year in [('oct','2017'),('april','2018'),('dec','2017'),('jan','2018'),('jul','2018')]:
    seeding = util.getOrderedNameList(month+'_nac_'+year+'_seeding.csv')#["a", "b", "c", "d", "e"]
    results = util.getOrderedNameList(month+'_nac_'+year+'_results.csv')#["d", "c", "a", "b", "e"]
    util.createCompetitionGraph(seeding, results, G, name_map)
    print 'nodes:', G.GetNodes(), ' edges:', G.GetEdges()
