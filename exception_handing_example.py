
class NegativeNumberError(Exception):
    pass

numbers = []


while True:

    try:

        user_input = input("Enter a Number (or 'done' to finish): ")

        if user_input.lower() == 'done':
            break 

        number = float(user_input)
        
        if number < 0:
            raise NegativeNumberError("Negative numbers are not allowed.",{number})
        
        numbers.append(number)

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except NegativeNumberError as e:
        print("Error:", e)


    if numbers:

        avg = sum(numbers) / len(numbers)

        positive_sum = sum(num for num in numbers if num > 0)

        print("Sum of positive numbers:", positive_sum)

        highest = max(numbers)
        print("Highest number:", highest)

        lowest = min(numbers)
        print("Lowest number:", lowest)

    else:
        print("No numbers were entered.")
