peoples = []

with open('names.csv') as file:
    for line in file:
        name, From = line.rstrip().split(',')
        people = {'name': name.title() , 'from': From.title()}
        peoples.append(people)

for people in sorted(peoples, key=lambda people : people['name']):
    print(f'{people['name']} is from {people['from']}')