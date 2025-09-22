import random

def main():
    r = random.randint(1, 10)

    print("STOP! You who would get fortune free, \n"
          "must answer me these questions three, \n"
          "ere the other side I see.\n")
    input("press Enter to continue\n")

    name = input("What is your name? ").strip()

    quest = input("What is your quest? ").strip().lower()

    color = input("What is your favorite color? ").strip().lower()

    # Adjust r based on user input
    # Adjust r up or down depending on if they put any names from movie (example: "arthur")
    if any(movie_name in name.lower() for movie_name in ["arthur", "lancelot", "galahad", "robin"]):
        r += 2
    else:
        r -= 1

    # Adjust r up if they mention holy grail in quest, down if no input or no mention
    if "holy grail" in quest:
        r += 3
    elif not quest:
        r -= 2

    # Adjust r up if blue, down if yellow
    if color == "blue":
        r += 2
    elif color == "yellow":
        r -= 2

    print(r)  # for testing purpose. will remove in final phase

    if r <= 0:
        print(f"Bad luck {name}\n Your dead, You might feel happy, but your just DEAD,\n Now get on the cart.")
    elif 0 < r <= 3:
        print("Ill luck.\n  Stay clear of Villagers,\n or risk being accused of witchcraft.")
    elif 3 < r <= 6:
        print("Mixed blessings.\n A vicious man eating Rabbit will block your path.\n  But you have a Holy Hand Grenade.")
    elif 6 < r <= 10:
        print("Good luck.\n You will soon meet Tim the Enchanter.")
    else:  # r > 10
        print("The best of luck, You have found the Holy Grail. \n You will be remembered and quoted for ages to come.")

if __name__ == "__main__":
    main()