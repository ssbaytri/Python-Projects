from cryptography.fernet import Fernet


'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_key = load_key()
fer = Fernet(master_key)


def add():
    name = input("UserName: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as file:
        file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User: " + user, ", Password: " + fer.decrypt(password.encode()).decode())


while True:
    mode = input("Do you wanna add new pwd or view passwords? (add, view), q to quit: ").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode!")
