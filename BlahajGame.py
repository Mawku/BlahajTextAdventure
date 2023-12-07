import time

def intro():
    print("Welcome to the Blahaj Adventure Game!")
    time.sleep(1)
    print("You are Blahaj, the adventurous IKEA shark.")
    time.sleep(1)
    print("Your mission is to navigate through different scenarios and make decisions.")
    time.sleep(1)
    print("Let the adventure begin!\n")

def choose_scenario():
    print("Choose a scenario:")
    print("1. Deep-sea exploration")
    print("2. Beach vacation")
    print("3. Space voyage")

    choice = input("Enter the number of your choice: ")
    return choice

def deep_sea_exploration():
    print("\nYou embark on a deep-sea exploration adventure.")
    time.sleep(1)
    print("As you dive deeper, you encounter a school of colorful fish.")
    time.sleep(1)
    print("Do you:")
    print("1. Join the fish in their dance party")
    print("2. Continue exploring the mysterious depths")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("\nThe fish appreciate your dance moves!")
        print("You gained the title 'Blahaj, the Dance King of the Deep'.")
    else:
        print("\nYou discover an ancient underwater city.")
        print("The residents welcome you and share their knowledge.")
        print("You gained wisdom and earned the 'Deep-sea Explorer' badge.")

def beach_vacation():
    print("\nYou decide to take a relaxing beach vacation.")
    time.sleep(1)
    print("While sunbathing, you notice a sandcastle-building competition.")
    time.sleep(1)
    print("Do you:")
    print("1. Join the competition and build a majestic sandcastle")
    print("2. Take a nap under the beach umbrella")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("\nYour sandcastle is a masterpiece!")
        print("You won the competition and received the 'Sandcastle King' crown.")
    else:
        print("\nWhile napping, you dream of underwater castles and mermaids.")
        print("You wake up feeling refreshed and earned the 'Relaxation Guru' title.")

def space_voyage():
    print("\nYou embark on a space voyage to explore the cosmos.")
    time.sleep(1)
    print("During your journey, you encounter a group of friendly aliens.")
    time.sleep(1)
    print("Do you:")
    print("1. Communicate with the aliens using your dance moves")
    print("2. Exchange gifts and learn about their culture")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("\nThe aliens appreciate your intergalactic dance-off!")
        print("You became the honorary 'Blahaj, the Intergalactic Dance Ambassador'.")
    else:
        print("\nYou exchange gifts and form a lasting friendship with the aliens.")
        print("They teach you the secrets of space travel.")
        print("You gained the 'Space Voyager' badge.")

def main():
    intro()

    scenario_choice = choose_scenario()

    if scenario_choice == "1":
        deep_sea_exploration()
    elif scenario_choice == "2":
        beach_vacation()
    elif scenario_choice == "3":
        space_voyage()
    else:
        print("Invalid choice. The adventure ends.")

if __name__ == "__main__":
    main()
