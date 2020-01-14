import random


class GuessingGameTwo:

    def game(self):
        print("Think a number in your head.\n I will try to guess it.\n If the number is high"
              "press 'h'.\nif the number is low press l\n and if the number is right press r\n\n\n")

        high = "h"
        low = "l"
        right = "r"
        computer_number = random.randint(0, 99)
        number_deduced = 100
        while True:
            print("Is this your number: ", int(computer_number))
            result = input("r/h/l: ")
            if result == high:
                number_deduced = number_deduced - number_deduced / 2
                print("New number deduced ", number_deduced)
                computer_number = computer_number - number_deduced
            elif result == low:
                number_deduced = number_deduced - number_deduced / 2
                print("New number deduced ", number_deduced)
                computer_number = computer_number + number_deduced
            elif result == right:
                break


GuessingGameTwo().game()
