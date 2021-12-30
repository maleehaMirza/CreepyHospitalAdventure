# Name: Maleeha Mirza
# Date: March 25, 2021
# Name of program: CreepyHospitalAdventure
# Purpose of program: To engage the user into a text-based story adventure where they can choose from the options of rooms and tasks to do inside those rooms, and based on their choices, they can either have a sad or fun ending. 

# To win the game, here are the following methods: 
# Enter the storage room -> Shelf rack -> Take a peek at the wall holes -> Look inside triangle hole.
# Enter the storage room -> Cabinet -> Dark and clean tunnel
# Enter the emergency room -> Bandages -> Yes I should trust the zombie.
# Enter the emergency room -> Medical cutting tools -> Hospital bed.
# Enter the pharmacy -> Baby -> Skateboard
# Enter the pharmacy -> Puppy -> Injection gun and stab the zombie.

# Introduces and explains the program to the user.
def introduce_program():
  print(" Welcome to the escape room program! ".center(45, "~"))
  print("")
  print("This program guides you through a text-based story adventure. This adventure involves running away from scary zombies at the hospital by traveling through rooms to figure out ways to exit. Remember: each choice can either determine your freedom or your doom. Choose wisely!")
  print("")
  print("Let the adventure begin!")
  print("")

# Outputs the waiting room portion (first part) of the story. Depending on if the user entered the waiting room the first or second time, it outputs 2 different story plot advancements. 
def waiting_room(numTimesEnterRoom):
  print("")
  if numTimesEnterRoom == 1:
    print("You wake up in the waiting room at the hospital with no memory of who you are and how you got there. All of a sudden, you see the television news and discover that there is a zombie apocalypse in the same hospital. There is no one around you, and you have to escape out of that hospital. You see that there are 3 doors in front of you that lead to the:")
    room_choices(1)
  elif numTimesEnterRoom ==2: 
    print("You are now in the waiting room. You have lost access to the pharmacy as the zombies have taken over it and is heading to the waiting room right now! You must immediately get out of there!")
    room_choices(2)

# Outputs room choices based on the number of times the user had entered the waiting room. If they entered the room for the first time, they are allowed to choose from 3 room options, and if they enter the room 2 or more times, they only have 2 room options. 
def room_choices(enterTimes): 
    answer = ""
    print("")
    print("1. Storage room")
    print("")
    print("2. Emergency room")
    if enterTimes == 1:
      print("")
      print("3. Pharmacy")
      print("")
      while not (answer == "1" or answer == "2" or answer == "3"):
        print("")
        answer = input("Which place/room would you like to enter? Enter the number of your room choice: ")
      if answer == "1":
        calculate_rooms()
        storage_room()
      elif answer == "2":
        calculate_rooms()
        emergency_room()
      else: 
        calculate_rooms()
        pharmacy_room()
    elif enterTimes == 2: 
      while not (answer == "1" or answer == "2"):
        print("")
        answer = input("Which room would you like to enter? Enter the number of your room choice: ")
      if answer == "1":
        calculate_rooms()
        storage_room()
      else:
        calculate_rooms()
        emergency_room()

