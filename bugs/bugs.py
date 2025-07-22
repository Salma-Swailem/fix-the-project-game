# Broken Login "Shafiq"
def login(user, password):
    if user == "admin" and password == "1234":
        print("Login successful")
        return True
    else:
        print("Login failed")
        return False

if __name__ == "__main__":
    user = input("Enter username: ")
    password = input("Enter password: ")
    login(user, password)




# Bubby_counter "Dalia"

def count_to_five():
    count = 0
    for i in range(5):
        count = count + 2
    print("Final count is:", count)
count_to_five()
