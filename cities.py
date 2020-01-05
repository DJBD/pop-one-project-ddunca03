import tkinter
from tkinter import *


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    list_of_tuples = []
    for line in lines:
        a = line.rstrip('\n').split("\t")
        a = tuple(a)
        list_of_tuples.append(a)

    return (list_of_tuples)


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    list_of_cities = []
    for item in road_map:
        a = (item[0], item[1], round(float(item[2]), 2), round(float(item[3]), 2))
        list_of_cities.append(a)
    print(list_of_cities)


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    # sqrt((x1-x2)^2 + (y1-y2)^2)
    import math
    import copy
    distance_road_map = copy.deepcopy(road_map)
    distance_road_map.append(road_map[0])
    total_distance = 0
    for city in range(0, len(road_map)):
        city_a = distance_road_map[city][2], distance_road_map[city][3]
        city_b = distance_road_map[city + 1][2], distance_road_map[city + 1][3]
        distance = math.sqrt(((float(city_a[0]) - float(city_b[0])) ** 2) + ((float(city_a[1]) - float(city_b[1])) ** 2))
        total_distance += distance

    return total_distance


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    # 1) need to handel exceptions/errors for negative and out of range index

    if index1 < 0 or index2 < 0:
        return ("Error: indicies in roadmap contain negative values")

    if index1 > len(road_map) or index2 > len(road_map):
        return ("Error: indicies in roadmap out of range")

    import copy
    city_index1 = road_map[index1]
    city_index2 = road_map[index2]

    if index1 != index2:
        new_road_map = copy.deepcopy(road_map)
        new_road_map[index1] = city_index2
        new_road_map[index2] = city_index1
        new_total_distance = compute_total_distance(new_road_map)
        return new_road_map, new_total_distance
    else:
        return road_map, compute_total_distance(road_map)


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    new_road_map = [road_map[len(road_map) - 1]]
    for i in range(0, len(road_map)-1):
        new_road_map.append(road_map[i])
    return new_road_map


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    import random
    best_cycle = road_map, compute_total_distance(road_map)

    for x in range (0, 10000):
        rand_index1 = int(round(((len(road_map)-1) * random.random()), 0))
        rand_index2 = int(round(((len(road_map)-1) * random.random()), 0))
        this_cycle = swap_cities(best_cycle[0], rand_index1, rand_index2)
        if this_cycle[1] < best_cycle[1]:
            best_cycle = this_cycle
    return (best_cycle[0])


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """

    print("Starting City: " + road_map[0][0] + ", " + road_map[0][1])

    for i in range (1, len(road_map)):
        print("Next Location: " + road_map[i][0] + ", " + road_map[i][1] + "\t" + "Travel Distance: " + str(compute_total_distance([(road_map[i-1]),(road_map[i])])))

    print("Ending City: " + road_map[0][0] + ", " + road_map[0][1]+ "\t" + "Travel Distance: " + str(compute_total_distance([(road_map[(len(road_map)-1)]),(road_map[0])])))

    print("total travel distance: " + str(compute_total_distance(road_map)))



def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    main_roadmap = read_cities('city-data.txt')
    print_cities(main_roadmap)
    best_cyclemap = find_best_cycle(main_roadmap)
    print_map(best_cyclemap)
    visualise(best_cyclemap)

def visualise(road_map):

    window = tkinter.Tk()
    window.title("Roap Map Visualisation")
    window.geometry('1600x1600')
    top_frame = tkinter.Frame(window).pack()
    bottom_frame = tkinter.Frame(window).pack(side="bottom")
    Label(top_frame, text = "WELCOME TO YOUR ROADMAP!").pack()

    my_canvas = Canvas(bottom_frame, width=1200, height=600, bg = 'white')
    my_canvas.pack()



    def write_slogan(i):
        my_canvas.create_line((float(road_map[i][2]) + 90) * 5, (float(road_map[i][3]) + 180) * 5,(float(road_map[i + 1][2]) + 90) * 5, (float(road_map[i + 1][3]) + 180) * 5,fill="red", arrow='last')

    #button = Button(window,
     #                  text="Previous City",
     #                  fg="red",
     #                  command=quit)
    #button.pack(side=BOTTOM)
    slogan = Button(window,
                       text="Next City",
                       command= write_slogan(i))
    slogan.pack(side=BOTTOM)

    # Creates all vertical lines at intevals of 10
    #for i in range(50, 1800, 20):
     #   my_canvas.create_line([(i, 50), (i, 1800)])

    # Creates all horizontal lines at intevals of 10
    #for i in range(50, 900, 20):
      #  my_canvas.create_line([(50, i), (3600, i)])

    #for i in range (0,len(road_map)-1):
     #   my_canvas.create_line((float(road_map[i][2])+90)*5, (float(road_map[i][3])+180)*5,(float(road_map[i+1][2])+90)*5, (float(road_map[i+1][3])+180)*5, fill = "red", arrow ='last')
     #   my_canvas.create_oval((float(road_map[i][2])+90)*5, (float(road_map[i][3])+180)*5,(float(road_map[i][2])+90)*5, (float(road_map[i][3])+180)*5, fill = "blue")

    mainloop()


if __name__ == "__main__":  # keep this in
    main()
