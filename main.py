""" Simple calculator by Kacper Wawrzonkiewicz"""
import os


class Calculator:
    def __init__(self):
        self.running = True
        self.operating = False
        self.valid_characters = ["+", "-", "*", "/", "**"]
        self.history = []


    def draw_menu(self):
        print("*-------------------- Simple Calculator Menu --------------------*")
        print("Choose one of the commands below:")
        print("  (1) Enter an operation")
        print("  (2) Show the operations history")
        print("  (3) Show the calculator commands")
        print("  Type 'exit' in order to leave the calculator")


    def get_user_input(self):
        user_input = str(input("> "))
        return user_input
    

    def show_operations_menu(self):
        self.clear_console()
        print("*--------------------- Calculator Operation ---------------------*")
        print("Enter an operation below, or type 'back' to return to the menu")


    def validate_operation(self, operation):
        for character in operation.split():
            try:
                character = float(character)
            except ValueError:
                if not character in self.valid_characters:
                    self.draw_error(f"Invalid operation! '{character}' is not recognized.")
                    return False
        return True
    

    def operate(self, operation):
        def add(x, y):
            return x + y

        def subtract(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def divide(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                self.draw_error("Invalid operation! You cannot divide by zero.")

        def power(x, y):
            return x ** y
        
        tokens = operation.split()
        if len(tokens) < 3:
            self.draw_error("Invalid operation! You must enter at least 3 tokens.")
            return
        index = 1

        try:
            result = float(tokens[0])
        except ValueError:
            self.draw_error("Invalid operation! Operation must begin with a number.")
            return

        while index < len(tokens) - 1:
            operator = tokens[index]
            try:
                number = float(tokens[index + 1])
            except ValueError:
                self.draw_error("Invalid operation! Operation must begin with a number.")
                return
        
            if operator == "+":
                result = add(result, number)
            elif operator == "-":
                result = subtract(result, number)
            elif operator == "*":
                result = multiply(result, number)
            elif operator == "/":
                result = divide(result, number)        
            elif operator == "**":
                result = power(result, number)

            index += 2

        self.add_operation_to_history(operation, result)
        if result == int(result):
            return int(result)
        return result
    

    def add_operation_to_history(self, operation, result):
        string = f"{operation} = {result}"
        self.history.append(string)

    
    def show_operations_history(self):
        self.clear_console()
        print("*---------------------- Operations History ----------------------*")

        if self.history:
            for string in reversed(self.history):
                print(f"> {string}")
        else:
            print("> No history.")

        print()
        print("Type anything in order to return to the menu")


    def show_calculator_commands(self):
        self.clear_console()
        print("*--------------------- Calculator Commands ----------------------*")
        print("  '+' Adds numbers together, e.g., x + y")
        print("  '-' Subtracts numbers, e.g., x - y")
        print("  '*' Multiplies numbers, e.g., x * y")
        print("  '/' Divides numbers (float result), e.g., x / y")
        print("  '**' Raises a number to a power, e.g., x ** y")
        print()
        print("Type anything in order to return to the menu")

    
    def leave_calculator(self):
        self.clear_console()
        self.running = False
        quit(0)


    def draw_error(self, error_message):
        self.clear_console()
        print("*---------------------------- Error -----------------------------*")
        print(f"> {error_message}")
        print()


    def clear_console(self):
        os.system('cls')


    def run(self):
        self.clear_console()
        while self.running:
            self.draw_menu()
            user_input = self.get_user_input()

            if user_input == "1":
                self.operating = True
                while self.operating:
                    self.show_operations_menu()
                    user_input = self.get_user_input()

                    if user_input == "back":
                        self.operating = False
                        self.clear_console()
                        continue
                    else:
                        valid = self.validate_operation(user_input)
                        if valid:
                            result = self.operate(user_input)
                            print(f"Result of the operation is: {result}")
                            print()
                            self.operating = False
                        else:
                            self.operating = False

            elif user_input == "2":
                self.show_operations_history()
                user_input = self.get_user_input()
                self.clear_console()
                if user_input:
                    continue

            elif user_input == "3":
                self.show_calculator_commands()
                user_input = self.get_user_input()
                self.clear_console()
                if user_input:
                    continue

            elif user_input == "exit":
                self.leave_calculator()

            else:
                self.draw_error("Invalid input! Please try again.")


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
