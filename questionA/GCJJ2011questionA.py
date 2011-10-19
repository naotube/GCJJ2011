#!/usr/bin/env python

def shuffle(cards, cut_from, cut_amount):
    cutA = cut_from - 1
    cutB = cutA + cut_amount
    return cards[cutA:cutB] + cards[0:cutA] + cards[cutB:]

def main(problem):
    with open(problem, 'r') as input_data:
        how_many_cases = input_data.__next__()
        how_many_cases = int(how_many_cases.rstrip())

        case_number = 1
        for line in input_data:
            line = line.rstrip()
            line = line.split()

            how_many_cards = int(line[0])
            how_many_shuffles = int(line[1])
            target_card = int(line[2])

            cards = [i for i in range(1, how_many_cards + 1)]

            while how_many_shuffles > 0:
                line = input_data.__next__()
                line = line.rstrip()
                line = line.split()
                cut_from = int(line[0])
                cut_amount = int(line[1])

                cards = shuffle(cards, cut_from, cut_amount)
                how_many_shuffles -= 1

            print("Case #{}: {}".format(case_number, cards[target_card - 1]))
            case_number += 1

if __name__ == "__main__":
    import sys
    try:
        problem = sys.argv[1]
    except Exception:
        raise
    main(problem)

