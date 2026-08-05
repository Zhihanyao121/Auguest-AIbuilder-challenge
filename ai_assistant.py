def generate_ai_report(telemetry, status, issues):
    issues_text = "\n".join(issues)
    prompt = f"""
You are a spacecraft mission assistant.

Your role is to help mission engineers make safe decisions during space missions.

Analyze the following spacecraft condition.

Telemetry data:
Temperature: {telemetry["temperature"]}
Battery: {telemetry["battery"]}
Oxygen: {telemetry["oxygen"]}
Radiation: {telemetry["radiation"]}
Fuel: {telemetry["fuel"]}

Mission Status:
{status}

Detected Issues:
{issues_text}

Please provide:
1. Explanation of the risks
2. Possible causes
3. Recommended actions
"""
    return prompt