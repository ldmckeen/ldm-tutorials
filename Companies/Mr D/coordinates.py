"""
Q: You receive a list of coordinates in sequence.
Each coordinate should be within 100m of the previous coordinate.
How would you detect a coordinate that is more than 100m from the previous one?
"""

import math

def detect_coordinate(coordinates):
    print(f"coordinates: {coordinates}")
    
    # for i in range(len(coordinates) - 1):
    #     distance = round(math.dist(coordinates[i], coordinates[i+1]), 2)
    #     print(f"Index:{i}, Coord:{coordinates[i]}, Distance:{distance}")
    #     if distance > 100:
    #         print(f"Coord:{coordinates[i]} is more than 100m from it's previous Coordinate")
    
    for i, v in enumerate(coordinates[:-1]):
        distance = round(math.dist(coordinates[i], coordinates[i+1]), 2)
        print(f"Index:{i}, Coord:{coordinates[i]}, Distance:{distance}")
        if distance > 100:
            print(f"Coord:{coordinates[i]} is more than 100m from it's previous Coordinate")
            

if __name__ == '__main__':
    coordinates = [[19, 52], [20, 52], [24, 52], [450, 52], [20, 53], [22, 53], [20, 54], [21, 54]]
    # coordinates = [(10, 20), (30, 40), (50, 60), (70, 80)]
    locations = [(40.7128, -74.0060), (34.0522, -118.2437), (51.5074, -0.1278), (-33.8688, 151.2093)]
    points_3d = [(0, 0, 0), (10, 200, 30), (40, 50, 60), (70, 80, 900)]
    
    print(detect_coordinate(points_3d))
    
