#   Jichun Li, Xuedeliang Li
#   jichunli, xl74
#   CSE 415 Milestone B

import random
import numpy

#   m[i][j] = Probability of choosing to use dice j in next toss, given tossed dice i.
# TRANSITION_MATRIX = [[1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7],
#                      [1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7],
#                      [1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7],
#                      [1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7],
#                      [1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7],
#                      [1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7],
#                      [1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7]]

TRANSITION_MATRIX = [[0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                     [0.2, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1],
                     [0.2, 0.1, 0.3, 0.1, 0.1, 0.1, 0.1],
                     [0.2, 0.1, 0.1, 0.3, 0.1, 0.1, 0.1],
                     [0.2, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1],
                     [0.2, 0.1, 0.1, 0.1, 0.1, 0.3, 0.1],
                     [0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3]]

#   m[i][j] = Probability of get j = {1, 2, 3, 4, 5, 6} - 1 using dice i.
#   dice 0 is the fair dice, others are not.
NUMBER_MATRIX = [[1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6],
                 [0.8, 0.04, 0.04, 0.04, 0.04, 0.04],
                 [0.04, 0.8, 0.04, 0.04, 0.04, 0.04],
                 [0.04, 0.04, 0.8, 0.04, 0.04, 0.04],
                 [0.04, 0.04, 0.04, 0.8, 0.04, 0.04],
                 [0.04, 0.04, 0.04, 0.04, 0.8, 0.04],
                 [0.04, 0.04, 0.04, 0.04, 0.04, 0.8]]

#   v[i] = Probability of selecting dice i at the beginning.
INITIAL_SELECTION = [1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7]

def generate(n = 100, seed = 123456, initial = None, trans = None, num_prob = None):
    global TRANSITION_MATRIX, NUMBER_MATRIX, INITIAL_SELECTION
    random.seed(seed)
    trans_m_cum = None
    init_selection_cum = None
    number_prob_cum = None

    if None == initial:
        init_selection_cum = numpy.cumsum(INITIAL_SELECTION)
    else:
        init_selection_cum = numpy.cumsum(initial)

    if None == trans:
        trans_m_cum = numpy.cumsum(TRANSITION_MATRIX, 1)
    else:
        trans_m_cum = numpy.cumsum(trans, 1)

    if None == num_prob:
        number_prob_cum = numpy.cumsum(NUMBER_MATRIX, 1)
    else:
        number_prob_cum = numpy.cumsum(num_prob, 1)

    result = []
    dices = []

    #   First toss using INITIAL_SELECTION
    first_rand = random.random()
    dice = 0

    if first_rand < init_selection_cum[0]:
        dice = 0
    elif first_rand < init_selection_cum[1]:
        dice = 1
    elif first_rand < init_selection_cum[2]:
        dice = 2
    elif first_rand < init_selection_cum[3]:
        dice = 3
    elif first_rand < init_selection_cum[4]:
        dice = 4
    elif first_rand < init_selection_cum[5]:
        dice = 5
    else:
        dice = 6

    dice_number = 0
    dice_num_rand = random.random()

    if dice_num_rand < number_prob_cum[dice][0]:
        dice_number = 1
    elif dice_num_rand < number_prob_cum[dice][1]:
        dice_number = 2
    elif dice_num_rand < number_prob_cum[dice][2]:
        dice_number = 3
    elif dice_num_rand < number_prob_cum[dice][3]:
        dice_number = 4
    elif dice_num_rand < number_prob_cum[dice][4]:
        dice_number = 5
    else:
        dice_number = 6

    result.append(dice_number)
    dices.append(dice)
    last_dice = dice

    for i in range(1, n):
        dice_rand = random.random()
        this_dice = 0
        this_dice_number = 0

        if dice_rand < trans_m_cum[last_dice][0]:
            this_dice = 0
        elif dice_rand < trans_m_cum[last_dice][1]:
            this_dice = 1
        elif dice_rand < trans_m_cum[last_dice][2]:
            this_dice = 2
        elif dice_rand < trans_m_cum[last_dice][3]:
            this_dice = 3
        elif dice_rand < trans_m_cum[last_dice][4]:
            this_dice = 4
        elif dice_rand < trans_m_cum[last_dice][5]:
            this_dice = 5
        else:
            this_dice = 6

        dice_num_rand = random.random()

        if dice_num_rand < number_prob_cum[this_dice][0]:
            this_dice_number = 1
        elif dice_num_rand < number_prob_cum[this_dice][1]:
            this_dice_number = 2
        elif dice_num_rand < number_prob_cum[this_dice][2]:
            this_dice_number = 3
        elif dice_num_rand < number_prob_cum[this_dice][3]:
            this_dice_number = 4
        elif dice_num_rand < number_prob_cum[this_dice][4]:
            this_dice_number = 5
        else:
            this_dice_number = 6

        result.append(this_dice_number)
        dices.append(this_dice)
        last_dice = this_dice

    return dices, result
