def analyze_telemetry(data):
    problems = []

    if data["temperature"] > 35:
        problems.append("temperature is too high")

    if data["battery"] < 20:
        problems.append("battery is too low")

    if data["oxygen"] < 90:
        problems.append("oxygen is dangerous")

    if data["radiation"] > 5:
        problems.append("radiation level is high")

    if data["fuel"] < 30:
        problems.append("fuel level is low")

    return problems
