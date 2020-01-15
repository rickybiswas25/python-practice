class MaxOfThree:


    def find_max(self):
        first_number = int(input("Take first number: "))
        second_number = int(input("Take second number: "))
        third_number = int(input("Take third number: "))
        max_number = first_number

        if max_number < second_number:
            max_number = second_number
        if max_number < third_number:
            max_number = third_number

        print("The maximum number is ", max_number)


MaxOfThree().find_max()
