import random


# ---------------- SIMPLE REFLEX AGENT ----------------

def simple_reflex_agent(rooms, location):

    print("\n--- Simple Reflex Agent ---")

    max_steps = 10
    steps = 0

    while steps < max_steps:

        steps += 1

        print("\nStep", steps)
        print("Vacuum is in Room", location)

        # Check the current room
        if rooms[location] == "Dirty":

            print("Room", location, "is Dirty")
            print("Action: SUCK")

            rooms[location] = "Clean"

        else:

            print("Room", location, "is Clean")

            # Reflex rule: move to the other room
            if location == "A":
                print("Action: MOVE RIGHT")
                location = "B"
            else:
                print("Action: MOVE LEFT")
                location = "A"

    print("\nSimple Reflex Agent stopped.")
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])


# ---------------- GOAL-BASED AGENT ----------------

def goal_based_agent(rooms, location):

    print("\n--- Goal Based Agent ---")

    # Goal: both rooms should be clean
    goal = {
        "A": "Clean",
        "B": "Clean"
    }

    max_steps = 10
    steps = 0

    while rooms != goal and steps < max_steps:

        steps += 1

        print("\nStep", steps)
        print("Vacuum is in Room", location)

        # If current room is dirty, clean it
        if rooms[location] == "Dirty":

            print("Room", location, "is Dirty")
            print("Action: SUCK")

            rooms[location] = "Clean"

        else:

            print("Room", location, "is Clean")

            # Look at the other room because of the goal
            if location == "A" and rooms["B"] == "Dirty":

                print("Room B is Dirty")
                print("Action: MOVE RIGHT")

                location = "B"

            elif location == "B" and rooms["A"] == "Dirty":

                print("Room A is Dirty")
                print("Action: MOVE LEFT")

                location = "A"

    if rooms == goal:
        print("\nGoal Achieved!")

    else:
        print("\nGoal not achieved within the step limit.")

    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])


# ---------------- MAIN PROGRAM ----------------

print("===== VACUUM CLEANER AGENT =====")

# Get initial room status
while True:
    status_A = input("Enter status of Room A (clean/dirty): ").lower()

    if status_A == "clean" or status_A == "dirty":
        break

    print("Please enter only clean or dirty.")

while True:
    status_B = input("Enter status of Room B (clean/dirty): ").lower()

    if status_B == "clean" or status_B == "dirty":
        break

    print("Please enter only clean or dirty.")


# Convert to required format
status_A = status_A.capitalize()
status_B = status_B.capitalize()


# Create rooms
rooms = {
    "A": status_A,
    "B": status_B
}


# Random initial location
location = random.choice(["A", "B"])


print("\nInitial State:")
print("Room A:", rooms["A"])
print("Room B:", rooms["B"])
print("Vacuum starts in Room", location)


# Run Simple Reflex Agent
simple_reflex_agent(rooms.copy(), location)


# Run Goal Based Agent
goal_based_agent(rooms.copy(), location)