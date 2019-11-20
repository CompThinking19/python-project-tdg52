# gives the user context on scenario 1
print "You're a soccer player trying out for the school team and you end up getting cut."
# this is how the user will choose between mental attitudes
def cut(attitude):
  if attitude == 'P':
    return "You're hopeful because it exposed some areas for improvement that you'll work on for next year."
  if attitude == 'N':
    return "Your self-esteem is shot by the fact you were cut so you give up trying."
# gives the user context on scenario 2
print "You're a recent college grad who's been interviewing for multiple field jobs but they all turned you down."
# this is how the user will choose between mental attitudes
def jobs(attitude):
  if attitude == 'P':
    return "You're optimistic because you've learned a ton through these experiences that are sharpening your skills for the next opportunity."
  if attitude == 'N':
    return "You begin to doubt your capabilities in the field so you settle for opportunities not as challenging or rewarding."
# gives the user context on scenario 3
print "You're halfway through the semester and you fail a midterm that's a sizable portion of your overall grade."
# this is how the user will choose between mental attitudes
def midterm(attitude):
  if attitude == 'P':
    return "You're not too down because there's another half of the semester to go and you know what adjustments to make for the final."
  if attitude == 'N':
    return "Your confidence is shot so you drop the class to avoid a hit on your GPA."
# gives the user context on scenario 4
print "You're a commuter on your way to class and you need to pull over because your car unexpectedly shut down."
# this is how the user will choose between mental attitudes
def car(attitude):
  if attitude == 'P':
    return "You're thankful that you were able to get clear of the road safely."
  if attitude == 'N':
    return "You're enraged at your car and it destroys the rest of your day."
