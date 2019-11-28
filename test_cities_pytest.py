import pytest
from cities import *
simple_road_map = [("STATE", "CITY",0.0, 0.0),("STATE1", "CITY1", 12, 0.0),("STATE2", "CITY2", 12, 5.0),("STATE3", "CITY3", 0.0, 5.0)]

def test_compute_total_distance():
    #simple test to see if pythagoras formulae is working correctly
    assert compute_total_distance(simple_road_map) == 34.0


def test_swap_cities_1():
    assert swap_cities(simple_road_map,0,1) == ([("STATE1", "CITY1", 12, 0.0),("STATE", "CITY",0.0, 0.0),("STATE2", "CITY2", 12, 5.0),("STATE3", "CITY3", 0.0, 5.0)], 50.0)

    #write a test that swaps with itself/ should return the same roadmap
    #write a test that deals with negitive indicies
    #write a test that measures the length of the roadmap



def test_shift_cities():
    assert shift_cities(simple_road_map) == [("STATE3", "CITY3", 0.0, 5.0),("STATE", "CITY",0.0, 0.0),("STATE1", "CITY1", 12, 0.0),("STATE2", "CITY2", 12, 5.0)]

    #write a test that swaps with itself/ should return the same roadmap
    #write a test that deals with negitive indicies
    #write a test that measures the length of the roadmap
        

    
   


