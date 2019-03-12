#   Jichun Li, Xuedeliang Li
#   jichunli, xl74
#   CSE 415 Milestone C

import ViterbiDiceFinder as vdf


def default_demo():
    demo_result = vdf.demo(n=-1)
    output(demo_result)


def custom_demo():
    n = 1000
    seed = 987654
    number_sequence = None
    actual_dice_sequence = None
    transmission_matrix = []
    emission_matrix = []
    initial_selection = []

    demo_result = vdf.demo(n, seed, number_sequence, actual_dice_sequence,
                           transmission_matrix, emission_matrix, initial_selection)
    output(demo_result)


#   Output the result from demo to standard output
def output(demo_result):
    actual_dice_sequence = demo_result[0][0]
    number_sequence = demo_result[0][1]
    predict_dice_sequence = demo_result[1]
    trellis_diagram = demo_result[2]

    test_size = len(number_sequence)
    state_number = len(trellis_diagram)

    for i in range(test_size):
        print("Used dice " + str(actual_dice_sequence[i]) + ", " +
              "Got number " + str(number_sequence[i]) + ", " +
              "Predicted dice " + str(predict_dice_sequence[i]) + ".")

        print("Probability of getting the number using each possible dice " +
              "given last max possible dice: ")

        for j in range(state_number):
            print("Dice " + str(j) + ": " + "{:0.2e}".format(trellis_diagram[j][i + 1][0]), end="; ")

        print("\n")


if __name__ == "__main__":
    if True:
        default_demo()

    if False:
        custom_demo()
