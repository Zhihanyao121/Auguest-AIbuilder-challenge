from analyzer import analyze_telemetry
from telemetry import collect_telemetry
from ai_assistant import generate_ai_report

def generate_report(status, issues):
    print("\n========== SpaceGuard AI Mission Report ==========")

    print("\nMission Status:")
    print(status)
    print("\nDetected Issues:")

    if len(issues) == 0:
        print("No abnormal conditions detected")
    else:
        for index, issue in enumerate(issues, start = 1):
            print(str(index)+ ".", issue)

    print("\nRecommended Actions:")

    if status == "SAFE":
        print("- Continue normal operation")

    elif status == "WARNING":
        print("- Monitor system conditions carefully")
        print("- Prepare backup procedures")

    else:
        print("- Activate emergency procedures")
        print("- Reduce unnecessary power consumption")

def main():
    telemetry = collect_telemetry()
    print("Welcome to SpaceGuard AI")
    print("Spacecraft Monitoring System Starting...")

    print("\nCurrent Spacecraft Telemetry:")
    print("Temperature: ",telemetry["temperature"])
    print("Battery: ", telemetry["battery"])
    print("Oxygen: ", telemetry["oxygen"])
    print("radiation: " , telemetry["radiation"])
    print("fuel: ", telemetry["fuel"])

    issues = analyze_telemetry(telemetry)
    print("System analysis")
    
    if len(issues) == 0:
        status = "SAFE"
    elif len(issues) <= 2: 
        status = "WARNING"
    else:
        status = "CRITIAL"
    print("Status: ", status)
    
    for i in issues:
        print(i)

    generate_report(status, issues)
    ai_prompt = generate_ai_report(
        telemetry,
        status,
        issues
    )

    print("\n AI Prompt: ")
    print(ai_prompt)
 
def restart():
    while True:

        system_again = input("Do you need check this system again?(yes/no)").lower()

        if system_again == 'yes':
            return True
        elif system_again == 'no':
            return False
        else:
            print("please enter yes or no")
while True:
    main()
    if restart() == False:
        print("Ended")
        break