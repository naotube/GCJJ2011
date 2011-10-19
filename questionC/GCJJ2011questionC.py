#!/usr/bin/env python

def how_many_1s_bin(number):
    return bin(number)[2:].count('1')

def main(problem):
    with open(problem, 'r') as input_data:
        how_many_cases = input_data.__next__()
        how_many_cases = int(how_many_cases.rstrip())

        case_number = 1
        for line in input_data:
            line = line.rstrip()
            number = int(line)

            order = 0
            max_ones = 0
            while True:
                A = 2 ** order - 1
                B = number - A
                if B < 0:
                    break
                ones = how_many_1s_bin(A) + how_many_1s_bin(B)
                if ones >= max_ones:
                    max_ones = ones
                order += 1

            answer = max_ones

            print("Case #{}: {}".format(case_number, answer))
            case_number += 1

if __name__ == "__main__":
    import sys
    try:
        problem = sys.argv[1]
    except Exception:
        raise
    main(problem)

