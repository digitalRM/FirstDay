print("hello world")

# VARIBLES - a way to store a single peice of data
# integers
score = 0
health = 100
# string data type
name = "Your Name?"

print(health)
print(score)
print("Hello " + name)

user = input("What Is Your Name? ")
print("Hello , Nice to meet you " + user)

color = input("What's your favroite color? ")
print("Wow my favroite is also " + color + ", Nice!")



# CONDITIONALS - if/else statements used for decision-makeing
# tests if a conditon is true, if so do a command else so something

# if color == "blue":
#      print("The Sky Is blue")
#  elif color == "black":
#      print("Ah yes! The color of the night.")
#  else:
#       print("I geuss thats cool...")

if type(color) == str:
    print("Color is a String")

if isinstance(color, str) :
    print("Color is a String")