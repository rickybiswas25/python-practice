class Divisor:

    def find_all_divisor(self, number):
        # https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
        divisor_list = []
        for num in range(1, number + 1):
            if number % num == 0:
                divisor_list.append(num)
        return divisor_list

