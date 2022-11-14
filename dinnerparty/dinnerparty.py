"""Dinner party by Popov Andrey"""
import random


def print_dict(friends: dict):
    """Print dictionary of friends"""
    print("="*30)
    for key, value in friends.items():
        print(f"'{key}' has to pay: {value} UAH;")
    print("="*30)


def main():
    """App entry point"""
    friends = {}

    print("Enter the number of friends joining (including you):")
    friends_count = int(input("> "))

    if friends_count <= 0:
        print("No one is joining for the party")
        return

    print("Enter the name of every friend (including you), each on a new line:")

    for _ in range(friends_count):
        friend_name = input("> ")
        friends[friend_name] = 0

    print("Enter the total amount:")
    total_amount = int(input("> "))

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")

    lucky_feature = input("> ").lower() == "yes"
    lucky_person = None

    if lucky_feature:
        lucky_person = random.choice(list(friends.keys()))
        print(f"{lucky_person} is the lucky one!")
        if friends_count == 1:
            print("No way, you are the only one here!")
            lucky_feature = False

    friends_count_to_pay = friends_count - int(lucky_feature)
    amount_to_pay = round(total_amount / friends_count_to_pay, 2)

    for key in friends:
        friends[key] = amount_to_pay if key != lucky_person else 0

    print_dict(friends)


if __name__ == '__main__':
    main()
