import random

def drawBoard(board):
	
	print(board[1] + '|' + board[2] + '|' + board[3])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[7] + '|' + board[8] + '|' + board[9])


def inputPlayerLetter():
	
	letter=''
	while not(letter=='X' or letter=='O'):
		print("What would you like?'X' or 'O'?")
		letter = input().upper()

	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']


def whoGoesFirst():
	
	if random.randint(0,1) == 0:
		return 'computer'
	else:
		return 'player'
	


def playAgain():
	
	print('Want to play again? (y/n)')
	return input().lower().startswith('y')


def makeMove(board, letter, move):
	board[move] = letter


def isWinner(board,letter):
	# this function returns True if that letter player has won.
	return ((board[1]==letter and board[2]==letter and board[3]==letter) or
			(board[4]==letter and board[5]==letter and board[6]==letter) or
			(board[7]==letter and board[8]==letter and board[9]==letter) or
			(board[1]==letter and board[4]==letter and board[7]==letter) or
			(board[2]==letter and board[5]==letter and board[8]==letter) or
			(board[3]==letter and board[6]==letter and board[9]==letter) or
			(board[1]==letter and board[5]==letter and board[9]==letter) or
			(board[3]==letter and board[5]==letter and board[7]==letter))

def isSpaceFree(board, move):
	return board[move] == ' '


def getPlayerMove(board):
	
	move = '' 
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
		print('Your next move?')
		move = input()
	return int(move)


def minimax(board, depth, isMax, computerLetter):
	# Given a board and the computer's letter, determine where to move and return that move.
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if isWinner(board, computerLetter):
		return 10
	if isWinner(board, playerLetter):
		return -10
	if isBoardFull(board):
		return 0

	if isMax:
		best = -1000

		for i in range(1,10):
			if isSpaceFree(board, i):
				board[i] = computerLetter
				score = minimax(board, depth+1,False,computerLetter)
				board[i] = ' '

				if (score > best):
					best=score

		return best
	else:
		best = 1000

		for i in range(1,10):
			if isSpaceFree(board, i):
				board[i] = playerLetter
				score = minimax(board, depth+1,True,computerLetter)
				board[i] = ' '

				if (score < best):
					best=score

		return best


def findBestMove(board, computerLetter):
	# Given a board and the computer's letter, determine where to move and return that move.
	bestVal = -1000
	bestMove = -1


	for i in range(1,10):
		if isSpaceFree(board, i):
			board[i] = computerLetter

			moveVal = minimax(board, 0, False,computerLetter)

			board[i] = ' '

			if moveVal > bestVal:
				bestMove = i
				bestVal = moveVal

	return bestMove


def isBoardFull(board):
	# Return True if every space on the board has been taken. Otherwise return False.
	for i in range(1,10):
		if isSpaceFree(board, i):
			return False
	return True


print('\nWelcome to Tic Tac Toe!\n')
print('A Sample for the board numbering')
drawBoard('0 1 2 3 4 5 6 7 8 9'.split())
print('')

while True:
	# Reset the board
	theBoard = [' '] * 10
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	print('The ' + turn + ' will go first.')
	gameIsPlaying = True

	while gameIsPlaying:
		if turn == 'player':
			drawBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)

			if isWinner(theBoard, playerLetter):
				drawBoard(theBoard)
				print('You won the game :)\n')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('This game is a tie :|\n')
					break
				else:
					turn = 'computer'
		else:
			move = findBestMove(theBoard, computerLetter)
			makeMove(theBoard, computerLetter, move)

			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print('You lost the game :(\n')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('This game is a tie :|\n')
					break
				else:
					turn = 'player'
	if not playAgain():
		break