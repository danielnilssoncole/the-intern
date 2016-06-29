# The Map and Engine for The Intern

from sys import exit
from scenes import *


class Map(object):
	
	#creates dictionary where the keys are the name of each scene as a string
	#the values are an instance of the class of each scene
	scenes = {
				'interview' : Interview(),
				'coffee_conflict' : CoffeeConflict(),
				'new_talent' : NewTalent(),
				'a_and_r' : AandR(),
				'game_complete' : GameComplete(),
				'game_over' : GameOver()
									}
	
	#initiate class
	#input variable start scene so the Map will know where to begin
	def __init__(self, start_scene):
	
		#create variable within the class so that it can be used whenever an instance of 
		#the class is called
		self.start_scene = start_scene
			
	#when next_scene function is called, input variable is name of the scene	
	def next_scene(self, scene_name):						
		
		#creates an instance of class Map
		#gets the scene name from dictionary and returns the value, which is an instance
		#of class of the new scene
		#gets key, returns value
		val = Map.scenes.get(scene_name)
		return val
		
		
	def opening_scene(self):
		#uses next_scene function with the input of the start scene variable
		#the next scene function returns the value of an instance of class of the input scene
		return self.next_scene(self.start_scene)
		

class Engine(object):
	
	#a Map class will be the input variable when creating an instance of engine class
	def __init__(self, scene_map):
		#stores map within engine class so it can be used throughout the class
		self.scene_map = scene_map
		
		
	def play(self):
		
		#variable stores the current scene of the game
		#uses opening_scene function from map class
		#opening scene function takes in a scene name and return an instance of the class
		#of that scene
		#current_scene = Scene1()
		current_scene = self.scene_map.opening_scene()

		#stores variable of the last scene
		#uses next scene function from map class create an instance of the class of the
		#last scene
		#last_scene = GameComplete()
		last_scene = self.scene_map.next_scene('game_complete')
		
		
		#create loop to go through each scene
		while current_scene != last_scene:
			
			#store the next scene name in a variable
			#current_scene is an instance of a scene class
			#use the enter function to run the scene and return the string name of the
			#next scene
			#next_scene = 'next_scene'  - key for map dictionary to use to get value
			next_scene_name = current_scene.enter()
			
			print "\t\t\t***\n"
			
			
			#update the current scene and run the scene
			#use next_scene function from the map class to create an instance of the 
			#class of the next scene name
			#current_scene = NextScene()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		#run the last scene, because the while loop will not	
		current_scene.enter()
		

