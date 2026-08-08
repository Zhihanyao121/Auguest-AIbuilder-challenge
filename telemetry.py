from validator import check_validate

def collect_telemetry():
    temperature = check_validate(
        "Enter temperature (-20 to 150 °C): ",-150,150)

    battery = check_validate(
        "Enter battery (0 to 100%): ",0,100)

    oxygen = check_validate(
        "Enter oxygen (0 to 100%): ",0,100)

    radiation = check_validate(
        "Enter radiation (0 to 100 mSv/h): ",0,100)

    fuel = check_validate(
        "Enter fuel (0 to 100%): ",0,100)

    telemetry = {
        "temperature": temperature,
        "battery": battery,
        "oxygen": oxygen,
        "radiation": radiation,
        "fuel": fuel,
    }

    return telemetry