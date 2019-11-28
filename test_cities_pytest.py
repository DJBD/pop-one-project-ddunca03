import pytest
from cities import *


def test_compute_total_distance():
    #simple two city test (test to see if pythagoras formulae is working correctly (travels along the same path twice) (there and back again)
    road_map1 = [("Kentucky", "Frankfort", 0, 0),("Delaware", "Dover", 12, 5)]
    assert compute_total_distance(road_map1) == 26.0



def test_swap_cities():
    road_map2 = ([("STATE", "CITY",0.0, 0.0),("STATE1", "CITY1", 0.0, 0.0)])

    assert swap_cities(road_map2,0,1) == ([("STATE1", "CITY1", 0.0, 0.0),("STATE", "CITY", 0.0, 0.0)],0.0)







def test_shift_cities():
    road_map3 = ([("STATE", "CITY",0.0, 0.0),("STATE1", "CITY1", 0.0, 0.0)])

    assert shift_cities(road_map3) == [("STATE1", "CITY1", 0.0, 0.0),("STATE", "CITY", 0.0, 0.0)]
        

    
   


