"""
Q: You receive a list of coordinates in sequence.
Each coordinate should be within 100m of the previous coordinate.
How would you detect a coordinate that is more than 100m from the previous one?
"""
import math
def coordinates_check(coordinates):

    for k, v in enumerate(coordinates):
        # print(coordinates[k+1])
        distance = math.dist(coordinates[k], coordinates[k+1])
        # print(distance)
        if distance > 100:
            return coordinates[k+1]

    return None


if __name__ == '__main__':
    coordinates = [[19, 52], [20, 52], [24, 52], [450, 52], [20, 53], [22, 53], [20, 54], [21, 54]]

    result = coordinates_check(coordinates)
    print(result)
