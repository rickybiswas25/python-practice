import datetime;


class CharachterInput:
    # https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

    def doTask(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        current_year = datetime.datetime.now().year
        print("Hi {}. You will be 100 years old in {} year".format(name, current_year + (100 - int(age))))


CharachterInput().doTask()
