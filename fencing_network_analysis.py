import csv
import fileinput


#f = open('seedingFencingNetworkTest.csv')



f = open('fencingNetworkTest.csv')
csv_f = csv.reader(f)
results = []
for i,row in enumerate(csv_f):
  print "{}:{} placed {}".format(i + 1,row[1], row[0])
  results.append(row[1])

num_participants = len(results)
place = 1
print("Looking at participant who placed {}/{}").format(place, num_participants)
i = place * 2
while(i < num_participants):
    print("{} beat {}").format(results[place], results[i])
    i *= 2
