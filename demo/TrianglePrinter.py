class TrianglePrinter:

    def print(self, row):
        for i in range(1, row):
            for j in range(0, i):
                print("*", end='')
            print()


TrianglePrinter().print(100)
