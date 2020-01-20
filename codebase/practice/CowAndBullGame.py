import random


def evaluate_user_entry(user_guessed_num, computer_guessed_num):
    cow = 0
    bull = 0
    user_list = [char for char in str(user_guessed_num)]
    computer_list = [char for char in str(computer_guessed_num)]
    for user in range(0, len(user_list)):
        if user_list[user] == computer_list[user]:
            cow += 1
        else:
            for com in range(0, len(user_list)):
                if user_list[user] == computer_list[com]:
                    bull += 1

    return "{} cow(s) and {} bull(s)".format(cow, bull)


class CowAndBullGame:

    def play(self):
        computer_guessed_num = random.randint(1000, 9999)
        while True:
            user_guessed_num = int(input("Enter your guess: "))
            if computer_guessed_num == user_guessed_num:
                print("User guessed right")
                break
            result_line = evaluate_user_entry(user_guessed_num, computer_guessed_num)
            print(result_line)


CowAndBullGame().play()
