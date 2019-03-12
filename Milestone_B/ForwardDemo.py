#   Jichun Li, Xuedeliang Li
#   jichunli, xl74
#   CSE 415 Milestone C

import WeatherRide as wr
import ForwardAlgorithm as fa
import random


def default_demo():
    dat = wr.format_data()
    t_matrix = dat[0]
    e_matrix = dat[1]
    initial_selection = dat[2]
    weather_condition = dat[3]

    print("Possible weather conditions: " + str(weather_condition) + "\n")

    print("Transmission matrix \n" +
          "(same order as above from left to right and top to bottom): ")
    for i in range(len(t_matrix)):
        print(t_matrix[i])
    print()

    print("Emission matrix \n" +
          "(Ride bike / Not ride bike): ")
    for i in range(len(e_matrix)):
        print(weather_condition[i] + ": " + str(e_matrix[i]))
    print()

    test_riding_sequence = random_riding_sequence()
    print("Riding sequence: ")
    for i in test_riding_sequence:
        if i == 0:
            print("Ride bike", end="; ")
        else:
            print("Not ride bike", end="; ")
    print("\n")

    result = fa.hmm_forward(test_riding_sequence, t_matrix, e_matrix, initial_selection)
    trellis_diagram = result[0]
    final_prob = result[1]

    for i in range(len(trellis_diagram)):
        print("Ride? ", end=" ")
        if test_riding_sequence[i] == 0:
            print("Ride")
        else:
            print("Not ride")

        print("Probability of weather condition: ")
        for j in range(len(trellis_diagram[i])):
            print(weather_condition[j] + ": " + str("{:0.3e}".format(trellis_diagram[i][j])), end="; ")
        print()
    print()

    print("Probability of getting the sequence: " + str(final_prob))


def custom_demo(riding_sequence):
    dat = wr.format_data()
    t_matrix = dat[0]
    e_matrix = dat[1]
    initial_selection = dat[2]
    weather_condition = dat[3]

    print("Possible weather conditions: " + str(weather_condition) + "\n")

    print("Transmission matrix \n" +
          "(same order as above from left to right and top to bottom): ")
    for i in range(len(t_matrix)):
        print(t_matrix[i])
    print()

    print("Emission matrix \n" +
          "(Ride bike / Not ride bike): ")
    for i in range(len(e_matrix)):
        print(weather_condition[i] + ": " + str(e_matrix[i]))
    print()

    print("Riding sequence: ")
    for i in riding_sequence:
        if i == 0:
            print("Ride bike", end="; ")
        else:
            print("Not ride bike", end="; ")
    print("\n")

    result = fa.hmm_forward(riding_sequence, t_matrix, e_matrix, initial_selection)
    trellis_diagram = result[0]
    final_prob = result[1]

    for i in range(len(trellis_diagram)):
        print("Ride? ", end=" ")
        if riding_sequence[i] == 0:
            print("Ride")
        else:
            print("Not ride")

        print("Probability of weather condition: ")
        for j in range(len(trellis_diagram[i])):
            print(weather_condition[j] + ": " + str("{:0.3e}".format(trellis_diagram[i][j])), end="; ")
        print()
    print()

    print("Probability of getting the sequence: " + str(final_prob))


def random_riding_sequence(seed=123456, n=10):
    random.seed(seed)

    result = []
    for i in range(n):
        result.append(int(random.random() > 0.5))
    return result


if __name__ == "__main__":
    if True:
        default_demo()

    if False:
        riding_sequence = random_riding_sequence(seed=654321, n=100)
        custom_demo(riding_sequence)
