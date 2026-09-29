def greet_user(name):
    return f"Hello, {name}! Welcome to Python."

user_name = input("Enter your name: ")
greeting = greet_user(user_name)
print(greeting)
