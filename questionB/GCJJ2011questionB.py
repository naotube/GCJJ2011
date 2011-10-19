#!/usr/bin/env python

class Coffee():
    def __init__(self, amount, limit, score):
        self.amount = amount
        self.limit = limit
        self.score = score

def todays_coffee(coffees, coffee_days):
    coffees_in_choise = [coffee for coffee in coffees if coffee.limit >= coffee_days]
    if coffees_in_choise == []:
        return 0, coffees
    coffee = max(coffees_in_choise, key=lambda x:x.score)
    coffee.amount -= 1
    if coffee.amount <= 0:
        coffees.remove(coffee)
    return coffee.score, coffees

def main(problem):
    with open(problem, 'r') as input_data:
        how_many_cases = input_data.__next__()
        how_many_cases = int(how_many_cases.rstrip())

        case_number = 1
        for line in input_data:
            line = line.rstrip()
            line = line.split()
            coffee_types = int(line[0])
            coffee_days = int(line[1])

            coffees = []
            for t in range(coffee_types):
                line = input_data.__next__()
                line = line.rstrip()
                line = line.split()
                amount = int(line[0])
                limit = int(line[1])
                score = int(line[2])
                coffees.append(Coffee(amount, limit, score))

            answer = 0
            while True:
                if coffees == []:
                    break
                todays_score, coffees = todays_coffee(coffees, coffee_days)
                answer += todays_score
                coffee_days -= 1
                if coffee_days <= 0:
                    break

            print("Case #{}: {}".format(case_number, answer))
            case_number += 1

if __name__ == "__main__":
    import sys
    try:
        problem = sys.argv[1]
    except Exception:
        raise
    main(problem)

