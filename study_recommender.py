print("===== Smart Study Recommendation System =====")

# User input
subject = input("Enter your weak subject: ").lower()
hours = int(input("How many hours do you study daily? "))
style = input("Preferred learning style (visual/practical/theory): ").lower()

print("\n----- AI Study Recommendation -----\n")

# Recommendation logic
if subject == "maths":
    print("• Practice problem-solving daily")
    print("• Focus on formulas and shortcuts")

elif subject == "programming":
    print("• Write code every day")
    print("• Practice mini projects")

elif subject == "cybersecurity":
    print("• Learn networking basics")
    print("• Practice using Linux commands")

else:
    print("• Revise concepts regularly")
    print("• Use active recall techniques")

# Study hours logic
if hours < 2:
    print("• Increase study time gradually")

else:
    print("• Maintain consistent study schedule")

# Learning style logic
if style == "visual":
    print("• Use diagrams and flowcharts")

elif style == "practical":
    print("• Learn through hands-on exercises")

elif style == "theory":
    print("• Read detailed notes and documentation")

print("\nAI-generated study plan completed!")