#----------------------------------------------------
# Game implementation
#----------------------------------------------------

from typing import List
from .goat import Goat
from .board import Board
from .player import Player
from .stack import Stack

GOATS_PER_PLAYER = 4
WINNING_NUMBER_GOATS = 3
VALID_COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
SIDE_JUMP_SIZE = 1
FORWARD_JUMP_SIZE = 1

class Game:
    '''
    Represents the Goat Race game
    '''
    ################################################
    #
    # The following methods MUST be in your solution
    # 
    ################################################
    def __init__(self, width: int, height: int, obstacle_positions: List = []):
        '''Initializes the game'''
        self.board = Board(width, height,obstacle_positions)            #initialise the board object
        self.players = []                                               #initialise the player list
        self.phase = 1                                                  #initialise the game with phase 1
        self.turn = 0                                                   #initialise the player turn to 0
        self.width = width
        self.height = height
        

    def __str__(self) -> str:
        '''Returns a visual snapshot of the game'''
        player_list = []
        for player in self.players:                     #iterate over player  list
            player_list.append(player.colour)           #player is an object from player class
        line = str(self.board) + '\n' + 'Players: ' + ','.join(player_list) + '\n' + 'Phase: '+ str(self.phase) + '\n' + 'Player whose turn it is: ' + self.get_current_player().colour
        return line                                     # returns str representation of the board with current players, phase, player's turn

    def get_phase(self) -> int:
        '''Returns the game phase'''
        return self.phase

    def get_turn(self) -> int:
        '''Returns the index of the player whose turn it is'''
        return self.turn  
        

    def get_current_player(self) -> Player:
        '''Returns the current player'''
        return self.players[self.turn]
        
    
    def get_goats_blocked(self, player: Player) -> int:
        '''Returns the number of goats blocked for a given player'''
        blocked_goats = 0
        player_goats = player.goat                     #list of the particular player's goat. Each object in that list is goat object
        
        for goat in player_goats:                      #iterate over each goat object
            goat_position = goat.get_position()        #str representation of a goat
            col = ord(goat_position[0])-65       
            row = int(goat_position[1])-1
            top_goat = self.get_top_goat(row,col)       #gets the top goat on a particular position on the board
            if (top_goat == goat.get_colour()[0].upper()) and (self.check_sideways_up(row,col) or self.check_sideways_down(row,col) or self.check_forward_step(row,col)): #check the blocked goats of the player
                blocked_goats = blocked_goats           # if goat is not blocked, it doesn't increaments the blocked goat counter
            else:
                blocked_goats += 1                      #if goat is blocked, it increaments the counter

        return  blocked_goats                           
    
    def check_sideways_up(self,row:int,col:int) -> bool:
        '''
        check if the goat can move up
        '''
        if row-1 <0:                                    #check if move up will take goat outside the board
            return False    
        position = str(row-1) + str(col)                #creates the position variable
        stack_position = self.board.positions[position]
        try:                                            #check if up position is an obstacle. if its empty, stack class will raise exception but we will interpret it as empty space.
            if stack_position.peek() == 'X':
                return False
            else:
                return True 
        except:
            return True                                 #position is empty


    def check_sideways_down(self,row:int,col:int) -> bool:
        '''
        check if the goat can move down
        '''
        if row + 1 >= self.height:                  #check if move down will take goat outside the board
            return False
        position = str(row+1) + str(col)            #creates the position variable
        stack_position = self.board.positions[position]
        try:                                            #check if down position is an obstacle. if its empty, stack class will raise exception but we will interpret it as empty space.
            if stack_position.peek() == 'X':
                return False
            else:
                return True 
        except:
            return True                             #position is empty
        
    def check_forward_step(self,row:int,col:int) -> bool:
        '''
        check if the goat can move forward
        '''
        if col + 1 >= self.width:                #check if move forward will take goat outside the board
            return False
        position = str(row) + str(col+1)         #creates the position variable
        stack_position = self.board.positions[position]
        try:                                     #check if forward position is an obstacle. if its empty, stack class will raise exception but we will interpret it as empty space.
            if stack_position.peek() == 'X':
                return False
            else:
                return True 
        except:
            return True                         #position is empty
        
    def get_top_goat(self, row : int, column : str) -> Goat:
        '''
            Obtains a goat at a specific location
            Inputs:
                - row: the row where the goat will be obtained from
                - column: the column where the goat will be obtained from
            Returns:
                The goat colour at the top of the stack in the specified location
        '''
        position = str(row) + str(column)     #creates the position variable
        stack_position = self.board.positions[position]
        try:
            return stack_position.peek().get_colour()[0].upper()
        except:
            return str(stack_position)
        

    def get_goats_per_player(self) -> List[int]:
        '''Return a list that contains the number of goats per player.'''
        goats_per_player = []
        for player in self.players:                                 #iterate over each player in the game
            goats_per_player.append(player.get_goat_numbers())
        return goats_per_player
        

    def set_phase(self, phase: int) -> None:
        '''Sets the game phase'''
        self.phase = phase

    def set_turn(self, turn: int) -> None:
        '''Sets the game turn'''
        self.turn = turn

    def add_player(self, player: Player) -> None:
        '''Adds a player to the list of players'''
        self.players.append(player)

    def add_goat(self, row: int, column: str) -> None:
        '''Add goat to stack in given location (row, column).
         column is str range of 0 to 8
         '''

        player = self.get_current_player()                          # gets current player 
        row = row-1                                                 # lower the row number by 1
        player.add_goat()                                           # adds goat into player by calling method
        valid = True
        for goat in player.goat:                                    #sets the position of newly added goat
            if goat.get_position() == "-1"and valid: 
                goat.set_position(row,ord(column)-65)
                position = str(row)+str(ord(column)-65)             
                position_stack = self.board.positions[position]     
                position_stack.push(goat)                           #adds the goat into the board
            
                valid = False
                
    def check_starting_goat_placement(self, row: int) -> bool:
        '''Checks that goat is not placed in a high stack'''
        position = str(row-1) + str(0)                                      #creates a position variable
        position_size = self.board.positions[position].size()               #gets stack position size
        inidividual_positions_size = self.get_starting_gate_sizes()         #gets number of goat on the starting gate 
        if position_size <= min(inidividual_positions_size):                #checking if goat is getting placed on the lowest stack
            return True
        else:
            return False
        
    def get_starting_gate_sizes(self) -> List[int]:
        '''
            Returns a list containing how many goats
            are in each row of the starting gate
        '''
        size_list= [] 
        for row in range(self.height):
            position = str(row) + str(0)
            size_list.append(self.board.positions[position].size())
    
        return size_list    

    def move_sideways(self, move) -> None:
        '''Executes sideways move if valid
        move = [(initial_row, initial_column),(final_row, final_column)] 
         '''
       
        try:
            if self.check_sideways_move(move):                                  # can raise exception if move is invalid
                if self.check_same_color(move[0][0]-1,ord(move[0][1])-65):      # minus 1 to calibrate the row to starting 0
                    self.move_goat(move)
                else:
                    raise Exception("Goat on the top is not the same colour")
            else:
                raise Exception('Invalid Move')
        except:
            raise
    

    def check_same_color(self, row: int, column: str) -> None:
        '''
            Checks if the color of the current 
            player and the goat on top coincide
        '''
        player = self.get_current_player()
        if self.get_top_goat(row,column)[0] == player.colour[0].upper():             
            return True
        else:
            return False
        
    def move_goat(self, move: List) -> None:
        '''
            Lets a goat jump in the board
            Inputs:
                - move: list with tuple of initial and final locations
        '''
        initial_position = move[0][1]+ str(move[0][0])
        final_col = ord(move[1][1])-65
        valid = True
        player = self.get_current_player()                      #gets current player
        goats = player.goat                                     #goat list
        while valid:
            for goat in goats:                                  #iterate over each goat 
                if goat.get_position() == initial_position:     #Executes when particular positioned goat is found
                    goat.set_position(move[1][0]-1,final_col)
                    self.update_board_position(move)
                    valid = False
        
    def update_board_position(self,move: List) -> None:
        '''
        update the individual position stacks.
        move = [(initial_row, initial_column),(final_row, final_column)]
        '''
        init_row = move[0][0]-1                                     #indexing from move list
        init_col = ord(move[0][1])-65                               #indexing from move list
        final_row = move[1][0]-1                                    #indexing from move list
        final_col = ord(move[1][1])-65                              #indexing from move list
        
        init_position = str(init_row)+str(init_col)                 #string representation of the position
        final_position = str(final_row)+str(final_col)              #string representation of the position
        final_position_stack = self.board.positions[final_position] # type(self.board.positions) = dict 
        init_position_stack = self.board.positions[init_position]   # type(self.board.positions) = dict
        goat = init_position_stack.pop()                            #pop the goat from the previous position
        final_position_stack.push(goat)                             #adds goat into the forward position
          

    def check_row(self, row: int) -> None:
        '''Checks if a row is valid'''
        try:
            self.board.check_row(row)        
        except:
            raise

    def check_column(self, column: str) -> None:
        '''Checks if a column is valid'''
        try:
            self.board.check_column(column)            
        except:
            raise

    
    def check_sideways_move(self, sideways_move: List[tuple]) -> None:
        '''
        Checks if player can move goat sideways
        Inputs:
         - forward_move: list with tuple of initial and final locations
        '''
        initial_col = ord(sideways_move[0][1])-65
        final_col = ord(sideways_move[1][1])-65

        if initial_col != final_col:                                            #raise exception if move is not in the same column
            raise(Exception("It should be a sideways move."))
        if sideways_move[0][0] - sideways_move[1][0] >=0:                       # execute if move is upwards 
            return self.check_sideways_up(sideways_move[0][0]-1,initial_col)    # minus 1 is to calibrate the row to starting 0
        else:
            return self.check_sideways_down(sideways_move[0][0]-1,initial_col)  #else move is downward
            

    def check_valid_move_format(self, move: List) -> None:
        '''Checks if the given location is an appropriate list of tuples'''
        '''move = [(initial_row, initial_column),(final_row, final_column)] 
        '''
        try:                                                                    #raise exception if move is not valid. Exception will be handled in the engine class
            self.check_row(move[0][0])
            self.check_column(move[0][1])
            self.check_row(move[1][0])
            self.check_column(move[1][1])
        except:
            raise
        
    def move_forward(self, move, dice_outcome) -> None:
        '''Executes forward move if valid
        move = [(initial_row, initial_column),(final_row, final_column)]
        '''
        initial_row = move[0][0]-1    
        initial_col = ord(move[0][1])-65
        try:                                                                   #raises exception if attempted forward position has obstacle
            self.check_forward_move(move,dice_outcome)                         #check forward move by calling forward method
            if self.check_forward_step(initial_row,initial_col) == True:       #execute if player can move forward
                self.move_goat_forward(move)                                   #move the goat
            else:
                raise Exception("Obstacle in the way")                    
        except:
            raise
                
    def check_forward_move(self, forward_move: List, dice_outcome: int) -> None:
        '''
            Checks if player can move goat forward
            Inputs:
                - forward_move: list with tuple of initial and final locations
                - dice_outcome: dice outcome (integer between 1 and 6)
        '''
        initial_row = forward_move[0][0]
        forward_row= forward_move[1][0]
        
        if initial_row != forward_row:                                          #execute if attempted move is not in the same row
            raise Exception("Forward Move should be in the same row")
        if initial_row != dice_outcome:                                         #execute if attempted move's row is not in the same dice outcome
            raise Exception('Forward Move should be in the same row as the dice outcome')
                   
        
    def move_goat_forward(self, move: List) -> None:
        '''
            Lets a goat jump forward in the board
            Inputs:
                - move: list with tuple of initial and final locations
        '''
    
        initial_position = move[0][1]+ str(move[0][0])                          #creates string representation of the position
        board_position = str(int(move[0][0])-1)+ str(ord(move[0][1])-65)        #creates string representation of the position
        final_col = ord(move[1][1])-65                                          #creates string representation of the position
        final_board_position = str(int(move[1][0])-1) + str(final_col)          #creates string representation of the position
        goat = self.board.positions[board_position].pop()                       #access the position stack of the board and pop the top goat
        
        if goat.get_position() == initial_position:                             #verify the top goat's position is same as initial position defined by the user
            goat.set_position(move[1][0]-1,final_col)                           #set the goat position
            self.board.positions[final_board_position].push(goat)               # push the goat into board's position
    
        
    def check_nonempty_row(self, row) -> bool:
        '''this method returns whether the given row has goats that can jump forward or not.'''
        unblocked_goat = 0
        
        for initial_col in range(self.width):                                  #iterate by number of columns
            position = str(row-1)+ str(initial_col)
            position_stack = self.board.positions[position]                    #gets position stack
            if position_stack.size() !=0:                                      #if position is not empty
                if position_stack.peek() != 'X':                               #if position is not an obstacle position
                    if self.check_forward_step(row-1,initial_col):             #check if goat at current position can move forward
                        unblocked_goat +=1                                     #if above condition meets, then increaments the counter
        
        if unblocked_goat != 0:
            return True
        else:
            return False          
    
    
    def check_winner(self) -> bool:
        '''
            Returns whether one player has won by getting 
            the necessary goats to the Destination
        '''
        destination_col = "I"                                                             #final column
        destination_goat_numbers = self.get_goats_destination_per_player(destination_col) #list of the number of the goat of each player in the destination column
        
        if WINNING_NUMBER_GOATS in destination_goat_numbers:
            return True
        else:
            return False
        
    
    def get_goats_destination_per_player(self, destination: str) -> List[int]:
        '''
            Return a list that contains the number 
            of goats per player in the destination.
        '''
        destination_goat_numbers = []
        for player in self.players:                             #iterate over each player
            goats = player.goat                                 #gets goat of the player
            destination_goats = 0
            for goat in goats:
                goat_position = goat.get_position()     
                if goat_position[0] == destination:             #checks if goat position is in the destination column
                    destination_goats += 1                      #increments the counter if condition met
            destination_goat_numbers.append(destination_goats)
        
        return destination_goat_numbers
    
    def check_tie(self) -> bool:
        '''
            Returns whether there is a tie since 
            no player has possible moves
        '''
        tie = False
        blocked_players = 0
        goat_blocked_list = self.get_goats_blocked_per_player()  #returns number of blocked goats per player
        for blocked_goats in goat_blocked_list:                  
            if blocked_goats == GOATS_PER_PLAYER:                #if all the goats are blocked
                blocked_players +=1
        if blocked_players == len(self.players):                #if all player' goats are blocked
            tie = True
            
        return tie
    
    def get_goats_blocked_per_player(self) -> List[int]:
        '''
            Returns a list that contains the number 
            of goats blocked per player.
        '''
        goat_blocked_list = []
        
        for player in self.players:                         #iterate over each player
            blocked_goats = self.get_goats_blocked(player)  #gets blocked goat number
            goat_blocked_list.append(blocked_goats)
            
        return goat_blocked_list
    

    ################################################
    #
    # The following methods do NOT need to be
    # included in your solution, but they might
    # give you an idea of possible useful methods
    # to include.
    # 
    ################################################
  

 
    
    def check_location(self, location) -> None:
        ''' Checks if location is in the board'''

        pass
    
    def check_jump(self, row: int, column: str) -> None:
        '''Checks if available stack to jump'''

        pass
    

