import datetime


class CharacterInput:
    # https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

    def doTask(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        print_time = int(input("How many times you want to see this message? "))
        for time in range(print_time):
            if age > 100:
                print("Hi", name, "You are already 100")
            else:
                print("Hi", name, "You will be 100 in year ", datetime.datetime.now().year + 100 - int(age))


CharacterInput().doTask()
