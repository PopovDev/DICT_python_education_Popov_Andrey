BOT_NAME = "SUPER-BOT"
BIRTH_YEAR = 2022


def main():
    print(f"Hello! My name is {BOT_NAME}.")
    print(f"I was created in {BIRTH_YEAR}.")
    print("Please, remind me your name.")

    name = input("> ")
    print(f"What a great name you have, {name}!")

    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    rem3 = int(input("> "))
    rem5 = int(input("> "))
    rem7 = int(input("> "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")

    print("Now I will prove to you that I can count to any number you want.")
    num = int(input("> "))
    for i in range(num + 1):
        print(f"{i} !")

    print("Let's test your programming knowledge.")
    print("What is an array?")
    print("1. Magic Data Storage for Programmers.")
    print("2. Boss from Genshin Impact")
    print("3. Collection of similar data elements stored at contiguous memory locations.")
    print("4. An unexplored area of ​​memory saturated with hopes for a better future.")

    while(True):
        ans = int(input("> "))
        if ans == 3:
            print("Completed, have a nice day!")           
            break
        print("Please, try again.")

    print("Congratulations, have a nice day!")



if __name__ == "__main__":
    main()
