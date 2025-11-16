
master_pwd = input("What is the master password? ")

# Function to view saved passwords
def view():
    print("\n--- Saved Passwords ---")
    try:
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                name, pwd = data.split("|")
                print("Account:", name, "| Password:", pwd)
    except FileNotFoundError:
        print("No passwords saved yet.")

# Function to add a new password
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # Save as: name|password (one line per entry)
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")
    print("Password saved!\n")


while True:
    mode = input("Would you like to add or view passwords (add/view), or press q to quit? ").lower()

    if mode == "q":
        print("Goodbye!")
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid option. Please type 'add', 'view', or 'q'.\n")