"""Mathematical test for students by Popov Andrey"""

from math_tests import MathTestFactory


def tesing():
    """Testing function"""
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        print("4 - Insane")
        print("5 - Tournament")
        input_level = input("> ")
        try:
            test = MathTestFactory.create_test(int(input_level))
            break
        except ValueError:
            print("Wrong level. Try again.")
    try:
        test.start()
    except KeyboardInterrupt:
        print("\nthrowing the test blank sheet out of the window")


def main():
    """Main function"""
    try:
        while True:
            tesing()
            print("Do you want to try again? (y/n)")
            input_try_again = input("> ")
            if input_try_again != "y":
                break
    except KeyboardInterrupt:
        print("\nthrowing the teacher out of the window")
    print("Goodbye!")


if __name__ == "__main__":
    main()
