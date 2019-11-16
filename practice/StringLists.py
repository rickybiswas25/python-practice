class StringLists:

    def print_string(self):
        # https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
        name = input("What is the input ")
        length = len(name) - 1
        is_palindrome = True
        for n in range(0, length):
            if name[n] != name[length - n]:
                is_palindrome = False
                break

        if is_palindrome:
            print("Palindrome")
        else:
            print("Not palindrome")


StringLists().print_string()