if __name__ == '__main__':
    game = Game(9,6,[(4,"C"),(2,'C'),(3,"D"),(1,'B'),(2,'A'),(3,'B'),(4,'A'),(2,'G'),(3,"H"),(4,'G')]) # TEST CASES
    player = Player('White')
    game.add_player(player)
    game.add_goat(1,'A')
    print(game.board) 
    game.add_goat(3,'C')    
    game.add_goat(3,"A")
    print(game.board)
    #game.move_forward([(3,'C'),(3,'D')],3)
    
    #game.move_sideways([(3,'C'),(2,'C')])
    print(game.board)    
    #print(game.get_goats_blocked(player))
    #print(game.check_nonempty_row(3))
    #print(game.check_nonempty_row(1))
    game.add_goat(3,'G')
    print(game.check_winner())
    game.add_goat(3,'I')
    game.add_goat(4,'I')
    game.add_goat(5,'I')
    '''print(game.check_nonempty_row(1))
    game.add_goat(3,"C")
    print(game.board)
    print(game.check_nonempty_row(3))
    game.move_forward([(3,'C'),(3,'D')],3)
    #game.move_sideways([(1,'A'),(0,'A')])
    #print(game.board)
        #game.move_sideways([(3,'C'),(4,'C')])
    #print(game.board)
    #game.move_sideways([(3,'C'),(2,'C')])
    #print(game.board)
    '''
    
    
    