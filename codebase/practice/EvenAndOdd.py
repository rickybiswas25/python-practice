class EvenAndOdd:

    def print_status_of_number(self):
        # https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
        number = int(input("What is the number you want to process: "))
        check = int(input("What is the number you want to check if dividable: "))
        status = "even" if number % 2 == 0 else "odd"
        is_dividable = number % check == 0
        if is_dividable:
            print("The number", number, "is dividable by", check)
        else:
            print("The number", number, "is", status)


EvenAndOdd().print_status_of_number()
