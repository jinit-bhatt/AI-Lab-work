def main():
    import bcrypt
    user_info = []

    def hashing(password):
        encode = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(encode, salt)
        print(hashed)
        return hashed

    def check_password(password, salt):
        return bcrypt.checkpw(password.encode('utf-8'), salt)

    def signup():
        import re
        while True:
            email = input("Enter your email:")
            pattern = r"^\w+@.*\..*$"
            if re.match(pattern, email):
                password = input("Enter your password:")
                hashed= hashing(password)
                user = {email: hashed}
                user_info.append(user)
                break
            else:
                print("enter the valid email")
        print(user_info)
        print("signup successful")

    def login():
        email = input("Enter your email:")
        if email in user_info:
            password = input("Enter your password: ")
            hashed = hashing(password)
            if user_info[email]==hashed:
                print("Login successful!")
            else:
                print("incorrect password")
                login()
        else:
            print("Email didn't found. Please try again.")
            login()

    def logout():
        print("Logout successful!")
        #return logout()
    logged_in = False

    def notes():
        print("1. create new note")
        print("2. open old")
        print("3. history")
        print("4. logout")
        choice1 = input("enter your choice:")
        f = open("file.txt", "w+" and "a")
        while input() != "end":
            if choice1 == "1":
                print(user_info)
                f.write(input("enter your note:"))
                if input() == "end":
                    f.close()
            elif choice1 == "2":
                print(user_info)
                f.write(input("enter your note:") + '\n')
                if input() == "end":
                    f.close()
            elif choice1 == "3":
                f.read()
            elif choice1 == "4":
                logout()
        f.close()

    while True:
        if not logged_in:
            print("1. Signup")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                signup()
            elif choice == "2":
                logged_in = login()
                notes()
            elif choice == "3":
                print("closing the site")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("1. Logout")
            print("2. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                logged_in = logout()
            elif choice == "2":
                print("closing the site")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
