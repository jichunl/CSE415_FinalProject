#   Jichun Li, Xuedeliang Li
#   jichunli, xl74
#   CSE 415 Milestone B

import random
import numpy

#   t[i][j] = Probability of using dice j in next toll,
#   giving used i in current toll.
TRANSITION_MATRIX = [[0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                     [0.2, 0.8, 0, 0, 0, 0, 0],
                     [0.2, 0, 0.8, 0, 0, 0, 0],
                     [0.2, 0, 0, 0.8, 0, 0, 0],
                     [0.2, 0, 0, 0, 0.8, 0, 0],
                     [0.2, 0, 0, 0, 0, 0.8, 0],
                     [0.2, 0, 0, 0, 0, 0, 0.8]]

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

    if initial is None:
        init_selection_cum = numpy.cumsum(INITIAL_SELECTION)
    else:
        init_selection_cum = numpy.cumsum(initial)

    if None == trans:
        trans_m_cum = numpy.cumsum(TRANSITION_MATRIX, 1)
    else:
        trans_m_cum = numpy.cumsum(trans, 1)

    if num_prob is None:
        number_prob_cum = numpy.cumsum(NUMBER_MATRIX, 1)
    else:
        number_prob_cum = numpy.cumsum(num_prob, 1)

    result = []
    dices = []

    #   1. First toss using INITIAL_SELECTION
    first_rand = random.random()
    dice = 0

    for i in range(len(init_selection_cum)):
        if first_rand < init_selection_cum[i]:
            dice = i
            break

    dice_number = 0
    dice_num_rand = random.random()

    #   2. Decide the number of the first toss
    for i in range(len(number_prob_cum[dice])):
        if dice_num_rand < number_prob_cum[dice][i]:
            dice_number = i + 1
            break

    result.append(dice_number)
    dices.append(dice)
    last_dice = dice

    #   3. Decide other toss based on previous one toss
    for i in range(1, n):
        dice_rand = random.random()
        this_dice = 0
        this_dice_number = 0

        for j in range(len(trans_m_cum[last_dice])):
            if dice_rand < trans_m_cum[last_dice][j]:
                this_dice = j
                break

        dice_num_rand = random.random()

        #   4. Decide current number given the chosen dice
        for k in range(len(number_prob_cum[this_dice])):
            if dice_num_rand < number_prob_cum[this_dice][k]:
                this_dice_number = k + 1
                break

        result.append(this_dice_number)
        dices.append(this_dice)
        last_dice = this_dice

    return dices, result
