# bounce.py
#
# Exercise 1.5
# ATTEMPT 1
#--------------------------
# Define Variables
height = 100 #in metres
bounce_factor = 3/5
# Make Table Framework
print("Bounce #\tHeight (m)")
print("--------\t-----------")
# Create loop
for bounce in range (1, 11): #11 to be 10 inclusive 
  height *= bounce_factor #*= is shorthand for height = height * bounce factor
  print(f"{bounce}\t\t{height:.2f}") #2.f specifies decimals
# Alternative solution
#-----------------------------
height = 100
bounce = 1
while bounce <= 10:
  height = height * (3/5)
  print bounce, round(height, 4))
  bounce += 1
  
