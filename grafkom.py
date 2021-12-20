from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import randint


width, height = 500, 500                               # window size
field_width, field_height = 50, 50                     # internal resolution
snake = [(20, 20)] # snake list of (x, y) positions
snake_dir = (1, 0) # snake movement direction
interval = 200 # update interval in milliseconds
food = [] # food list of type (x, y)

def refresh2d_custom(width, height, internal_width, internal_height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, internal_width, 0.0, internal_height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
   
def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle
   
def draw():                                            # draw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d_custom(width, height, field_width, field_height)
   
    # TODO draw things
   
    glutSwapBuffers()                                  # important for double buffering

def draw_snake():
    glColor3f(1.0, 1.0, 1.0)  # set color to white
    for x, y in snake:        # go through each (x, y) entry
        draw_rect(x, y, 1, 1) # draw it at (x, y) with width=1 and height=1

def draw():                                            # draw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d_custom(width, height, field_width, field_height)
   
    draw_snake()                                       # draw the snake
   
    glutSwapBuffers()                                  # important for double bufferin


def vec_add(p1, p2):
    (x1, y1), (x2, y2)=p1, p2
    return (x1 + x2, y1+y2)
new_pos = vec_add(snake[0], snake_dir)           

def controller(key, x, y):
    global snake_dir
    
    if key == GLUT_KEY_UP:
        snake_dir = (0, 1)
    if key == GLUT_KEY_DOWN:
        snake_dir = (0, -1)
    if key == GLUT_KEY_LEFT:
        snake_dir = (-1, 0)
    if key == GLUT_KEY_RIGHT:
        snake_dir = (1, 0)
        

def update(value):  
    # move snake      
    snake.insert(0, vec_add(snake[0], snake_dir))      
    snake.pop()                                        
   
# let the snake eat the food
    (hx, hy) = snake[0]          # get the snake's head x and y position
    for x, y in food:            # go through the food list
        if hx == x and hy == y:  # is the head where the food is?
            snake.append((x, y)) # make the snake longer
            food.remove((x, y))  # remove the food
   
    # spawn food
    r = randint(0, 20)                                
    if r == 0:
        x, y = randint(0, field_width), randint(0, field_height) 
        food.append((x, y))
   
    glutTimerFunc(interval, update, 0)                 

def draw_food():
    glColor3f(0.5, 0.5, 1.0)  # set color to blue
    for x, y in food:         # go through each (x, y) entry
        draw_rect(x, y, 1, 1) # draw it at (x, y) with width=1 and height=1

def draw():                                            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()                                  
    refresh2d_custom(width, height, field_width, field_height)
   
    draw_food()                                      
    draw_snake()                                       
   
    glutSwapBuffers()                                  

(hx, hy) = snake[0]          
for x, y in food:            
    if hx == x and hy == y:  
        snake.append((x, y))
        food.remove((x, y)) 

# initialization
glutInit()                                             
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                     
glutInitWindowPosition(0, 0)                           
glutCreateWindow("Hungry Snake")              
glutDisplayFunc(draw)                                 
glutIdleFunc(draw)                                    
glutTimerFunc(interval, update, 0)                       
glutSpecialFunc(controller)                       
glutMainLoop()
