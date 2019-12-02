# This code is an educational, interactive program designed to help users see the power of perspective.
# Numerous prompts will be printed with two choices for the user to select from: PMA (positive mental attitude) or nma (negative mental attitude)
# Using a for loop, the program will return results based on the user's choice of perspective
# Answers aren’t necessarily right or wrong, but they simply produce different results
# At the end of the prompts, there will be a conclusion paragraph to wrap up the purpose of this program
# str prepares user for prompts
print "Following will be a selection of prompts in which you'll choose your perspective on the situation. Type PMA to see it positively or NMA to see it negatively. Alternate your answers to see the differences in results."
# str gives context on prompt 1
print "You're a soccer player trying out for the school team and you end up getting cut. Type PMA to see this positively or NMA to see this negatively."
# cut returns statement depending on user's choice
def cut(perspective):
  for perspective in cut:
    if perspective = raw_input("PMA"):
      return "You're hopeful because it exposed some areas for improvement that you'll work on for next year."
    if perspective = raw_input("NMA"):
      return "Your self-esteem is shot by the fact you were cut so you give up trying."
# str gives context on prompt 2
print "You're a recent college grad who's been interviewing for multiple jobs but they all turned you down. Type PMA to see this positively or NMA to see this negatively."
# jobs returns a statement depending on user's choice
def jobs(perspective):
  for perspective in jobs:
    if perspective = raw_input("PMA"):
      return "You're optimistic because you've learned a ton through these experiences that are sharpening your skills for the next opportunity."
    if perspective = raw_input("NMA"):
      return "You begin to doubt your capabilities in the field so you settle for opportunities not as challenging or rewarding."
# str gives context on prompt 3
print "You're halfway through the semester and you fail a midterm that's a sizable portion of your overall grade. Type PMA to see this positively or NMA to see this negatively."
# midterm returns a statement depending on user's choice
def midterm(perspective):
  for perspective in midterm:
    if perspective = raw_input("PMA"):
      return "You're not too down because there's another half of the semester to go and you know what adjustments to make for the final."
    if perspective = raw_input("NMA"):
       return "Your confidence is shot so you drop the class to avoid a hit on your GPA."
# str gives context on prompt 4
print "You're a commuter on your way to class and you need to pull over because your car unexpectedly shut down. Type PMA to see this positively or NMA to see this negatively."
# car returns a statement depending on user's choice
def car(perspective):
  for perspective in car:
    if perspective = raw_input("PMA"):
      return "You're thankful that you were able to get clear of the road safely."
    if perspective = raw_input("NMA"):
      return "You're enraged at your car and it destroys the rest of your day."
# str wraps up the purpose of the program
print "PMA stands for positive mental attitude and NMA stands for negative mental attitude. How your life pans out is dependent on your attitude towards it. Your mental state influences your physical actions which influences your end results. Choose your perspective, and you choose your life trajectory. Choose wisely!"
