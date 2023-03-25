#----------------------------------------------------
# Board implementation
#----------------------------------------------------

from .stack import Stack
from .goat import Goat


class Board:
    '''
    An object in this class represents a board configuration in the game Goat Race.
    '''
    def __init__(self, width, height,obstacle_positions):
        if width != 9 or height != 6:                       #raises exception if height or width doesn't match with the requirement
            raise Exception("Invalid Dimensions")
        self.width = int(width)                             #initialize the width of the board
        self.height = int(height)                           #initialize the height of the board
        self.obstacle = obstacle_positions                  #initialize the board with the obstacles provided
        self.positions = {}                                 #creates a dictionary. Each position on the board is a stack.
        for row in range(self.height):
            for col in range(self.width):
                position = str(row) + str(col)             #creates position name like '00'
                self.positions[position] = Stack()         #set each position value as a stack object

    def check_row(self,row:int)-> bool:
        '''
        Checks if the given value for the row is valid, else raise exception
        '''
        if row >= 1 or row <= self.height:              
            return True
        else:            
            raise Exception("Invalid Row")
    
    def check_column(self, column:str) -> bool:
        '''
        Checks if the given value for the column is valid, else raise exception
        '''
        if column in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
            return True
        else:            
            raise Exception("Invalid Column")
    
    def check_obstacle_positions(self, obstacle_positions:list) -> bool:
        '''
        Checks that the given list of obstacles has valid rows and columns for each obstacle.
        '''
        for obstacle in self.obstacle:
            try:
                self.check_row(obstacle[0])
                self.check_column(obstacle[1])
            except:
                raise Exception("Invalid obstacle position")
            
        return True
    
    def obstacle_positions_list(self)-> None:
        '''
        adds "X" for each obstacle on the position in the board
        '''        
        if self.check_obstacle_positions(self.obstacle) == True:                    # checks if all the obstacles are valid
            for obstacle in self.obstacle:
                position = str(obstacle[0]-1) + str(ord(obstacle[1].upper())-65)    # recalibrate each given position to str(int) e.g. "(1,A)" to "00"
                value = self.positions[position]
                value.push('X')                                                     # push "X" to the stack
    
    def get_width(self):
        '''
        returns the width of the board
        '''
        
        return self.width
    
    def get_height(self):
        '''
        returns the height of the board
        '''
        return self.height
    
    
    def get_board(self)-> list:
        '''
        returns the 2D list of Stack objects representing the board
        '''
        self.obstacle_positions_list()                               #Calls the function to insert "X" for each obstacle position
        main_list = []
        
        for row in range(self.height):
            inner_list = []
            for col in range(self.width):
                position = str(row) + str(col)                        #creates each position index
                value = self.positions[position]                      #gets the position object which defined as a stack
                try:                                                  #try to peek position object. if its empty, stack class will raise exception which would be interpret as a empty space
                    if value.peek() == "X":
                        inner_list.append(value.peek())
                    else:
                        inner_list.append(value.peek().get_colour()[0].upper()) #if position object is not empty, it will push the top goat colour into 2-D list
                except:
                    inner_list.append(str(value))         #str representation of stack object is '' if its empty            
            main_list.append(inner_list)
        
        return main_list
    
    def __str__(self)-> str:
        '''
        returns a string representation of the board
        '''
        line = ''                                           #Main string that will be updated to include everything
        separator = " "+("+"+('-'*3))*self.width+"+"
        i = 0
        j= 1
       
        if i==0:                                           #skip to add empty space on the first run      
            line += '  '
            i = i+1
        if i>0:                                             #writes the header of the board
            while i <= self.width:
                line += '{:>4s}'.format(chr(i+64))
                i = i +1
            line += "\n"                                    #adds new line character
    
        line += separator                                   #adds the separator
        line += '\n'                                        #adds new line character
        board_list = self.get_board()                       #gets the 2-D representation of the board
             
        for row in range(len(board_list)):                  #Iterate over the 2-D
            line1 = ''                                      #creates line1 string
            line1 += str(j)                                 #adds number of each line
            for col in range(len(board_list[row])):         #Iterate over each list of nested list
                line1 += "|"+'{:^3s}'.format(board_list[row][col] if len(board_list[row][col]) != 0 else " ") # adds each value from list to line1 
                
                       
            line1 += "|\n"                                  #add new line character
            line1 += separator                              #add separator line
            line1 += "\n"                                   #add new line character
            j +=1                                           #increament the j by 1
            line += line1                                   # add line1 to line(which is the main line representation of the board)

        return line                                         #return the str representation of the board
            
                
if __name__ == '__main__':
    board = Board(9,6,[(2,'A'),(2,'B'),(4,'C')])            #TEST CASES 
    print(board)
        
                
        
    


