def get_percentage(message):
    while True:
        try:
            number = float(input(message))
            if number > 100 or number < 0:
                print("Invaild range of number please make sure number beteen 0~100")
            else:
                return number
        except ValueError:
            print("Invaild input, please input a number")

def check_danger(temperature, battery, oxygen, radiation, fuel):
    dangerlist = []
    if temperature < 20 or temperature > 35:
        dangerlist.append("temperature danger")

    if battery < 20:
        dangerlist.append("battery danger")

    if oxygen < 90:
        dangerlist.append("oxygen danger")

    if radiation > 5:
        dangerlist.append("radiation danger")

    if fuel < 30:
        dangerlist.append("fuel danger")
    
    return dangerlist

def restart():
    while True:

        system_again = input("Do you need check this system again?(yes/no)").lower()

        if system_again == 'yes':
            return True
        elif system_again == 'no':
            return False
        else:
            print("please enter yes or no")

def main():
    test_number = 1
    while True:
        temperature = get_percentage("enter temperature: " )
        battery = get_percentage("enter battery: ")
        oxygen = get_percentage("enter oxygen: ")
        radiation = get_percentage("enter radiation: ")
        fuel = get_percentage("enter fuel: ")  
        
        result = check_danger(temperature, battery, oxygen, radiation, fuel)

        print("*************" + " Test" + str(test_number) + " ******************")
        print("--------- Spacecraft Status --------")   
        print("Temperature: " + str(temperature) + " C")
        print("Battery: " + str(battery) + " %")
        print("Oxygen: " + str(oxygen) + " %")
        print("radiation: " + str(radiation))
        print("fuel: " + str(fuel) + " %")

        if len(result) > 1:
            for danger in result:
                print(danger)
            print("spacecraft is danger and need to be fixed")
        elif len(result) == 0:
            for i in result:
                print(i)
            print("spacecraft is very safe")
        else:
            for i in result:
                print(i)
            print("spacecraft have warning")
        
        if restart() == False:
            print("Ended")
            break

        test_number += 1

main()



    