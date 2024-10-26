# SOURCE: MIT OCW ALGORITHMS LECTURE 9 and 10 -> use of dfs and queues to traverse non weighted graphs

# TASK 1
class City:
    def __init__(self,name,pop):
        self.name = name
        self.population = pop 
        self.connection = []
    
    def edge(self, city2):
        self.connection.append(city2)

# create a hashmap for the graph traversal
newMap = {}
f = open("city_population.txt","r")
for line in f:
    name, pop = line.strip().split(" : ")
    newMap[name] = City(name,int(pop))
f.close()

f = open("road_network.txt","r")
for line in f:
    name1, name2 = line.strip().split(" : ")
    name1 = newMap[name1]
    name2 = newMap[name2]
    name1.edge(name2)
    name2.edge(name1)
f.close()

# for city_name, city in newMap.items():
#     print(city.name,city.population, city.connection)

def numIsland(newMap):
    visited = set()
    numIslands = 0

    def dfs(city):
        visited.add(city)
        for edge in city.connection:
            if edge not in visited:
                dfs(edge)
    
    for city in newMap.values():
        if city not in visited:
            dfs(city)
            numIslands += 1

    return numIslands

def islandPeople(newMap):
    visited = set()
    numPeople = []

    def dfs(city):
        visited.add(city)
        pop = city.population
        for edge in city.connection:
            if edge not in visited:
                pop += dfs(edge)
        return pop
    
    for city in newMap.values():
        if city not in visited:
            pop = dfs(city)
            numPeople.append(pop)

    return numPeople

def minDistance(cities,city1,city2):
    A = newMap.get(city1)
    B = newMap.get(city2)
    if not A or not B:
        return -1
    if A == B:
        return 0
    visited = set()
    queue = [(A,0)]

    while queue:
        curr, distance = queue.pop(0)
        if curr == B:
            return distance
        visited.add(curr)
        for adjacent in curr.connection:
            if adjacent not in visited:
                queue.append((adjacent, distance + 1))
    return -1

newMap = {}

# Simulating reading from files
city_data = [
    "cityA : 30000",
    "cityB : 40000",
    "cityC : 50000",
    "cityD : 60000",
    "cityE : 70000",
    "cityF : 80000"
]

road_data = [
    "cityA : cityB",
    "cityC : cityD",
    "cityE : cityF"
]

# Populate the city map
for line in city_data:
    name, pop = line.strip().split(" : ")
    newMap[name] = City(name, int(pop))

# Create road connections
for line in road_data:
    name1, name2 = line.strip().split(" : ", 1)  # Split only on the first occurrence
    city1 = newMap[name1]
    city2 = newMap[name2]
    city1.edge(city2)
    city2.edge(city1)

# Test the functions
print("Number of islands:", numIsland(newMap))  # Expected output: 3
print("Population of each island:", islandPeople(newMap))  # Expected output: [70000, 110000, 150000]

# Test minDistance function (example for cities in different islands)
print("Minimum distance from City A to City B:", minDistance(newMap, "cityA", "cityB"))  
print("Minimum distance from City A to City C:", minDistance(newMap, "cityA", "cityC"))

# for city in newMap.values():
#     print(city.name)