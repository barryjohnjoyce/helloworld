#name = raw_input("hi, what is your name?")
#age = raw_input("and what is your age?")

#print "Hello, %s!" % name #in this context modulus means "take this string and put it into another string"

#print "Hello, {0}! so, you are {1} years old!".format(name,age)

name = raw_input("Hi, what is your name?")

response = raw_input("Hello " +name.capitalize() + ", would you like to play a game?")

if response.capitalize() == 'Y':
    print "You die in a horrible global thermonucleur war"
elif response.capitalize() == 'N':
    print " Good choice, the only way to win is not to play"
else:
    print "Enter Y or N"


