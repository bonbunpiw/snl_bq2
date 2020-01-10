import math
class Maze:
  def __init__(self):
    return

  step = 0
  matrix = [
    [0,0,0,1],
    [0,1,1,0],
    [0,0,1,0],
    [1,0,0,0],
    [0,1,0,0],
  ]
  
  path = []
  blocked = []

  def can_exit(self):

    m = len(self.matrix)
    n = len(self.matrix[0])

    if(self.matrix[0][0]==1):
      print('false')
      return
    if(self.matrix[m-1][n-1]==1):
      print('false')
      return
    
    current = [0,0]
    self.look_around(current)

    return 

  def look_around(self, current):
    self.step = self.step + 1

    m = len(self.matrix)
    n = len(self.matrix[0])

    pos_top = self.get_pos([current[0]-1, current[1]])
    pos_right = self.get_pos([current[0], current[1]+1])
    pos_bottom = self.get_pos([current[0]+1, current[1]])
    pos_left = self.get_pos([current[0], current[1]-1])
    
    bottom = -1
    if(pos_bottom != -1):
      bottom = self.matrix[pos_bottom[0]][pos_bottom[1]]

    right = -1
    if(pos_right != -1):
      right = self.matrix[pos_right[0]][pos_right[1]]

    left = -1
    if(pos_left != -1):
      left = self.matrix[pos_left[0]][pos_left[1]]

    top = -1
    if(pos_top != -1):
      top = self.matrix[pos_top[0]][pos_top[1]]

    move = -1
    if(bottom == 0):
      move = [pos_bottom[0],pos_bottom[1]]
    elif(right == 0):
      move = [pos_right[0],pos_right[1]]
    elif(left == 0):
      move = [pos_left[0],pos_left[1]]
    elif(top == 0):
      move = [pos_top[0],pos_top[1]]
    else:
      print('false')
      return
    
    if(move in self.path):
      self.blocked.append(current)
    
    print(current)
    current = move
    
    if(current[0]==m-1 and current[1] == n-1 and self.matrix[current[0]][current[1]] == 0):
      print(current)
      print('true')
      return
    else:
      self.path.append(current)
      if(self.step < math.pow(m,n)):
        self.look_around(current)

    return

  def get_pos(self, current):
    m = len(self.matrix)
    n = len(self.matrix[0])

    x = current[0]
    y = current[1]

    
    if(x>=0 and y>=0 and x<m and y<n and not ([x, y] in self.blocked)):
      return [x, y]
    return -1

maze = Maze()
result = maze.can_exit()
