# Program: minutes_to_seconds.py


def validate_data(value):
    try:
        if not value:
            raise ValueError("Input cannot be empty.")
        if value.isalpha():
            raise ValueError("Input must be a number.")
        int_val = int(value)
        if int_val < 0:
            raise ValueError("Input must be a non-negative number.")
        return int_val
    except ValueError as e:
        print(f"Error: {e}")
        return None

def get_integer(prompt):
    while True:
        user_input = input( prompt)
        validated = validate_data(user_input)
        if validated is not None:
            return validated

def convert_to_seconds(minutes):
    return minutes * 60

def run_conversion_program():
    minutes = get_integer("Enter the time in minutes")
    seconds = convert_to_seconds(minutes)
    print(f"\n{minutes} minute(s) is equal to {seconds} second(s).")

if __name__ == "__main__":
    run_conversion_program()

