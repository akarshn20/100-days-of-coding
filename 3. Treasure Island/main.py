from art import logo

print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You are at a crossroad. Where do you want to go? ")
direction = input("Type 'left' or 'right' ")
if direction == "left":
  print(f"You have chosen {direction}. You are now at a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
  action = input("What to do? wait or swim? ")
  if action == "wait":
    print(f"You have chosen {action}. You are now at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
    door = input("Which door?red, yellow or blue? ")
    if door == "red":
      print(f"You have chosen {door}. You are burned by fire. Game over.")
    elif door == "yellow":
      print(f"You have chosen {door}. You win!")
    elif door == "blue":
      print(f"You have chosen {door}. You are eaten by beasts. Game over.")
    else:
      print(f"You have chosen {door}. Game over.")
  else:
    print(f"You have chosen {action}. You are attacked by trout. Game over.")
else:
  print(f"You have chosen {direction}. You fall into a hole. Game over.")