# Kaden Jones

def encode(number_string):
    password_out = ""
    for char in number_string:
        if int(char) < 7:
            password_out = password_out + str((int(char) + 3))
        else:
            password_out = password_out + str(int(char) - 7) # create a way to handle cases where the number wraps around
    return password_out

def decode(encoded):
    encoded = int(str(encoded).replace("0","a").replace("1","b").replace("2","c").replace("3","d").replace("4","e").replace("5","f").replace("6","g").replace("7","h").replace("8","i").replace("9","j").replace("a","7").replace("b","8").replace("c","9").replace("d","0").replace("e","1").replace("f","2").replace("g","3").replace("h","4").replace("i","5").replace("j","6"))
    return encoded

def main():
    menu_continue = True
    while menu_continue:
      print("-------------\n1. Encode\n2. Decode\n3. Quit\n")
      choice = input("Please enter an option: ")
      if choice == "1":
          password = str(input("Please enter your password to encode:")) # take input from the user
          encoded_password = encode(password)
      elif choice == "2":
          decoded = decode(encoded_password)
          print(f"The encoded password is {encoded_password}, and the original password is {decoded}.\n")
      elif choice == "3":
          menu_continue = False
      else:
          print("Invalid input!")

if __name__ == '__main__':
    main()

