#   Jichun Li, Xuedeliang Li
#   jichunli, xl74
#   CSE 415 Milestone C


def hmm_forward(sequence, transmission_matrix, emission_matrix, initial_selection):
    N = len(sequence)           # sequence length
    S = len(initial_selection)  # states number

    output_matrix = []

    #   The first condition must be calculated separately based on initial_selection probabilities.
    t1 = []
    for i in range(S):
        t1.append(initial_selection[i] * emission_matrix[i][sequence[0]])

    output_matrix.append(t1)

    for i in range(1, N):
        ti = []
        for j in range(S):
            #   Probability of getting sequence[i] as result from state[j]
            #   given known states from t_[i-1]
            prob_k = 0
            for k in range(S):
                #   Adding the probability of getting state[j] from every possible
                #   states from previous states, known the previous sequence
                prob_k = prob_k + output_matrix[i - 1][k] * transmission_matrix[k][j]

            #   Given state[j], get sequence[i]
            prob_k = prob_k * emission_matrix[j][sequence[i]]
            ti.append(prob_k)

        output_matrix.append(ti)

    return output_matrix, sum(output_matrix[N - 1])


if __name__ == "__main__":
    initial_selection = [0.2, 0.4, 0.4]
    transition_matrix = [[0.5, 0.2, 0.3],
                         [0.3, 0.5, 0.2],
                         [0.2, 0.3, 0.5]]
    emission_matrix = [[0.5, 0.5],
                       [0.4, 0.6],
                       [0.7, 0.3]]

    result = hmm_forward([0, 1, 0], transition_matrix, emission_matrix, initial_selection)
    print(result[0])
    print(result[1])
