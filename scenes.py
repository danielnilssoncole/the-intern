# This file contains all the scenes for the game "The Interview"

from sys import exit
from random import randint 


#each class is a scene and returns a value of the name of the next scene
#as a string for the engine to use the map dictionary to know what to do 
#next

#create base class scene in order to create the scenes of the game
class Scene(object):

	def enter(self):
		exit(1)
		
#creates class Interview that is a Scene	
class Interview(Scene):
	#This is the first scene of the game
	#In this scene, the user will interview for the intern positon and be accepted or
	#rejected
	
	def enter(self):
		#intro: game set up
		print """
			\n\n\t\t\t\t ###THE INTERN###"""
		print "You are an aspiring DJ.\n"
		print "You need to make a living somehow before your DJ skills can pay the bills.\n"
		print "You recently applied to be an intern at independent record label called"
		print "'Palm Tree Records' in your home town.\n"
		print "Your interview with John, the owner of the label, starts now.\n\n"
		
		#interview
		print 'John:\t"Hello, thank you for coming in to interview with us today."\n'
		
		name = raw_input('John:\t"What is your name?"\n> ')
		print ""
		print 'John:\t"We\'re looking for someone who will do anything that they\'re asked of.'
		print '\tSomeone that will get the job done reguardless of what it takes.'
		print '\tAre you that person, %s?"\n' % name
		
		print "You can respond to this in two ways:\n"
		print "\t1. Yes, I am that person willing to go the extra mile.\n"
		print "\tOR\n"
		print "\t2. No, I really just want to use this position to get connects for DJing."
		print "\t   I don't really care about the label or the job itslef.\n"
		
		choice = raw_input("Choose 'Yes' or 'No' > \n")
		
		if choice.lower() == "yes":
			print '\nJohn: "Great! Your hired, your first day is tomorrow!"\n\n\n'
			return 'coffee_conflict'
		elif choice.lower() == "no":
			print '\nJohn: "Sorry, we\'re going to move in a different direction."'
			return 'game_over'
		else:
			print "\nYou did not choose 'yes' or 'no'. Interview over.\n"
			return 'game_over'
			
			
class CoffeeConflict(Scene):
	#This is the second scene in the game
	
	def enter(self):
		print "It's your 2nd week on the job, and things are going well.\n"
		print "Some one with a higher position at the label says to you:\n"
		print '\t"Hey new guy, make me some coffee."\n'
		print "You can respond to this in three different ways:\n"
		
		print '\t1. [Excited] "Ok, I\'ll get right on that!"\n'
		print '\t2. [Unbothered] "I\'m not here to serve you coffee."\n'
		print '\t3. [Screams abnoxiously] "I ain\'t gettin you a mother flippin thing!"\n'
		
		choice = raw_input('Choose 1, 2, or 3 > \n')
		
		if choice == '1':
			print "\n"
			print "You might not have realized this at the time," 
			print "but what your co-worker asked of you was very disrespectful."
			print "By fulfilling his request, you're letting him know that is ok to"
			print "disrespect you. This leads to more disrespect from him, and other"
			print "co-workers. You will deal with it for a some time, in order to keep"
			print "the job, but after some time, you will get tired of it and decide to"
			print "quit the job.\n"
			print "So let's end this now.\n\n"
			
			return 'game_over'
			
		elif choice == '2':
			print "\n"
			print "You handled this very well. You let your co-worker know that it is not"
			print "ok to disrespect you. And you did not return his disrespect with more"
			print "disrespect. You're co-worker will now think twice before disrespecting you."
			print "This will be great as you advance your status at the label.\n"
			
			return 'new_talent'
			
		elif choice == '3': 
			print "\n"
			print "You have every right to be angry. Your co-worker disrespected you."
			print "You made a scene, and HR doesn't know the whole story, and you look"
			print "like the bad guy.\n"
			print "You're fired.\n"
		
			return 'game_over'
			
		else:
			print "\nYou did not choose '1', '2', or '3'.\n"
			
			return 'game_over'
			
			
class NewTalent(Scene):
	#3rd scene
	
	def enter(self):
		print "\nThe label is looking for new talent.\n"
		print "You've demonstrated that you have good taste in music, so the label asks"
		print "you to submit 2 unsigned artists. Enter the names of the artists or groups"
		print "you would like to submit."
		
		act1 = raw_input('Act 1 > ')
		act2 = raw_input('Act 2 > ')
		
		choice_int = randint(0, 10) #random number to decide which act is chosen
		
		
		if choice_int <= 4:
			choice = act1
			
		elif choice_int > 4 and choice_int < 8:
			choice = act2
			
		else:
			choice = 'none'
			
		
		if choice == act1 or choice == act2:
			print "\nJohn, the owner of the label, listened to both of the acts that you"
			print "submited. He really like %s's music and wants to sign them ASAP!" % choice
			print "%s signs to Palm Tree Records the next week." % choice
			print "\nYou are now an A&R person at the label, congrats on the promotion!\n"
			
			return 'a_and_r'
			
		else:
			print "\nAlthough both %s and %s are really great. John didn't like either of"
			print "them. If he did, you could have become an A&R person at the label."
			print "A week later, the label fires you.\n"
			
			return 'game_over'
			
			
class AandR(Scene):
	#final scene
	
	def enter(self):
	
		print "\nNow that you are an A&R person. You are responsible for overseeing 5 acts"
		print "that are signed to Palm Tree Records.\n"
		print "A year has passed, and the label is evaluating the progress of each of"
		print "the acts that you oversee. The label is also evaluating your performance"
		print "based on the success of each act you oversee.\n"
		
		#scores for each act
		act1 = randint(1, 10)
		act2 = randint(1, 10)
		act3 = randint(1, 10)
		act4 = randint(1, 10)
		act5 = randint(1, 10)
		
		
		num = randint(6, 11)
		choice = raw_input('Guess a number 6 - 10 to boost your success rate > \n')
		
		#if guess is right, add bonus, if not, no bonus
		if choice == num:
			#include bonus score in user's average for boost
			print "You guessed correctly, congrats on the %d point bonus!\n" % num
			bonus = num
			acts = [act1, act2, act3, act4, act5, bonus]
		else:
			print "You guessed incorrectly, no bonus this year.\n"
			#no bonus, no boost
			acts = [act1, act2, act3, act4, act5]
			
		
		
		#A&R's average score
		ar = float(sum(acts)) / float(len(acts))
		
		print "Here is the success rate of each act.\n"
		print "The Birds success rate this year was %d" % act1
		print "Mondai success rate this year was %d" % act2
		print "The Beaks success rate this year was %d" % act3
		print "Sailure success rate this year was %d" % act4
		print "The Sox success rate this year was %d\n" % act5
		
		print "Your success rate this year was %.2f\n" % ar
		
		if ar >= 5:
			print "Congratulations on a great year!\n"
			print "Because of your success, you have been promoted to the Director of A&R.\n"
			print "YOU WIN!\n"
			return 'game_complete' 
		else:
			print "It was rough year for you. Palm Tree Records has decided to let you go.\n"
			print "GAME OVER\n"
			return 'game_over'
			
			
class GameOver(Scene):
	def enter(self):
		print '\nGAME OVER\n'
		exit(1)
		
class GameComplete(Scene):
	def enter(self):
		return 'game_complete'
			
		
		
		
		
		