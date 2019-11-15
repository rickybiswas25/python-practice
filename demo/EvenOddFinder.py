class EvenOddFinder:

    def even_odd_numbers(self, number):
        if number == 0:
            print("The number is not prime")
            return
        if number < 0:
            print("Negative can not be accepted")
            return
        if number % 2 == 0:
            print("Even number found ", number)
        else:
            print("Odd number found ", number)


EvenOddFinder().even_odd_numbers(0)
EvenOddFinder().even_odd_numbers(-1)
EvenOddFinder().even_odd_numbers(5)
EvenOddFinder().even_odd_numbers(10)