# Lets the user enter the storage room and outputs all the storage room choices to the user.
def storage_room():
  print("")
  print("You are now in the storage room. You have the choice of moving the shelf rack that is against the wall or opening a cabinet.")
  print("")
  print("1. Shelf rack")
  print("")
  print("2. Cabinet")
  print("")
  answer = ""
  # Asks the user which object they would like to move and based on their choices, they are landed in different scenarios. 
  while not(answer == "1" or answer == "2"):
    answer = input("Which object would you like to move? Enter 1 for shelf rack or 2 for cabinet: ")
    print("")
  if answer == "1": 
    calculate_tasks()
    print("You moved the shelf rack, and you see 2 small holes in the wall. You can either choose to see inside these holes or go back to the waiting room.")
    print("")
    print("1. Take a peek inside the wall holes")
    print("")
    print("2. Go to the waiting room")
    print("")
    answer = ""
    while not(answer == "1" or answer =="2"):
      answer = input("Which option do you want to choose? Enter 1 for the holes or 2 for going to the waiting room. ")
      print("")
    if answer == "1":
      calculate_tasks()
      print("1. Look in the circle hole")
      print("")
      print("2. Look in the triangle hole")
      print("")
      answer = ""
      while not(answer== "1" or answer == "2"):
        answer = input("Which hole would you like to peek in? Answer 1 for circle hole or 2 for triangle hole: ")
        print("")
      if answer == "1": 
        calculate_tasks()
        print("You look inside the circle hole and find that a shape-shifting zombie was hiding in there waiting for its prey. It pokes you in the eye, breaks the wall, and eats you for its dinner.")
        lose_game()
      else: 
        calculate_tasks()
        print("You look inside the triangle hole and find that the parking lot is right outside. You break the wall, and you quickly run for your life. You are now free and alive while eating a Happy Meal and enjoying the rain outside.")
        win_game()
    else: 
      calculate_rooms()
      waiting_room(2)
  else: 
    calculate_tasks()
    print("You open the cabinet and find 2 secret tunnels. You are confused about which tunnel to take. Alas, you have to quickly choose which tunnel to go through as you hear the zombies breaking the storage room door. 1 tunnel is dark and clean, while the other is very bright but dirty.")
    print("")
    print("1. Dark and clean tunnel")
    print("")
    print("2. Bright and dirty tunnel")
    print("")
    answer = ""
    while not(answer == "1" or answer == "2"):
      answer= input("Which tunnel would you like to take? Enter 1 for dark and clean tunnel or 2 for bright and dirty tunnel: ")
      print("")
    if answer == "1": 
      calculate_tasks()
      print("You travel through the dark and clean tunnel. Eventually, the tunnel led to a slide in the McDonalds playpark. All the adults stare at you and are confused as to where you came from. You don't care about what these adults think since you realize that you are finally safe and free from that scary hospital!")
      win_game()
    else: 
      calculate_tasks()
      print("You travel through the tunnel that is very dirty but has bright lighting. However, this bright lighting has attracted many zombie mosquitos, and you get many mosquito bites. Unfortunately, these bites have turned you into a zombie, and you wander around the hospital with your zombie friends.")
      lose_game()

# Lets the user enter the emergency room and outputs all the various choices of the emergency room portion of the story adventure.
def emergency_room():
  print("")
  print("You are now in the emergency room. You find an unconscious zombie lying on the floor. You quickly get scared and try to avoid it. Suddenly, the zombie opens their eyes, but they seem to not able to get up. They instantly see you and point towards a cupboard. You proceed towards the cupboard and see bandages and medical cutting tools.")
  print("")
  print("1. Bandages")
  print("")
  print("2. Medical cutting tools")
  print("")
  answer = ""
  while not (answer == "1" or answer == "2"):
    answer = input("From the above options, which object will you reach for? Answer 1 for bandages or medical cutting tools: ")
    print("")
  # Outputs 4 choices to the user where each choice results in a different story plot advancement. 
  if answer == "1": 
    calculate_tasks()
    print("You take the bandages and give them to the zombie. The zombie starts to heal and offers you a secret way out of the hospital. Do you think you can trust them and escape with them? At the same time, the tooth fairy suddenly appears out of nowhere and also offers you only 1 chance of safely teleporting to the pharmacy and storage room.")
    print("")
    print("1. Yes I should trust the zombie.")
    print("")
    print("2. No I should not trust the zombie.")
    print("")
    print("3. Let's go to the pharmacy.")
    print("")
    print("4. Let's go to the storage room.")
    print("")
    answer = ""
    while not(answer == "1" or answer == "2" or answer == "3" or answer =="4"): 
      answer = input("From the above options, enter the number of the option that you would like to choose: ")
      print("")
    if answer == "1": 
      calculate_tasks()
      print("The zombie holds your hand and leads you through several rooms in the hospital with secret passages. You start to get suspicious if the zombie is playing you, and as soon as you try to run away, the last door the zombie opens leads to your parents at the back of the hospital. You feel so relieved, and the zombie thanks you for your kindness.")
      win_game()
    elif answer == "2":
      calculate_tasks()
      print("You don't trust the zombie at all and runs away to a staircase. You feel so happy and relieved that you did not stay with the zombie for even a second longer. You then start looking for another way out. To your surprise, the zombie that you left came back to haunt you for not helping them. Before you could try to reason with the zombie, it instantly eats you for its snack.")
      lose_game()
    elif answer == "3": 
      calculate_rooms()
      pharmacy_room()
    else: 
      calculate_rooms()
      storage_room()
  else: 
    calculate_tasks()
    print("")
    print("You get the medical cutting tools and start threatening the zombie to leave you alone. The zombie is not happy about this and calls their zombie friends with a scary growl. You are panicking as to how you will escape or defend yourself. As you look around the room, you see a defibrillator (an electric shocker) and a hospital bed with wheels.")
    print("")
    print("1. Defibrillator")
    print("")
    print("2. Hospital bed")
    print("")
    answer = ""
    while not(answer == "1" or answer == "2"): 
      answer = input("Which object will you use? Enter 1 for defibrillator or 2 for hospital bed: ")
      print("")
    if answer == "1": 
      calculate_tasks()
      print("You use the defibrillator to shock all the zombies around you. They all become electrocuted and melt on the ground. After a lot of zombies electrocuted, you then open the exit door in the room. You feel a ray of sunlight shining on your face, and you feel so relieved. Your heart then becomes filled with darkness as a zombie struck you from behind and eats you...")
      lose_game()
    else: 
      calculate_tasks()
      print("At full speed, you drag the hospital bed across the hospital floor. Immediately, you hop onto the bed as if it was a moving horse and speed through the hospital, hitting any zombies in its way. Although with many minor injuries and hundreds of zombies chasing after you, you successfully escaped out of the hospital in a hospital bed! It looks like hospital beds aren't the worse after all!")
      win_game()
  
