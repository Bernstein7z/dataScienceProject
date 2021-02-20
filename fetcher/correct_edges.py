import csv

with open("../data/euclidean_edges_2016.csv", 'r') as fileRead:
    reader = csv.reader(fileRead, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    temp = [row for row in reader]

with open("../data/_euclidean_edges_2016.csv", 'w') as fileWrite:
    writer = csv.writer(fileWrite, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    writer.writerow(temp[0])
    for i in range(1, len(temp)):
        writer.writerow([temp[i][0], temp[i][1], float(temp[i][2])+1])
