PLACEHOLDER = "[name]"

with open("Mail Merge Project Start/Input/Names/invited_names.txt") as f:
    names = f.readlines()


with open("Mail Merge Project Start/Input/Letters/starting_letter.txt")as f:
    file = f.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = file.replace(PLACEHOLDER,stripped_name)
        with open(f"Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt","w") as completed_letter:
            completed_letter.write(new_letter)

    
       



   