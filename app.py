import time
from flask import Flask, render_template, request
import random

gamewon = False
final = []

def print_maze(maz): #takes a 2 dimensional array and prints it as strings
	#print chr(27) +"[2J"
	s=""	
	for n in maz:
		for u in n:
			s += u
		#s= s[:-1] #takes out the last character, the extra new linw
	return s

# function for checking postions in maze
def checkpos(m,r,c):
	global gamewon
	global final
	tempmaze = m
	if gamewon:
		return final
	if m[r][c] in "+-|": # Wall Case
		return
	if m[r][c] == '$': # Winning Case
		gamewon = True
		return final
	if tempmaze[r][c] == '#': # Visited Case
		return
	if tempmaze[r][c] == " ":
		tempmaze[r][c] = '#'
		final = print_maze(tempmaze)
		print final
		time.sleep(0)
		checkpos(tempmaze,r,c+1) #Check up
		checkpos(tempmaze,r,c-1) #Check down
		checkpos(tempmaze,r+1,c) #check left
		checkpos(tempmaze,r-1,c) #check right
		tempmaze[r][c]="." # Replace w/ dot to mark "Bad positions" ie: leading to dead ends

app = Flask(__name__)
name="Bob"

@app.route("/")
def index():
	color = random.randrange(0,20000)
	return render_template("index.html", name=name,color=color)

@app.route("/page")
def page():
	return render_template("page.html",name=name)

@app.route("/maze", methods=["GET","POST"])
def maze():

	# || Maze Solving Program||
	#
	#variables

	path = '#'
	wall = '='
	exit = '$'
	visited = '#'
	deadend = "."
	solved = False
	start = '*'
	x = 0
	y = 1
	gamewon = False
	#import file
	mazefile = open('maze.txt')
	#open might read automatically
	# file.read () [everything in a string] or file.readlines()[everything in a list] or file.readline()

	maze = mazefile.readlines()
	#maze string array
	maze2=[]
	for line in maze:
		m=[]
		l=0
		while l < len(line):
			m.append(line[l])
			l += 1
		maze2.append(m)	
	#print "ASDFGASGFASF\n\n" + str(m)
	if request.method=="GET":	
		m = print_maze(maze2)	
		return render_template("maze.html",maze=m)
	else:
		m = checkpos(maze2,1,1) #None?
		return render_template("maze.html",maze=m)

@app.route("/mazesolved", methods=["GET","POST"])
def mazesolved():

	# || Maze Solving Program||
	#
	#variables

	path = '#'
	wall = '='
	exit = '$'
	visited = '#'
	deadend = "."
	solved = False
	start = '*'
	x = 0
	y = 1
	gamewon = False
	#import file
	mazefile = open('maze.txt')
	#open might read automatically
	# file.read () [everything in a string] or file.readlines()[everything in a list] or file.readline()

	maze = mazefile.readlines()
	#maze string array
	maze2=[]
	for line in maze:
		m=[]
		l=0
		while l < len(line):
			m.append(line[l])
			l += 1
		maze2.append(m)	
	#print "ASDFGASGFASF\n\n" + str(m)
	if request.method=="GET":
		m = checkpos(maze2,1,1)	
		#m = print_maze(maze2)	
		return render_template("mazesolved.html",maze=m)

if __name__ == "__main__":
	#checkpos(maze2,1,1)
	app.debug = True
	app.run()



	
