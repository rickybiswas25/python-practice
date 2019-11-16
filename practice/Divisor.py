class Divisor:

    def print_all_divisor(self):
        #https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
        number = int(input("Enter the number "))
        divisor_list = []
        for num in range(1, number):
            if number % num == 0:
                divisor_list.append(num)
        print(divisor_list)


Divisor().print_all_divisor()
