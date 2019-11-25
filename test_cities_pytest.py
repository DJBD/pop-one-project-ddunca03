import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1) == 11.111

           

    
def test_swap_cities():
    road_map2 = ([("STATE", "CITY", 121.121, 55.555),("STATE1", "CITY1", 39.161, -75.526)])

    index1 = 0
    index2 = 1

    assert swap_cities(road_map2) == ([("STATE", "CITY", 121.121, 55.555),\
                ("STATE1", "CITY1", 39.161, -75.526)])

def test_shift_cities():
    road_map3 = ([("STATE", "CITY", 121.121, 55.555),\
                ("STATE1", "CITY1", 39.161, -75.526)])

    assert shift_cities() == ([("STATE", "CITY", 121.121, 55.555),\
                ("STATE1", "CITY1", 39.161, -75.526)])
        

    
   


