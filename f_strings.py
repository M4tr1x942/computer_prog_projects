def main():
    if __name__ == "__main__":
        #Part 1
        username = input("What is your name: ")
        food = input("What is your favorite food: ")
        response1 = F"Hello, {username}, I hear your favorite food is {food}. That's pretty weird."
        print(response1)
        #Part 2
        num1 = input("enter a number: ")
        num2 = input("enter a second number: ")
        sum = F"{num1} + {num2} = {(int(num1) + int(num2))}"
        print(sum)
        dif = F"{num1} - {num2} = {(int(num1) - int(num2))}"
        print(dif)
        product = F"{num1} * {num2} = {(int(num1) * int(num2))}"
        print(product)
        #Part 3
        name = "grafton steele"
        a_name = name.title()
        print(F"{a_name}")
        name_upper = name.upper()
        print(F"{name_upper}")
        #Part 4
        decimal = 5.437284
        print(decimal)
        decimal_formatted = F"{(decimal):.2f}"
        print(decimal_formatted)
        #Part 5
        #The F tells Python to automatically format the following things
        # Math and formatting for things like decimal places
main()