# Lets the user enter into the pharmacy room and outputs several options that the user can choose from while in the pharmacy area. 
def pharmacy_room(): 
  print("")
  print("You are now in the pharmacy room. You find a lot of medicines lying on the floor and glass on the floor. You find a baby crying and a hurt puppy on different sides of the room. However, you are hesitant to go near any of them as you saw on the news that the zombies are shapeshifters. Due to your sympathy, you want to help one of them but who? ")
  print("")
  print("1. Baby")
  print("")
  print("2. Puppy")
  print("")
  answer = ""
  # Asks the user which option they would like to take, and each option includes a different way of how the adventure goes forward. 
  while not (answer == "1" or answer == "2"):
    print("")
    answer = input("From the above options, who you would like to help? Enter 1 for the baby or 2 for the puppy: ")
    print("")
  if answer == "1": 
    calculate_tasks()
    print("You take the baby, and you start rocking it in your arms. Eventually, the baby stops crying, and you start noticing that your arms and hands are very gooey. You look at the baby with sudden fear, and the baby replies with a creepy smile. You quickly drop the baby and come across 2 gadgets:  ")
    print("")
    print("1. Skateboard")
    print("")
    print("2. Hoverboard")
    print("")
    answer = ""
    while not(answer == "1" or answer == "2"): 
      answer = input("Which gadget would you like to use to escape? Answer 1 for skateboard or 2 for hoverboard: ")
      print("")
    if answer == "1": 
      calculate_tasks()
      print("You travel across the hospital hallway with the skateboard, and it turns out that you are a skateboard expert. Despite the zombies chasing you, you are having fun on a skateboard. On purpose, you break a door with the skateboard and crash into a garbage can. You get up and find the army escorting you to a safe area. You run from the hospital and go to a nearby Tim Hortons to get some donuts. Victory sure does taste sweet!")
      win_game()
    else: 
      calculate_tasks()
      print("You take the hoverboard and speed through the hospital like lightning. You find yourself about to bust your way out the door when your hoverboard runs out of battery and stops. You fall straight on your face like a pancake, and when you turn around, you find out that you are now a yummy pancake to the zombies.")
      lose_game()
  else: 
    # Outputs other courses of action if the user chose the second option in the first question of being asked if they would want to help the baby or puppy. 
    calculate_tasks()
    print("")
    print("Despite hearing the loud cries of the baby, you help the puppy and bandages its wounds. You then feel guilty about leaving the baby to cry and slowly start to approach it. You realize that there is nasty green slime around the baby, and in a heartbeat, the baby transforms into a freaky zombie. You have 2 options:")
    print("")
    print("1. Take the injection gun nearby and stab the zombie.")
    print("")
    print("2. Grab the puppy and run for your life.")
    print("")
    answer = ""
    while not(answer == "1" or answer == "2"): 
      answer = input("Which option will you choose? Answer 1 for the first option or 2 for the second option: ")
      print("")
    if answer == "1": 
      calculate_tasks()
      print("You stab the injection gun on the zombie's leg, and the zombie instantly melts to the ground. You realize that these injection guns can destroy the entire zombie army. You take the puppy with you and inject all the zombies standing in your way. You become a great hero and get offered the position of a police officer. As a new officer, you ensure that this type of situation never happens again!")
      win_game()
    else: 
      calculate_tasks()
      print("You grab the puppy and run as fast as a cheetah. Suddenly, you bumped into the mafia boss, the leader of the zombie army. He yells at you and questions why you took his puppy. Before he gave you a chance to explain, he eats your head off. You are now known as the infamous 'headless zombie.'")
      lose_game()

