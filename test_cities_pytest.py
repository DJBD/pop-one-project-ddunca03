import pytest
from cities import *
simple_road_map = [("STATE", "CITY",0.0, 0.0),("STATE1", "CITY1", 12, 0.0),("STATE2", "CITY2", 12, 5.0),("STATE3", "CITY3", 0.0, 5.0)]

def test_compute_total_distance_1(): # simple test to see if pythagoras formulae is working correctly
    assert compute_total_distance(simple_road_map) == 34.0

def test_swap_cities_1(): # a test that swaps
    assert swap_cities(simple_road_map,0,1) == ([("STATE1", "CITY1", 12, 0.0),("STATE", "CITY",0.0, 0.0),("STATE2", "CITY2", 12, 5.0),("STATE3", "CITY3", 0.0, 5.0)], 50.0)

def test_swap_cities_2(): # a test that swaps with itself/ should return the same roadmap
    assert swap_cities(simple_road_map, 2, 2) == ([("STATE", "CITY",0.0, 0.0),("STATE1", "CITY1", 12, 0.0),("STATE2", "CITY2", 12, 5.0),("STATE3", "CITY3", 0.0, 5.0)], 34.0)

def test_swap_cities_3(): # a test that returns an error statement for negative indicies
    assert swap_cities(simple_road_map, -1, 3) == "Error: indicies in roadmap contain negative values"

def test_swap_cities_4(): # a test that returns an error statement for indicies out of range
    assert swap_cities(simple_road_map, 1, 6) == "Error: indicies in roadmap out of range"

def test_swap_cities_5(): # a test that measures the length of the roadmap
    simple_road_map_length = len(simple_road_map)
    new_swapped_roadmap = swap_cities(simple_road_map, 2, 1)
    assert len(new_swapped_roadmap[0]) == simple_road_map_length

def test_shift_cities_1():
    assert shift_cities(simple_road_map) == [("STATE3", "CITY3", 0.0, 5.0),("STATE", "CITY",0.0, 0.0),("STATE1", "CITY1", 12, 0.0),("STATE2", "CITY2", 12, 5.0)]

def test_shift_cities_2(): # a test that measures the length of the roadmap
    simple_road_map_length = len(simple_road_map)
    new_shifted_roadmap = shift_cities(simple_road_map)
    assert len(new_shifted_roadmap[0]) == simple_road_map_length
    
