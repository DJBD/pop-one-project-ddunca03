import os
from cities import *

a = read_cities('city-data.txt')

#print_cities(a)

print(compute_total_distance(a))

#print((swap_cities(a, 0, 1)))

#print(shift_cities(a))

print(find_best_cycle(a))