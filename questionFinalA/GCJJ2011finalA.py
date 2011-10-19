#!/usr/bin/env python

from math import sin
from math import radians

def main(problem):
    with open(problem, 'r') as input_data:
        how_many_cases = input_data.__next__()
        how_many_cases = int(how_many_cases.rstrip())

        case_number = 1
        for line in input_data:
            line = line.rstrip()
            line = line.split()

            how_many_elements = int(line[0])
            angle = radians(360 / how_many_elements)

            line = input_data.__next__()
            line = line.rstrip()
            elements = [int(i) for i in line.split()]

            maximized = []
            for i in range(len(elements)):
                if i % 2 == 0:
                    maximized.append(max(elements))
                else:
                    maximized.insert(0,max(elements))
                elements.remove(max(elements))

            anthena = 0
            for i in range(len(maximized)):
                anthena += maximized[i] * maximized[i-1] * sin(angle) / 2

            answer = round(anthena, 9)
            if answer == int(answer):
                answer = int(answer)
            print("Case #{}: {}".format(case_number, answer))
            case_number += 1

if __name__ == "__main__":
    import sys
    try:
        problem = sys.argv[1]
    except Exception:
        raise
    main(problem)

