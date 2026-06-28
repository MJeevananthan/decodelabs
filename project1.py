import datetime
import random

print("=" * 50)
print("🤖 Welcome to Smart Rule-Based AI Chatbot")
print("Type 'help' to see available commands.")
print("Type 'exit' to quit.")
print("=" * 50)

jokes = [
    "Why did the computer sleep? Because it had too many tabs open!",
    "Python programmers don't like bugs... they prefer exceptions!",
    "AI doesn't replace humans, it helps them!",
    "Why was the robot happy? It got a software update!"
]

quotes = [
    "Success comes from continuous learning.",
    "Practice makes perfect.",
    "Never stop exploring technology.",
    "Dream big and code bigger."
]

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user:
        print("Bot: I'm Smart AI Chatbot.")

    elif "who created you" in user:
        print("Bot: I was created using Python.")

    elif "bye" in user or user == "exit":
        print("Bot: Goodbye! Have a great day.")
        break

    elif user == "help":
        print("""
Available Commands:
- hello
- how are you
- your name
- who created you
- time
- date
- joke
- quote
- ai
- python
- machine learning
- internship
- course
- weather
- calculator
- thank you
- help
- exit
        """)

    elif "time" in user:
        now = datetime.datetime.now()
        print("Bot: Current Time:", now.strftime("%I:%M:%S %p"))

    elif "date" in user:
        today = datetime.date.today()
        print("Bot: Today's Date:", today)

    elif "joke" in user:
        print("Bot:", random.choice(jokes))

    elif "quote" in user:
        print("Bot:", random.choice(quotes))

    elif "thank" in user:
        print("Bot: You're welcome!")

    elif "ai" in user:
        print("Bot: Artificial Intelligence enables machines to perform human-like tasks.")

    elif "python" in user:
        print("Bot: Python is one of the most popular programming languages.")

    elif "machine learning" in user:
        print("Bot: Machine Learning allows computers to learn from data without explicit programming.")

    elif "internship" in user:
        print("Bot: Internships help you gain practical skills and industry experience.")

    elif "course" in user:
        print("Bot: Keep completing courses and building projects to strengthen your resume.")

    elif "weather" in user:
        print("Bot: Sorry! I can't access live weather without internet.")

    elif "calculator" in user:
        try:
            n1 = float(input("Enter first number: "))
            op = input("Operator (+,-,*,/): ")
            n2 = float(input("Enter second number: "))

            if op == "+":
                print("Result:", n1 + n2)
            elif op == "-":
                print("Result:", n1 - n2)
            elif op == "*":
                print("Result:", n1 * n2)
            elif op == "/":
                if n2 != 0:
                    print("Result:", n1 / n2)
                else:
                    print("Cannot divide by zero.")
            else:
                print("Invalid operator.")
        except:
            print("Invalid input.")

    else:
        print("Bot: Sorry, I didn't understand that. Type 'help' for commands.")