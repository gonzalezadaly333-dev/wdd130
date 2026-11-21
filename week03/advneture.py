print ("The Mystery Forest")

print ("You are walking alone trhough a mysterious forest. Suddenly,you hear someone calling your name. You feel scared, but curious.")
print ("You see three things: An old wooden CABIN, a dark PATH and a strange glowing LIGHT between the trees")

choice = input("Where do you want to go? CABIN, PATH, or LIGHT?")


if choice == "cabin":
    print("You enter the old cabin. Everything is covered in dust.")
    print("Suddenly, you find an old diary on a table.")
    

    second_choice = input( "Do you want to READ the diary or LEAVE the cabin?")
    second_choice = second_choice.lower ()

    if second_choice == "read":
        print("You open the diary and discover a mysterious message.")

    elif second_choice =="leave":
        print("You leave the cabin and return to the forest.")
    else: print("Not valid.")




elif choice == "path":
    print("You go through a tunnel, and see nothing.")
    print("Suddenly you see a sign.")

    second_choice = input("Do you go through the TUNNEL or you follow the SIGN?")
    second_choice = second_choice.lower()

    if second_choice == "tunnel":
        print("You follow the tunnel and it leads you to a river.")

    elif second_choice == "sign":
     print("You follow the sign and it takes you to the same place you started.")
    else: print("Not valid.")


elif choice == "light":
    print("You run towards the light and see a man.")
    print("You go the opposite way and fall and can't see.")

    second_choice = input("Do you RUN towards the light or you GO the opposite way?")
    second_choice = second_choice.lower ()

    if second_choice == "run towards the light":
        print("You run towards the light and see a man")
        
    elif second_choice == "go the opposite way":
        print("You go opposite way, you fall and can't see.")
    else:
        print("Not valid.")





