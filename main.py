#TODO: Create a letter using starting_letter.txt

with open("Input/Names/invited_names.txt", "r") as inv:
    for name in inv.readlines():
        name = name.strip("\n")
        with open("Input/Letters/starting_letter.txt", "r") as letter:
            new_letter = letter.read()
            with open(f"Output/ReadyToSend/letter_for_{name}", "w") as rfs:
                rfs.write(new_letter.replace("[name]", f"{name}"))

