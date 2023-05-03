import sys

input_filename = sys.argv[1]
origin_city = sys.argv[2]
destination_city = sys.argv[3]
city_set = {}
list = []

print(input_filename, origin_city, destination_city)

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

                        if line[last_index:current_index-1] not in city_set:
                            list.append([line[start_index:last_index-1], line[current_index:-1]])
                            city_set.update({line[last_index:current_index-1] : list}) # Used to store second city's available paths to other cities and path distance
                        elif line[last_index:current_index-1] in city_set:
                            city_set.get(line[last_index:current_index-1]).append([line[start_index:last_index-1], line[current_index:-1]])

                        list = [] # Resets list to 0
                        break
                break

                # start_index = last_index
            
            elif line[0:last_index] == "END":
                break

    print(city_set.get("Bremen"))
        

l = set()
l.add(1)
print(l)