import util

seeding = util.getOrderedNameList('oct_nac_2017_seeding.csv')#["a", "b", "c", "d", "e"]
results = util.getOrderedNameList('oct_nac_2017_results.csv')#["d", "c", "a", "b", "e"]
util.createCompetitionGraph(seeding, results)
