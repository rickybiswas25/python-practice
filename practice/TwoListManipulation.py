import random


class TwoListManipulation:


    def print_list(self):
        a = [random.randint(1, 100) for itr in range(10)]
        b = [random.randint(1, 100) for itr in range(10)]
        print(a)
        print(b)
        print(set([number for number in b if number in a]))


TwoListManipulation().print_list()
