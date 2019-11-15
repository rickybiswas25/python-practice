class Loops:

    def test(self):
        x = 0
        if x < 0:
            print("X is less than 0")
        elif x == 0:
            print("X is equal to 0")

    def loops(self):
        words = [1, 2, 3, 4, 5]
        for w in words[:]:
            if w > 3:
                words.append(w)

        print(words)

    def range(self):
        for i in range(5, 10):
            print(i)

    def break_this(self):
        words = [1, 2, 3, 4, 5]
        for w in words:
            if w == 4:
                continue

            print(w)

    def func_with_args(self, words):
        print(words)

    def default_args_val(self, string, val=4):
        print(string, val)


obj = Loops()
obj.default_args_val("The value without passing")
obj.default_args_val("The value with passing", 6)

obj.break_this()

