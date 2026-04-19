print("Imported sales.py", __name__)


def calculate_tax():
    pass


tax_rate = 0.16

# If we run this code, as it is a package the __name__ variable will be __main__.
# you can run this code as a Script

if __name__ == "__main__":
    print("Sales module")
    print(calculate_tax())
    print(tax_rate)
    print("End of sales module")

# So if we run this code as a script, the __name__ variable will be __main__.
# But if we import this module, the __name__ variable will be sales and the code inside the if statement will not run.
# Scripts let us run code directly.
