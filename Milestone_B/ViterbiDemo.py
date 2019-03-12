#   Jichun Li, Xuedeliang Li
#   jichunli, xl74
#   CSE 415 Milestone C

import ViterbiDiceFinder as vdf


def default_demo():
    demo_result = vdf.demo(n=-1)

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
    default_demo()
