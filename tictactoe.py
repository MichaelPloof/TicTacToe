import math
import time
import copy
import random

ehealth = 100 #enemy health
phealth = 100
class Tictactoe:
    grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    grid_simul = copy.deepcopy(grid)
    moves_temp = random.sample(["X", "O"], 2)
    computer = moves_temp[0]
    player = moves_temp[1]
    winner = "t" # t = tie, p = player, e = enemy
    def __init__(self, health):
        self.anger = 100-health
    def __repr__(self):
        n = self.grid
        return "=============\n| {a1} | {a2} | {a3} |\n=============\n| {b1} | {b2} | {b3} |\n=============\n| {c1} | {c2} | {c3} |\n=============\n".format(a1=n[0][0], a2=n[0][1], a3=n[0][2], b1=n[1][0], b2=n[1][1], b3=n[1][2], c1=n[2][0], c2=n[2][1], c3=n[2][2])
    def input_move(self, player, index1, index2):
        if self.grid[index1][index2] == " ":
            self.grid[index1][index2] = player
            return True
        else:
            return False
    def input_move_simul(self, player, index1, index2):
        if self.grid_simul[index1][index2] == " ":
            self.grid_simul[index1][index2] = player
            return True
        else:
            return False
    def get_empties(self):
        total = 0
        for i in range(len(self.grid_simul)):
            for j in range(len(self.grid_simul[i])):
                if self.grid_simul[i][j] == " ":
                    total +=1
        return total
    def get_inputs(self):
        list = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == " ":
                    list.append([i, j])
        return list
    def get_inputs_simul(self):
        list = []
        for i in range(len(self.grid_simul)):
            for j in range(len(self.grid_simul[i])):
                if self.grid_simul[i][j] == " ":
                    list.append([i, j])
        return list
    def find_winner(self):
        # rows
        if (self.grid[0][0]==self.grid[0][1]) and (self.grid[0][0]==self.grid[0][2]):
            return self.grid[0][0]
        elif (self.grid[1][0]==self.grid[1][1]) and (self.grid[1][0]==self.grid[1][2]):
            return self.grid[1][0]
        elif (self.grid[2][0]==self.grid[2][1]) and (self.grid[2][0]==self.grid[2][2]):
            return self.grid[2][0]
        # columns
        elif (self.grid[0][0]==self.grid[1][0]) and (self.grid[0][0]==self.grid[2][0]):
            return self.grid[0][0]
        elif (self.grid[0][1]==self.grid[1][1]) and (self.grid[0][1]==self.grid[2][1]):
            return self.grid[0][1]
        elif (self.grid[0][2]==self.grid[1][2]) and (self.grid[0][2]==self.grid[2][2]):
            return self.grid[0][2]
        # diagonals
        elif (self.grid[0][0]==self.grid[1][1]) and (self.grid[0][0]==self.grid[2][2]):
            return self.grid[0][0]
        elif (self.grid[0][2]==self.grid[1][1]) and (self.grid[0][2]==self.grid[2][0]):
            return self.grid[0][2]
        else:
            return " "
    def find_winner_simul(self):
        # rows
        if (self.grid_simul[0][0]==self.grid_simul[0][1]) and (self.grid_simul[0][0]==self.grid_simul[0][2]):
            return self.grid_simul[0][0]
        elif (self.grid_simul[1][0]==self.grid_simul[1][1]) and (self.grid_simul[1][0]==self.grid_simul[1][2]):
            return self.grid_simul[1][0]
        elif (self.grid_simul[2][0]==self.grid_simul[2][1]) and (self.grid_simul[2][0]==self.grid_simul[2][2]):
            return self.grid_simul[2][0]
        # columns
        elif (self.grid_simul[0][0]==self.grid_simul[1][0]) and (self.grid_simul[0][0]==self.grid_simul[2][0]):
            return self.grid_simul[0][0]
        elif (self.grid_simul[0][1]==self.grid_simul[1][1]) and (self.grid_simul[0][1]==self.grid_simul[2][1]):
            return self.grid_simul[0][1]
        elif (self.grid_simul[0][2]==self.grid_simul[1][2]) and (self.grid_simul[0][2]==self.grid_simul[2][2]):
            return self.grid_simul[0][2]
        # diagonals
        elif (self.grid_simul[0][0]==self.grid_simul[1][1]) and (self.grid_simul[0][0]==self.grid_simul[2][2]):
            return self.grid_simul[0][0]
        elif (self.grid_simul[0][2]==self.grid_simul[1][1]) and (self.grid_simul[0][2]==self.grid_simul[2][0]):
            return self.grid_simul[0][2]
        else:
            return " "
    def get_player_move(self):
        is_valid = False
        print("Your turn!\n")
        time.sleep(1)
        while not is_valid:
            vpts = 0
            index1 = 0
            index2 = 0
            pmove = input("Input move here: ")
            pmovelist = list(pmove)
            if pmovelist[0].upper() == "A":
                index2 = 0
                vpts += 1
            elif pmovelist[0].upper() == "B":
                index2 = 1
                vpts += 1
            elif pmovelist[0].upper() == "C":
                index2 = 2
                vpts += 1
            else:
                print("Unrecognized Column")
            try:
                if int(pmovelist[1]) == 1:
                    index1 = 0
                    vpts += 1
                elif int(pmovelist[1]) == 2:
                    index1 = 1
                    vpts += 1
                elif int(pmovelist[1]) == 3:
                    index1 = 2
                    vpts += 1
                else:
                    print("Unrecognized Row")
            except:
                print("Unrecognized entry")
            if vpts == 2:
                if self.input_move(self.player, index1, index2):
                    print(" ")
                    print(self)
                    is_valid = True
                else:
                    print("Invalid Square: {pmove} already is placed".format(pmove=pmove))
        time.sleep(1)
    def minimax(self, player):
        max_player = self.computer
        other_player = 'O' if player == 'X' else 'X'

        if self.find_winner_simul() == other_player:
            return {'position': None, 'score': 1 * (self.get_empties() + 1) if other_player == max_player else -1 * (self.get_empties() + 1)}
        elif self.get_empties() == 0:
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        for i in self.get_inputs_simul():
            self.input_move_simul(player, i[0], i[1])
            sim_score = self.minimax(other_player)
            self.grid_simul[i[0]][i[1]] = ' '
            sim_score['position'] = i

            if player == max_player: 
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
    def reset(self, health):
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.grid_simul = copy.deepcopy(self.grid)
        self.moves_temp = random.sample(["X", "O"], 2)
        self.computer = self.moves_temp[0]
        self.player = self.moves_temp[1]
        self.winner = "t"
        self.anger = 100-health
    def rand_chance(self):
        randints = range(100)
        randchance = random.choice(randints)
        return randchance
    def play(self):
        print("    A   B   C\n  =============\n1 |   |   |   |\n  =============\n2 |   |   |   |\n  =============\n3 |   |   |   |\n  =============\n\nWhen inputing the move of your choice, state the column and the row (e.g. A1 or C2)\n\n")
        time.sleep(1)
        for i in range(9):
            if ((self.computer == "O") and (i%2 == 0)) or ((self.computer == "X") and (i%2 == 1)):
                self.get_player_move()
                if self.find_winner() == "X":
                    self.winner = "p" if self.player == "X" else "e"
                    return True
                elif self.find_winner() == "O":
                    self.winner = "e" if self.player == "X" else "p"
                    return True
            else:
                is_valid = False
                index1 = 0
                index2 = 0
                rand_chance = self.rand_chance()
                if rand_chance > self.anger:
                    while not is_valid:
                        cinputs = range(9)
                        cmove = random.choice(cinputs)
                        if cmove/3 < 1:
                            index1 = 0
                        elif cmove/3 >=1 and cmove/3 < 2:
                            index1 = 1
                        else:
                            index1 = 2
                        index2 = cmove%3
                        if self.input_move(self.computer, index1, index2):
                            is_valid = True
                            print("\nComputer has made it's move!\n")
                            print(self)
                else:
                    while not is_valid:
                        self.grid_simul = copy.deepcopy(self.grid)
                        cmoves = self.minimax(self.computer)
                        index1str = cmoves["position"][0]
                        index2str = cmoves["position"][1]
                        index1 = int(index1str)
                        index2 = int(index2str)
                        if self.input_move(self.computer, index1, index2):
                            is_valid = True
                            print("\nComputer has made it's move!\n")
                            print(self)
                    if self.find_winner() == "X":
                        self.winner = "p" if self.player == "X" else "e"
                        return True
                    elif self.find_winner() == "O":
                        self.winner = "e" if self.player == "X" else "p"
                        return True
                     
