class FileOverlap:

    def check(self):
        f = open("resources/primenumbers.txt", "r")
        prime_number_content = f.read().split("\n")
        f.close()
        f = open("resources/happynumbers.txt")
        happy_number_content = f.read().split("\n")
        overlapping_number = [num for num in prime_number_content if num in happy_number_content]
        print(overlapping_number)


FileOverlap().check()
