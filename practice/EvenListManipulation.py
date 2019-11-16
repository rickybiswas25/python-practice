class EvenListManipulation:

    def print_list(self):
        #https: // www.practicepython.org / exercise / 2014 / 03 / 19 / 07 - list - comprehensions.html
        a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        print([number for number in a if number % 2 == 0])


EvenListManipulation().print_list()