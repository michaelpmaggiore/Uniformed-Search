import sys

input_filename = sys.argv[1]
origin_city = sys.argv[2]
destination_city = sys.argv[3]
city_set = set()

print(input_filename, origin_city, destination_city)

with open(input_filename, "r") as file:
    for line in file:
        start_index = 0
        last_index = 0

        for char in line:
            last_index += 1
            if char == ' ':
                city_set.add(line[start_index:last_index])
                start_index = last_index
            elif line[0:last_index] == "END":
                break
    print(city_set)
        

l = set()
l.add(1)
print(l)