def encode(number_string):
    password_out = ""
    for char in number_string:
        if int(char) < 7:
            password_out = password_out + str((int(char) + 3))
        else:
            password_out = password_out + str(int(char) - 7) # create a way to handle cases where the number wraps around
    return password_out

def decode():
    pass

def main():
    menu_continue = True
    while menu_continue:
      print("-------------\n1. Encode\n2. Decode\n3. Quit\n")
      choice = input("Please enter an option: ")
      if choice == "1":
          password = str(input("Please enter your password to encode:")) # take input from the user
          encoded_password = encode(password)
      elif choice == "2":
          pass # decoder goes here
      elif choice == "3":
          menu_continue = False
      else:
          print("Invalid input!")

if __name__ == '__main__':
    main()

