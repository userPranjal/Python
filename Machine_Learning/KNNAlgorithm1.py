import math

def EuclideanDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans

def KNNClassifier():

    border = "-" * 30

    Data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'}
    ]

    print(border)
    print("KNN Classifier")
    print(border)

    for i in Data:
        print(i)

    print(border)

    # Accept X and Y coordinates of a new point from user
    x = int(input("Enter X coordinate: "))
    y = int(input("Enter Y coordinate: "))

    new_point = {'X': x, 'Y': y}

    # Calculate the distance
    for d in Data:
        d['distance'] = EuclideanDistance(d, new_point)

    # Sort data according to distance
    sorted_data = sorted(Data, key=lambda item: item['distance'])

    # Select K nearest neighbours
    k = 3

    nearest = sorted_data[:k]

    print(border)
    print("Nearest 3 members are :")
    print(border)

    for d in nearest:
        print(d['point'], "- Distance:", format(d['distance'], ".2f"))

    print(border)

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

    print("Predicted Class : ", Name)

    print(border)

def main():
    KNNClassifier()

if __name__ == "__main__":
    main()