# Calculates the number of tasks that the user performs by adding 1 each time they choose to perform an action. 
numTasks = 0
def calculate_tasks(): 
  global numTasks
  numTasks = int(numTasks) +  1

# Calculates the number of rooms the user entered in the game by adding 1 each time they choose to go to a different room. 
numRooms = 0
def calculate_rooms():
  global numRooms
  numRooms = int(numRooms) + 1

# Outputs a message to the user informing them that they have won the game. Depending on the number of rooms the user entered or tasks they did, the sentence changes to ensure no grammar mistakes.
def win_message(completeSentence): 
  print("Congratulations, you win the game! You completed " + str(numTasks) + completeSentence + " Try this game again to find out other ways to win!") 

def win_game(): 
  print("")
  print("")
  print(" GAME OVER ".center(67, "~"))
  if numRooms>1 and numTasks>1:
    win_message(" tasks and entered " + str(numRooms) + " rooms!")
  elif numRooms>1 and numTasks == 1: 
    win_message(" task and entered " + str(numRooms) + " rooms!")
  elif numRooms ==1 and numTasks>1:
    win_message(" tasks and entered only " + str(numRooms) + " room!")
  elif numRooms == 1 and numTasks ==1:
    win_message(" task and entered only " + str(numRooms) + " room!")
  repeatGame()

# Outputs a message to the user informing them that they have lost the game. Depending on the number of rooms the user entered or tasks they did, the sentence changes to ensure no grammar mistakes.
def lose_message(completeSentence): 
  print("You lose! You completed " + str(numTasks) + completeSentence + " Try this game again to find out other ways to win!") 

def lose_game():
  print("")
  print(" GAME OVER ".center(58, "~"))
  if numRooms>1 and numTasks>1:
    lose_message(" tasks and entered " + str(numRooms) + " rooms!")
  elif numRooms>1 and numTasks == 1: 
    lose_message(" task and entered " + str(numRooms) + " rooms!")
  elif numRooms ==1 and numTasks>1:
    lose_message(" tasks and entered only " + str(numRooms) + " room!")
  elif numRooms == 1 and numTasks == 1: 
    lose_message(" task and entered only " + str(numRooms) + " room!")
  repeatGame()

# Asks the user if they would like to play the story adventure game again. If they answer yes, it outputs the entire game for them.
def repeatGame():
  repeatGameUserAnswer = ""
  repeatGame = True
  print("")
  while repeatGame:
    repeatGameUserAnswer = (input("Would you like to play this game again? Enter Y for yes or N for no: ")).upper()
    print("")
    if repeatGameUserAnswer.startswith("Y"):
      repeatGame = False
      # Resets the global variable to 0 so that it does not calculate the previous game's number of rooms they already entered and the tasks they did.
      global numTasks 
      numTasks = 0
      global numRooms 
      numRooms = 0
      waiting_room(1)
    elif repeatGameUserAnswer.startswith("N") or repeatGameUserAnswer.startswith!=("Y"):
      repeatGame = False
      # Outputs a final goodbye message if the user does not want to play the game again.
      print("Alright then, thank you for playing this story adventure game! Just remember that you and your loved ones are always welcome to try this adventure game again! Have a great day!")
      
# *** Functions end here! ***

# Starts the entire program by calling just 2 functions that include several other function calls within their code.
introduce_program()
waiting_room(1)







