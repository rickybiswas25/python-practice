class ListManipulation:

    def manipulate(self):
        number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        print([number for number in number_list if number < 5])


ListManipulation().manipulate()
