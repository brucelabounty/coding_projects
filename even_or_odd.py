def even_or_odd():
    # Program: Even or Odd 
    # Recieves number input from user and determines whether the number is even or odd.
    # Author: Bruce LaBounty
    # Date: 1/20/2025

    num = int(input("Please enter a number: "))

    if(num % 2 == 0):
        print("Your number is even.")
    else:
        print("Your number is odd.")

even_or_odd()