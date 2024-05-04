

def main():
    # our list of tuples that we will use
    points = [(6, 5), (7, 9), (4, 7), (8, 2)]

    result = calc_distance(points)


    print(result)  


# function will accept two tuples that have 2 values in it
# E.g (x0, y0) and (x1, y1)
def euclideanDistance(coordinate1, coordinate2):
    # square((x0 - x1) + (y0 - y1))
    return pow((pow(coordinate1[0] - coordinate2[0], 2) + pow(coordinate1[1] - coordinate2[1], 2)), 0.5)


def calc_distance(points):
    distance = []
    # start from 0 index , End in the range of len(points -  1) second to the last
    for i in range(len(points) - 1):
        # start i + 1 index after i always, end with last index
        for e in range(i + 1, len(points)):
            # put always next (x, y) , (x, y)
            distance.append("{:.4f}".format(euclideanDistance(points[i], points[e])))
    
    for i in range(len(distance)):
        distance[i] = float(distance[i])
    
    return distance

if __name__ == "__main__":
    main()