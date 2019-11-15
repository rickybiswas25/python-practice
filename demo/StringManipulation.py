class StringManipulation:
    def compare(self, str):
        local_str = "Hello"

        if local_str == str:
            print("matched")
        else:
            print("Not matched")

    def manipulate(self, str):
        length_str = len(str)
        print("Length of a string ", length_str)

        count_of_i = str.count("i")
        print("Total number of 'i' present in the string ", count_of_i)

        print("Start and end manipulation ", str[0:5])

        delete_white_space = str.replace(" ", "")
        print("Deleting white space ", delete_white_space)

        reversed_str = ''.join(reversed(str))
        print("After reversing string ", reversed_str)


StringManipulation().compare("Hello")
StringManipulation().compare("Hello1")

StringManipulation().manipulate("Hi I am a boy")
