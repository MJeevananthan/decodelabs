# AI Recommendation System

print("=" * 50)
print("🎬 AI Recommendation System")
print("=" * 50)

while True:

    print("\nChoose a Category")
    print("1. Movies")
    print("2. Books")
    print("3. Courses")
    print("4. Music")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":

        genre = input("Enter Movie Genre (action/comedy/horror/romance): ").lower()

        if genre == "action":
            print("\nRecommended Movies:")
            print("- John Wick")
            print("- Avengers: Endgame")
            print("- Mission Impossible")

        elif genre == "comedy":
            print("\nRecommended Movies:")
            print("- 3 Idiots")
            print("- Jumanji")
            print("- Home Alone")

        elif genre == "horror":
            print("\nRecommended Movies:")
            print("- The Conjuring")
            print("- Annabelle")
            print("- IT")

        elif genre == "romance":
            print("\nRecommended Movies:")
            print("- Titanic")
            print("- The Notebook")
            print("- Me Before You")

        else:
            print("Genre not found.")

    elif choice == "2":

        category = input("Enter Book Category (programming/self-help/story): ").lower()

        if category == "programming":
            print("\nRecommended Books:")
            print("- Python Crash Course")
            print("- Clean Code")
            print("- Automate the Boring Stuff")

        elif category == "self-help":
            print("\nRecommended Books:")
            print("- Atomic Habits")
            print("- Rich Dad Poor Dad")
            print("- Think and Grow Rich")

        elif category == "story":
            print("\nRecommended Books:")
            print("- Harry Potter")
            print("- The Alchemist")
            print("- Wings of Fire")

        else:
            print("Category not found.")

    elif choice == "3":

        interest = input("Enter Interest (AI/Web/Data Science/Cyber Security): ").lower()

        if interest == "ai":
            print("\nRecommended Courses:")
            print("- Machine Learning")
            print("- Deep Learning")
            print("- Generative AI")

        elif interest == "web":
            print("\nRecommended Courses:")
            print("- HTML & CSS")
            print("- JavaScript")
            print("- React")

        elif interest == "data science":
            print("\nRecommended Courses:")
            print("- Python")
            print("- Pandas")
            print("- Data Visualization")

        elif interest == "cyber security":
            print("\nRecommended Courses:")
            print("- Ethical Hacking")
            print("- Network Security")
            print("- Penetration Testing")

        else:
            print("Interest not found.")

    elif choice == "4":

        mood = input("Enter Mood (happy/sad/chill): ").lower()

        if mood == "happy":
            print("\nRecommended Songs:")
            print("- Happy")
            print("- Believer")
            print("- On Top of the World")

        elif mood == "sad":
            print("\nRecommended Songs:")
            print("- Let Her Go")
            print("- Someone Like You")
            print("- Fix You")

        elif mood == "chill":
            print("\nRecommended Songs:")
            print("- Perfect")
            print("- Until I Found You")
            print("- Night Changes")

        else:
            print("Mood not found.")

    elif choice == "5":
        print("\nThank you for using AI Recommendation System!")
        break

    else:
        print("Invalid Choice! Try Again.")