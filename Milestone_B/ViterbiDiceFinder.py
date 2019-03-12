#   Jichun Li, Xuedeliang Li
#   jichunli, xl74
#   CSE 415 Milestone B

import DefaultSequenceGenerator as g


#   Take in a number of sequence, generate the
def viterbi_dp(num_sequence, trans_matrix, number_matrix, initial_selection):
    obs = len(num_sequence)
    states = len(initial_selection)

    #   Initialize dynamic programming table
    temp = [(0, 0) for i in range(len(num_sequence))]
    temp.insert(0, (1, -1))
    OPT = [temp.copy() for i in range(states)]

    #   The probability of getting to the first state is different from
    #   that of getting to sequential states,
    #   need to be calculated separately.
    first_number = num_sequence[0]
    for i in range(states):
        number_prob = initial_selection[i] * number_matrix[i][first_number - 1] * OPT[i][0][0]
        OPT[i][1] = (number_prob, -1)

    for i in range(2, obs + 1):
        current_number = num_sequence[i - 1]

        #   Calculate the current max possible dice given the max possible dice previously
        for current_state in range(states):
            max_prob = -1
            max_last = -1

            #   Calculate the max probability for the current dice
            #   given the transmission matrix, the probability of getting current number given current dice,
            #   and the probability of getting last dice.
            for last_state in range(states):
                delta = trans_matrix[last_state][current_state] \
                        * number_matrix[current_state][current_number - 1] * OPT[last_state][i - 1][0]
                #   Break tie by always record the first
                if delta > max_prob:
                    max_prob = delta
                    max_last = last_state

            #   Store the probability of getting current dice and the best last dice into the OPT table for back trace.
            OPT[current_state][i] = (max_prob, max_last)

    return OPT


def viterbi_tb(opt):
    states = len(opt)
    obs = len(opt[0]) - 1
    result = []

    last_state = 0
    for i in range(states):
        if opt[i][obs][0] > opt[last_state][obs][0]:
            last_state = i

    result.append(last_state)
    for i in range(obs, 0, -1):
        next_state = opt[last_state][i][1]
        result.append(next_state)
        last_state = next_state

    result.reverse()
    return result


def demo(n=-1, seed=234567, number_sequence=None, dice_sequence=None,
         transition_matrix=None, emission_matrix=None, initial_selection=None):
    if n == -1:
        #   Use default 7 dices example
        sampleInput = g.generate(n=50, seed=234567)
        OPT = viterbi_dp(sampleInput[1], g.TRANSITION_MATRIX, g.NUMBER_MATRIX, g.INITIAL_SELECTION)
        result = viterbi_tb(OPT)

        #   Return generated dice sequence
        return sampleInput, result[1:], OPT

    else:
        #   Use custom settings:
        if number_sequence is None:
            #   Generate sample sequence
            sampleInput = g.generate(n, seed, initial_selection, transition_matrix, emission_matrix)
            OPT = viterbi_dp(sampleInput[1], transition_matrix, emission_matrix, initial_selection)
            result = viterbi_tb(OPT)
            return sampleInput, result[1:], OPT
        else:
            #   Calculate from given sequence
            OPT = viterbi_dp(number_sequence, transition_matrix, emission_matrix, initial_selection)
            result = viterbi_tb(OPT)
            return [dice_sequence, number_sequence], result[1:], OPT
