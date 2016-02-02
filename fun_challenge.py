# decision tree to decide if you should eat the bacon!

q1 = str.upper(raw_input("Do you want to feel like angels are frolicking in your tastebuds?"))

if q1 == "YES":
	print "Eat it!"
elif q1 == "NO":
	print "You've clearly never tasted bacon"
	print "Eat it"
else:
	q2 = str.upper(raw_input("Are you a coward?"))

if q2 == "NO":
	print "Then eat it"
else: print "bacon will turn you into a true warrior"

