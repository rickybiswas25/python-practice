class MaxOfThree:

    def find_max(self, first_number, second_number, third_number):
        max_number = first_number
        if max_number < second_number:
            max_number = second_number
        if max_number < third_number:
            max_number = third_number

        return max_number
