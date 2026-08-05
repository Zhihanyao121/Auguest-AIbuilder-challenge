def collect_telemetry():
    temperature = int(input("Enter temperature: "))
    battery = int(input("Enter a battery: "))
    oxygen = int(input("Enyer am oxygen: "))
    radiation = int(input("Enter a radiation: "))
    fuel = int(input("Enter a fuel: "))
    telemetry ={
        "temperature": temperature,
        "battery": battery,
        "oxygen": oxygen,
        "radiation": radiation,
        "fuel": fuel,
    }
    return telemetry