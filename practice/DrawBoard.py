class DrawBoard:

    def draw(self):
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        for line in range(0, row):
            print(" ")
            self.print_row(row)
            print("")
            for c in range(0, col+ 1):
                print("| ", end=" "),
        print("")
        self.print_row(row)

    def print_row(self, row):
        for r in range(0, row + 1):
            print("--", end=" "),


DrawBoard().draw()
