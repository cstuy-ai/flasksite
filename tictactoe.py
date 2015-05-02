########################################
# Tic - Tac - Toe Game                 #
# Version 1.0                          #
########################################





# Tic Tac Board Layout |V|
space = " "
board = '''
   |   |   
 %s | %s | %s 
___|___|___
   |   |   
 %s | %s | %s 
___|___|___
   |   |   
 %s | %s | %s 
   |   |   
'''

#print board%(space, space, space, space, space, space, space, space, space)
gamewon = False
boardlist = [1,2,3,4,5,6,7,8,9]
boardfilled = False
winningcombos = [[1,2,3] , [4,5,6] , [7,8,9] , [1,4,7] , [2,5,8] , [3,6,9] , [1,5,9] , [3,5,7]]
# ^ Winning combinations of cells
print board%tuple(boardlist)
player1 = True
# ^ defines which "player" ie: x or o you are currently. Player1 being X and not player 1 being O.
def spacefilled(index):
	if boardlist[index] != "x" and boardlist[index] != "o":
		return False
	return True

 

def replace(n, s):
	boardlist[n-1] = s
	return

#def win(s):
	#for combo in winningcombos:
		#gamewon = True
		#for cell in winningcombo[combo]:
			#if (


while not boardfilled:
# |v| Sets your player and checks which (X or O) to replace with
	player = "Player 1"
	if player1:
		s = "x"
	else:
		player = "Player 2"
		s = "o"
	inp = input ("Please specify your desired move...\n> ")
	if (inp >= 1 and inp <= 9 ):
		if (spacefilled(inp-1)):
			print "Space was filled already"
		else:
			replace(inp, s)
	
			player1 = not player1
# If you put in a number that breaks it, returns a message |v|
	else:
		print ("You have specified an invalid number, please choose a number on the board from 1 to 9")

   	print board%tuple(boardlist)
	boardn=0
	boardfilled = True
	while boardn < len(boardlist):
		if boardlist[boardn] != "x" and boardlist[boardn] != "o":
			boardfilled = False
		boardn += 1
	print boardfilled
	if boardfilled:
		print ("The game is over, the board has been filled")
	
 #winningcombos = [ [1,2,3] , [4,5,6] , [7,8,9] , [1,4,7] , [2,5,8] , [3,6,9] , [1,5,9] , [3,5,7]]
	woncombo = False
# ^ Whether your move has won ,  based on the check in the below For loop
#winningcombos[0]
	print winningcombos
	for g in winningcombos:
		w = 0		
		while w < len(g):	
			
			if boardlist[g[w]-1] != s:
				break
			elif w == 2:
				woncombo = True 
				break
			w = w+1
	if woncombo == True:
		break
print("The game has ended, hopefully you have enjoyed the game")


  





