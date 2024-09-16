try:
    # Code that may fail or raise an exception.
    age = int(input("Please type your Age "))
    if age <= 0:
        raise ValueError("Age MUST be more than ZERO")
    print(f"Your age is {age}")
except ValueError as e:
    # Code to handle the exception error
    print(f"Error {e:}. Please enter a valid number.")