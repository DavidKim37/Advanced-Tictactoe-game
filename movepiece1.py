import random
gameend = False
player = "X"
playboard = "0"
validmove1 = False
currentblock = ""
dictio = {"a3":"A","b3":"B","c3":"C","a2":"D","b2":"E","c2":"F","a1":"G","b1":"H","c1":"I"}
dead = []
def check(board,boards,currentblock,dead,color,player):
  filled = []
  gameend = False
  algorithm = [["a1","b1","c1"],["a2","b2","c2"],["a3","b3","c3"],["a1","a2","a3"],["b1","b2","b3"],["c1","c2","c3"],["a1","b2","c3"],["a3","b2","c1"]]
  for i in boards[ord(currentblock)-65]:
    if boards[ord(currentblock)-65][i] == player:
      filled.append(i)
  x = 0
  try:
    for i in algorithm:
      for k in i:
        if k in filled:
          x += 1
      if x == 3:
        raise("Hi")
      else:
        x = 0
  except:
    print("A block was won")
    dead.append(currentblock)
    for i in board:
      if i[0] == currentblock:
        if i[1:3] == "b2":
          board[i] = color[0:6] + i[0] + color[7:12]
        board[i] = color
    gameend = checkmate(color,dead,board)
  return gameend,dead,board

def checkmate(color,dead,board):
  algorithm = [["A","B","C"],["D","E","F"],["G","H","I"],["A","D","G"],["B","E","H"],["C","F","I"],["A","E","I"],["G","E","C"]]
  filled = []
  for i in dead:
    if board[i + "a1"] == color:
      filled.append(i)
  x = 0
  try:
    for i in algorithm:
      for k in i:
        if k in filled:
          x += 1
      if x == 3:
        raise("Hi")
      else:
        x = 0
    return False
  except:
    return True

def movepiece(currentblock,dead,board,player,dictio,boards,color):
  gameend = False
  randomized = False
  try:
    if currentblock == "":
      currentblock = input(color + "Please enter the block you would like to move in\u001B[0m\n").upper()
      try: 
        if ord(currentblock) - 64 > 9 or currentblock in dead:
          randomized = True
          currentblock = chr(random.randint(1,8)+64).upper()
          while currentblock in dead:
            currentblock = chr(random.randint(1,8)+64).upper()
      except:
        randomized = True
        currentblock = chr(random.randint(1,8)+64).upper()
        while currentblock in dead:
          currentblock = chr(random.randint(1,8)+64).upper()
    printboard(board,currentblock,dead)
    if randomized:
      print("You entered an invalid response. Sad face. Therefore, a random block was selected for you. More sad face.")
      randomized = False
    print(currentblock)
    usermove = input(color + "Player " + player + " please enter a move.\u001B[0m\n")
    if usermove[0] == "a" or usermove[0] == "b" or usermove[0] == "c":
      if usermove[1] == "1" or usermove[1] == "2" or usermove[1] == "3":
        if board[currentblock + usermove][0] == " ":
          if player == "X":
            board[currentblock + usermove] = color + board[currentblock+usermove] + "\u001B[0m"
            boards[ord(currentblock) - 65][usermove] = "X"
            gameend,dead,board = check(board,boards,currentblock,dead,color + "   " + "\u001B[0m",player)
            player = "O"
            color = "\u001B[44m"
          else:
            board[currentblock + usermove] = color + board[currentblock+usermove] + "\u001B[0m"
            boards[ord(currentblock) - 65][usermove] = "O"
            gameend,dead,board = check(board,boards,currentblock,dead,color + "   " + "\u001B[0m",player)
            player = "X"
            color = "\u001B[41m"
          currentblock = dictio[usermove]
          if currentblock in dead:
            currentblock = ""
          printboard(board,currentblock,dead)
    elif usermove[0:4] == "dead":
      dead.append(usermove[4].upper())
  except Exception as e:
    print(e)
  try:
    if gameend == False:
      movepiece(currentblock,dead,board,player,dictio,boards,color)
      pass
    else:
      if player == "X":
        player = "blue"
      else:
        player = "red"
      print("Good game,", player, "wins")
      exec(open("main.py").read())
  except: movepiece(currentblock,dead,board,player,dictio,board,color)