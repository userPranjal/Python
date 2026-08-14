import math

def EuclideanDistance(P1, P2):
    Ans = math.sqrt((P1['Study'] - P2['Study'])**2 + (P1['Attendance'] - P2['Attendance'])**2)
    return Ans


def KNNClassifier():

    border = "-" * 30

    Data = [
        {'Study': 2, 'Attendance': 60, 'Result': 'Fail'},
        {'Study': 5, 'Attendance': 80, 'Result': 'Pass'},
        {'Study': 6, 'Attendance': 85, 'Result': 'Pass'},
        {'Study': 1, 'Attendance': 50, 'Result': 'Fail'}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    for d in Data:
        print(d)

    print(border)

    # Accept input from user
    study = int(input("Enter Study Hours: "))
    attendance = int(input("Enter Attendance: "))

    new_point = {
        'Study': study,
        'Attendance': attendance
    }

    print(border)
    print("Distances of all points :")
    print(border)

    # Calculate distance
    for d in Data:
        d['distance'] = EuclideanDistance(d, new_point)

    for d in Data:
        print(d)

    print(border)

    # Sort according to distance
    sorted_data = sorted(Data, key=lambda item: item['distance'])

    print("Sorted Data :")
    print(border)

    for d in sorted_data:
        print(d)

    print(border)

    # Select K = 3
    k = 3

    nearest = sorted_data[:k]

    print("Nearest 3 members are :")
    print(border)

    for d in nearest:
        print(d)

    print(border)

    # Voting
    votes = {}

    for neighbours in nearest:
        result = neighbours['Result']
        votes[result] = votes.get(result, 0) + 1

    print("Voting result is :")
    print(border)

    for d in votes:
        print("Name : ", d, "Number of votes : ", votes[d])

    print(border)

    # Find maximum votes
    iMax = 0
    Name = ""

    for d in votes:
        if votes[d] > iMax:
            iMax = votes[d]
            Name = d

    print("Predicted Result:", Name)

    print(border)


def main():
    KNNClassifier()

if __name__ == "__main__":
    main()