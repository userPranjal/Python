import math

def EuclideanDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans


def KNNClassifier(Data, new_point, k):

    # Calculate distance
    for d in Data:
        d['distance'] = EuclideanDistance(d, new_point)

    # Sort according to distance
    sorted_data = sorted(Data, key=lambda item: item['distance'])

    # Select K nearest neighbours
    nearest = sorted_data[:k]

    # Voting
    votes = {}

    for neighbours in nearest:
        label = neighbours['label']
        votes[label] = votes.get(label, 0) + 1

    # Find maximum votes
    iMax = 0
    Name = ""

    for d in votes:
        if votes[d] > iMax:
            iMax = votes[d]
            Name = d

    return Name

def main():

    Data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'}
    ]

    # Accept X and Y coordinates of a new point from user
    x = int(input("Enter X coordinate: "))
    y = int(input("Enter Y coordinate: "))

    new_point = {'X': x, 'Y': y}

    print("\nPrediction Results")

    # K = 1
    Result = KNNClassifier(Data, new_point, 1)
    print("K = 1 ->", Result)

    # K = 3
    Result = KNNClassifier(Data, new_point, 3)
    print("K = 3 ->", Result)

    # K = 5
    Result = KNNClassifier(Data, new_point, 5)
    print("K = 5 ->", Result)


if __name__ == "__main__":
    main()