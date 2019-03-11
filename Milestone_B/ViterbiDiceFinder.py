#   Jichun Li, Xuedeliang Li
#   jichunli, xl74
#   CSE 415 Milestone B

import RandomSequenceGenerator as g


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

        for current_state in range(states):
            max_prob = -1
            max_last = -1
            for last_state in range(states):
                delta = trans_matrix[last_state][current_state] * number_matrix[current_state][current_number - 1] * OPT[last_state][i - 1][0]
                #   Break tie by always record the first
                if delta > max_prob:
                    max_prob = delta
                    max_last = last_state

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


if __name__ == '__main__':
    test_trans_matrix = [[0.9, 0.1],
                         [0.2, 0.8]]
    test_number_matrix = [[1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6],
                          [0.04, 0.04, 0.04, 0.04, 0.04, 0.8]]
    test_initial_selection = [1 / 2, 1 / 2]

    #   sampleInput = g.generate(n = 100, initial = test_initial_selection, trans = test_trans_matrix, num_prob = test_number_matrix)
    #   OPT = viterbi_dp(sampleInput[1], test_trans_matrix, test_number_matrix, test_initial_selection)
    sampleInput = g.generate(n=100, seed=234567)
    OPT = viterbi_dp(sampleInput[1], g.TRANSITION_MATRIX, g.NUMBER_MATRIX, g.INITIAL_SELECTION)
    result = viterbi_tb(OPT)
    #   print(result[1:])
    #   print(sampleInput[0])
    print(sum([result[i] != sampleInput[0][i - 1] for i in range (1, 101)]))
