import itertools
from colorama import Fore,Back,Style,init
init()


def game(mat,cur_p=0,i=0,j=0,disp=False):
	try:                                            #try is for error handling
		if mat[i][j]!=0:
			print("Oops already occupied try another! ")
			return mat, False
		print("   "+"  ".join([str(i) for i in range(len(mat))]))     # str() is a function so we need to use () 
		if not disp:
			mat[i][j]=cur_p

		for count,row in enumerate(mat):
			crow=""
			for y in row:
				if y==0:
					crow+="   "
				elif y==1:
					crow+=Fore.GREEN+' X '+ Style.RESET_ALL
				elif y==2:
					crow+=Fore.MAGENTA+' O '+ Style.RESET_ALL
			print(count, crow)
		
		return mat, True
	except IndexError as e:
		print("Did you input the row or column as 0,1,2...",e)
		return mat,False

	except Exception as e:
		print("Something went very wrong.....",e)
		return mat,False
	

def win(mat):
	def common(a):
		if a.count(a[0])==len(a) and a[0]!=0:
			return True
		else:
			return False
	# for rows
	for row in mat:
		if common(row):
			print(f"Player {row[0]} is the winner horizontally(--)")
			return True
	# for columns
	for q in range(len(mat)):
		cols=[]
		for row in mat:
			cols.append(row[q])
		if common(cols):
			print(f"Player {row[q]} is the winner vertically(|)")
			return True
	# for diagonals
	diags=[]
	for i in range(len(mat)):
		diags.append(mat[i][i])
	if common(diags):
		print(f"Player {diags[0]} is the winner diagonally \\")
		return True
	# the right diagonal now
	diags=[]
	for s,t in enumerate(reversed(range(len(mat)))):
		diags.append(mat[s][t])
	if common(diags):
		print(f"Player {diags[0]} is the winner diagonally /")
		return True


play=True
players=[1,2]
while play:
	size=int(input("Enter the size of the matrix for tic tac toe: "))
	matrix=[[0 for i in range(size)] for i in range(size)]
	won=False
	matrix, _ = game(matrix, disp=True)
	choice=itertools.cycle([1,2])
	while not won:
		cur=next(choice)
		print(Fore.CYAN+f"Current Player: {cur}"+Style.RESET_ALL)
		played=False
		while not played:
			col=int(input("Enter the columm:(0,1,2) "))
			row=int(input("Enter the row:(0,1,2) "))
			matrix,played=game(matrix,cur,row,col)
			if win(matrix):
				won=True
				mes=input("Would you like to play again? (y/n)")
				if mes.lower()=='y':
					print("Loading......")
					play=True
				if mes.lower()=='n':
					print("Thanks for playing...")
					play=False





