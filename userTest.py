import pygame,sys
from ant import Ant

instructions = input("Enter the sequene with L and R \n")

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Langton\'s Ant')
window_icon = pygame.image.load('Icon.png').convert()
pygame.display.set_icon(window_icon)

gridimg = pygame.image.load('Grid.PNG').convert()

running = True

grid = []

for i in range(0,100):
  t=[]
  for j in range(0,100):
    t.append(0)
  grid.append(t)

ant = Ant(50,50,1,0)

turn = 0

while running:

  
  print(turn)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False

  if(turn == len(instructions)):
      turn=0

  ch = instructions[turn]
  if(ch=='L'):
    ant.rotatecw()
    grid[ant.gridx][ant.gridy] = 1
    ant.gridx += ant.dir.x
    ant.gridy += ant.dir.y
  else:
    ant.rotateccw()
    grid[ant.gridx][ant.gridy] = 1
    ant.gridx += ant.dir.x
    ant.gridy += ant.dir.y


  
  screen.blit(gridimg,(0,0)) 
  
  for i in range(0,100):
    for j in range(0,100):
      if int(grid[i][j]) == 0:
            pygame.draw.rect(screen,(0,0,0),pygame.Rect(i*10,j*10,10,10))
      else:
            pygame.draw.rect(screen,(255,0,0),pygame.Rect(i*10,j*10,10,10))
  
  pygame.display.flip()
  
  turn+=1
  #pygame.time.delay(300)
  
  pygame.display.update()
  

print('Game has been exited')