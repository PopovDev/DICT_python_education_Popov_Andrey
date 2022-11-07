"""Matrinx processing by Popov Andrey"""
from calculator import Calculator

def main():
    """Main function"""
    calc = Calculator()
    try:
        print("Matrix calculator started")
        calc.caltulator_loop()
    except KeyboardInterrupt:
        print("\nCrossing out all matrices and throwing them away")
    finally:
        print("Exiting")


if __name__ == "__main__":
    main()
