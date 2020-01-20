class StringReverseOrder:

    def reverse(self):
        name = input("Write a sentence: ")
        splitted_name = name.split(" ")

        for count in reversed(range(0, len(splitted_name))):
            print(splitted_name[count])


StringReverseOrder().reverse()
