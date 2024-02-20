# https://www.kaggle.com/datasets/risakashiwabara/netfllix-weekly-views-data
import csv
with open("marvel.csv", "r") as file:
    reader = csv.reader(file)
    count={}
    i=4 #column number
    for row in reader:
            if row[i] in count:
                count[row[i]] += 1
            else:
                count[row[i]] = 1
for favorite_character in sorted(count, key=count.get, reverse=True):
    print(f"{favorite_character} = {count[favorite_character]}")

