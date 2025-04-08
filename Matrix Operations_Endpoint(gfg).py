def findindex(target,matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == target:
        return (i,j)  
        
def swap_dir(d):
  if d == "right":
    return "down"
  elif d == "down":
    return "left"
  elif d == "left":
    return "up"
  elif d == "up":
    return "right"
    
cur_dir = "right"
moving = True
while moving:
  value = matrix[0][0]
  if value == "0":

                     
                
                if d == "right":
                return lis
            elif d == "down":
                return "left"
            elif d == "left":
                return "up"
            elif d == "up":
                return "right"