tictactoe = Tictactoe(ehealth)
print("Welcome, stranger, to the marvelous game of Tic Tac Toe.\n")
time.sleep(2)
print("This program uses artifical intellegence (specifically, the minimax algorithm) to come up with the best possible move. It is unbeatable.\n")
time.sleep(3)
print("Would you like to try the ai or would you like to begin the game?")
time.sleep(1.5)
pchoice = input("Input \"y\" if you wish to challenge the unbeatable ai, or input anything else to play the game: ")
if pchoice.lower() == "y":
    print("\nYou have chosen to challenge the unbeatable ai. Have fun!\n")
    tictactoe.anger = 100
    tictactoe.play()
    if tictactoe.winner == "p":
        print("You won? Please let me know of this, this is supposed to be unbeatable")
    elif tictactoe.winner == "e":
        print("You have lost.")
    elif tictactoe.winner == "t":
        print("As I expect to happen, you have tied. In fact, if you pair minimax with itself, it will tie 100% of the time!")
else:
    print("\nYou have chosen to play the main game: Very well, good luck!\n")
    time.sleep(1)
    while (ehealth > 0) and (phealth > 0):
        print("\nComputer currently has {hp} hp.".format(hp=ehealth))
        time.sleep(1)
        print("\nYou have {hp} hp.\n".format(hp=phealth))
        time.sleep(1)
        tictactoe.play()
        if tictactoe.winner == "p":
            print("You win! The computer has lost 10 hp")
            ehealth -= 10
            time.sleep(1)
        elif tictactoe.winner == "e":
            print("Computer wins! Computer has gained 10 hp")
            phealth -= 10
            time.sleep(1)
        elif tictactoe.winner == "t":
            print("It's a tie. Computer loses 2 hp")
            ehealth -= 2
            time.sleep(1)
        tictactoe.reset(ehealth)
    if ehealth <= 0:
        print("CONGRADULATIONS, YOU WIN!")
        time.sleep(1)
    else:
        print("You have lost.")
        time.sleep(1)
print("\n\nAs you may probably tell, the game of tic tac toe is solved, meaning computers can always find the optimal moves necesary to beat or tie the game. As a result, the optimal games always result in a tie.\n\nThank you for playing!")
