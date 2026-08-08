# Auguest-AIbuilder-challenge
This is for AI builder Auguest challenge - Advance Space Exploration with AI
SpaceGuard AI

SpaceGuard AI is a command-line spacecraft monitoring prototype created for the **August AI Builders Challenge — Advance Space Exploration with AI**.

The program collects spacecraft telemetry from the user, checks the data against a set of safety thresholds, reports detected problems, and generates a prompt for an AI mission assistant.

## Project Purpose

Space missions produce important telemetry data that must be interpreted quickly. SpaceGuard AI demonstrates a simple way to convert several spacecraft measurements into a clear mission status and list of detected issues.

The current version monitors:

- Temperature
- Battery level
- Oxygen level
- Radiation level
- Fuel level

## Current Features

- Accepts spacecraft telemetry through the terminal.
- Accepts integer and decimal values.
- Rejects non-numeric input.
- Checks whether input values are inside their accepted ranges.
- Repeats the input request when data is invalid.
- Detects abnormal telemetry using fixed safety thresholds.
- Classifies the mission as safe, warning, or critical based on the number of issues.
- Prints a SpaceGuard mission report.
- Generates a structured prompt for an AI spacecraft mission assistant.
- Allows the user to check another set of telemetry values.

## How the Program Works

1. The user runs `main.py`.
2. `telemetry.py` asks the user to enter five telemetry values.
3. `validator.py` checks that each input is numeric and within its accepted range.
4. `analyzer.py` compares the telemetry with the current safety thresholds.
5. `main.py` determines the overall mission status from the number of detected issues.
6. The program prints the telemetry, mission status, issues, and recommended actions.
7. `ai_assistant.py` creates a prompt containing the mission information.
8. The user can choose whether to perform another system check.
