# VIRAY, Geraldine Marie M.
# CMSC 170 X-5L
# 2021-12525

from collections import Counter

# function to calculate euclidean distance between two data points
def euclidean_distance(item, input):
    sum = 0
    for i in range(len(item)-1):
        sum += ((item[i] - input[i]) ** 2)

    return sum
    
# function to read input file
def read_input_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = [list(map(float, line.split(','))) for line in file]
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    return data

# class declaration
class KNN:
    def __init__(self, list, distance):
        # list is the data point
        self.list = list
        # distance is the euclidean distance between the data point and the input
        self.distance = distance

# file names
training_data_file = 'diabetes.csv'
input_file = 'input.in'

# list of output
output = []

# read files
training_data = read_input_file(training_data_file)
input_data = read_input_file(input_file)

# get k
k = int(input("Enter k: "))


if training_data is not None and input_data is not None:
    # calculate euclidean distance for each input
    for input in input_data:
        distances = []
        # calculate euclidean distance for each data point in training data
        for item in training_data:
            sum = euclidean_distance(item, input)
            # append a new instance of KNN class
            distances.append(KNN(item, sum))

        # sort the classes
        distances.sort(key=lambda x: x.distance)

        # get the k nearest neighbors
        classification_list = []

        # get the classification of the k nearest neighbors
        for i in range(k):
            classification_list.append(distances[i].list[-1])

            classification = max(set(classification_list), key=classification_list.count)

        # append the classification to the input
        new_item = []
        new_item.extend(input)
        new_item.append(classification)

        # append the input to the output
        output.append(new_item)

    # write output to file
    with open('output.txt', 'w') as file:
        for item in output:
            # print(output[i])
            file.write(str(item) + "\n")
    
    print("output.txt created.")