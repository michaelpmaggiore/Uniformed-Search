import sys
import heapq
from collections import defaultdict
import copy
import os



def find_route(input_filename, origin_city, destination_city):
    city_set = {}
    list = []
    global shortest_distance # Keeps track of distance from start city to current city
    shortest_distance = 0
    routes_list = []
    frontier_nodes = city_set.get(origin_city)
    current_city = ""

    print(input_filename, origin_city, destination_city)

    def create_graph(edges):
        graph = defaultdict(list)
        for src, dst, cost in edges:
            graph[src].append((dst, cost))
            graph[dst].append((src, cost))  # if the graph is undirected
        return graph

    # Checks surrounding routes and finds shortest distance between all possible routes from start to goal.
    def UCS_function():
        if origin_city == destination_city:
            return [origin_city], 0

        frontier = []
        heapq.heappush(frontier, (0, [origin_city]))

        i = 0
        while frontier:
            if i > 10000:
                break

            cost, path = heapq.heappop(frontier)
            current_node = path[-1]

            if current_node == destination_city:
                return path, cost

            for neighbor, neighbor_cost in city_set[current_node]:
                new_cost = cost + int(neighbor_cost)
                new_path = path + [neighbor]
                heapq.heappush(frontier, (new_cost, new_path))
            i += 1
        return [], float('inf')

    with open(input_filename, "r") as file:
        for line in file:
            start_index = 0
            last_index = 0

            for char in line:
                last_index += 1

                if char == ' ':
                    current_index = last_index # Used for second loop to obtain second city name
                    for char2 in line[last_index:]:
                        current_index += 1
                        if char2 == ' ':

                            if line[start_index:last_index-1] not in city_set:
                                
                                list.append([line[last_index:current_index-1], line[current_index:-1]])
                                city_set.update({line[start_index:last_index-1] : list}) # Used to store first city's available paths to other cities and path distance
                            elif line[start_index:last_index-1] in city_set:
                                city_set.get(line[start_index:last_index-1]).append([line[last_index:current_index-1], line[current_index:-1]])

                            list = [] # Resets list to 0

                            if line[last_index:current_index-1] not in city_set:

                                list.append([line[start_index:last_index-1], line[current_index:-1]])
                                city_set.update({line[last_index:current_index-1] : list}) # Used to store second city's available paths to other cities and path distance
                            elif line[last_index:current_index-1] in city_set:
                                city_set.get(line[last_index:current_index-1]).append([line[start_index:last_index-1], line[current_index:-1]])


                            list = [] # Resets list to 0
                            break
                    break
                
                elif line[0:last_index] == "END":
                    break

    # Loads data into a graph
    tuple_list = []
    original_city_set = copy.deepcopy(city_set)
    for key in city_set:
        for element in city_set[key]:
            element = tuple(element)
            tuple_list.append(element)
        city_set[key] = tuple_list
        tuple_list = []

    paths, shortest_distance = UCS_function()
    if paths == []:
        print("distance: " + "infinity")
        print("route: ")
        print("none")
    else:
        print("distance: " + str(shortest_distance) + " km")
        print("route: ")
        if (shortest_distance == 0):
            print(paths[0] + " to " + paths[0] + ", 0 km")

        for index, city in enumerate(paths[:-1]):
            for city2 in original_city_set.get(city):
                if city2[0] == paths[index+1]:
                    print(city + " to " + paths[index+1] + ", " + city2[1] + " km")

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        input_filename = sys.argv[1]
        origin_city = sys.argv[2]
        destination_city = sys.argv[3]
        find_route(input_filename, origin_city, destination_city)

