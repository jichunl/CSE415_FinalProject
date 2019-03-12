#   Jichun Li, Xuedeliang Li
#   jichunli, xl74
#   CSE 415 Milestone C

import csv


def format_data():
    riding_stats = []
    weather_stats = {}
    weather_count = {}
    weather_type = []

    f1 = open("riding_stats.csv")
    reader1 = csv.reader(f1)

    f2 = open("weather_condition.csv")
    reader2 = csv.reader(f2)

    #   Convert CSV file into python list.
    for item in reader1:
        if reader1.line_num == 1:
            continue
        riding_stats.append(item)
        weather_type.append(item[0])

    temp = []
    for item in reader2:
        if reader2.line_num == 1:
            continue
        temp.append(item)

    #   The weather condition is stored by time sequence.
    #   Need to calculate (day1, day2) weather pairs
    #   and the number of days that each kind of weather appears
    #   to approximate transmission matrix.
    for i in range(len(temp) - 1):
        weather1 = temp[i][1]
        weather2 = temp[i + 1][1]

        if weather1 not in weather_count:
            weather_count[weather1] = 0

        weather_count[weather1] = weather_count[weather1] + 1

        if (weather1, weather2) not in weather_stats:
            weather_stats[(weather1, weather2)] = 0

        weather_stats[(weather1, weather2)] = weather_stats[(weather1, weather2)] + 1

    #   Calculate the days of each kind of weather to approximate initial selection
    #   probability of weathers.
    total_days = 0
    initial_selection = []
    for i in range(5):
        initial_selection.append(int(riding_stats[i][1]))
        total_days += int(riding_stats[i][1])

    initial_selection = [i / total_days for i in initial_selection]

    transmission_matrix = []
    for c1 in weather_count:
        row = []
        for c2 in weather_count:
            if (c1, c2) in weather_stats:
                row.append(weather_stats[(c1, c2)] / weather_count[c1])
            else:
                row.append(0.0)

        transmission_matrix.append(row)

    #   Use relative probabilities to approximate emission matrix
    #   Use bike in clear weather = 0.5
    #   other cases prob. = 0.5 * Avg usage in other cases / Avg usage in clear
    emission_matrix = [[0.5, 0.5]]

    for i in range(1, 5):
        positive_rate = 0.5 * float(riding_stats[i][3]) / float(riding_stats[0][3])
        emission_matrix.append([positive_rate, 1 - positive_rate])

    return transmission_matrix, emission_matrix, initial_selection, weather_type
