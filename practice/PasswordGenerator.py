import random


class PasswordGenerator:

    def generate(self):
        alphabet_list = ["a", "A", "b", "B", "c", "C"]
        number_list = [1, 2, 3, 4, 5, 6]
        sign_list = ["!", "@", "$", "%"]
        times = int(input("How strong you want to generate the password? "))
        password = ""
        for num in range(0, times):
            password += random.choice(alphabet_list)
            password += str(random.choice(number_list))
            password += random.choice(sign_list)

        print("Your password is: ", password)


PasswordGenerator().generate()
