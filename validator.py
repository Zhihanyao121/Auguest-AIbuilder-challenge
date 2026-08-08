
def check_validate(message,minimun,maximum):
    while True:
        try:
            value = float(input (message))
            if value > maximum or value < minimun:
                 print("Invalid, please enter the range between", min ,"and" ,max)
            else:
                 return value
        except ValueError:
            print("Invalid input. Please enter a number.")

    
        