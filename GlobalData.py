import pygame

# vehicle typpes
CAR:str = 'car'
BUS:str = 'bus'
TRUCK:str = 'truck'
MOTORCYCLE:str = 'motorcycle'

# directions
RIGHT:str = 'right'
LEFT:str = 'left'
UP :str= 'up'
DOWN :str= 'down'



# Lanes
#Right direction lanes
CD = 0
IJ = 1
KL = 2
ST= 3
QR = 4
WX = 5

#Down direction lanes
A_I_ = 0
D_F_ = 1
J_Q_ = 2
L_N_ = 3
R_W_= 4
T_V_ = 5

#Left direction lanes
BA = 0
FE = 1
HG = 2
NM = 3
PO = 4
VU = 5

#Up direction lanes
E_C_ = 0
G_B_ = 1
M_K_ = 2
O_H_ = 3
X_P_ = 4
U_S_ = 5

# overall vehicles per lane
#lanes_quantity= [[0 for _ in range(6)] for _ in range(4)]
lanes_quantity = {
     RIGHT:[0,0,0,0,0,0],
     DOWN :[0,0,0,0,0,0],
     LEFT :[0,0,0,0,0,0],
     UP   :[0,0,0,0,0,0]
}
#lanes_quantity= [[ streets[direction][lane][] for lane in range(6)] for direction in range(4)]
# LOOK IN DESIG FILE
points = {
     'A' : { 'x' : 175 , 'y' : 0 },
     'B' : { 'x' : 360 , 'y' : 0 },

     'C' : { 'x' : 175 , 'y' : 175 },
     'D' : { 'x' : 360 , 'y' : 175 },

     'E' : { 'x' : 200 , 'y' : 280 },
     'F' : { 'x' : 335 , 'y' : 280 },
     'G' : { 'x' : 480 , 'y' : 280 },
     'H' : { 'x' : 620 , 'y' : 280 },

     'I' : { 'x' : 175 , 'y' : 365 },
     'J' : { 'x' : 360 , 'y' : 365 },
     'K' : { 'x' : 625 , 'y' : 365 },
     'L' : { 'x' : 825 , 'y' : 365 },

     'M' : { 'x' : 625  , 'y' : 570 },
     'N' : { 'x' : 825  , 'y' : 570 },
     'O' : { 'x' : 770  , 'y' : 570 },
     'P' : { 'x' : 915 , 'y' : 570 },

     'Q' : { 'x' : 770 , 'y' : 555 },
     'R' : { 'x' : 825 , 'y' : 555 },
     'S' : { 'x' : 770 , 'y' : 555 },
     'T' : { 'x' : 905 , 'y' : 555 },

     'U' : { 'x' : 770 , 'y' : 620 },
     'V' : { 'x' : 905 , 'y' : 620 },

     'W' : { 'x' : 770 , 'y' : 870 },
     'X' : { 'x' : 905 , 'y' : 870 },



     'A_' : { 'x' : 100 , 'y' : 90 },
     'B_' : { 'x' : 410 , 'y' : 90 },

     'C_' : { 'x' : 130 , 'y' : 90 },
     'D_' : { 'x' : 385 , 'y' : 90 },

     'E_' : { 'x' : 130 , 'y' : 240 },
     'F_' : { 'x' : 160 , 'y' : 240 },
     'G_' : { 'x' : 190 , 'y' : 240 },
     'H_' : { 'x' : 950 , 'y' : 240 },

     'I_' : { 'x' : 100 , 'y' : 365 },
     'J_' : { 'x' : 500 , 'y' : 365 },
     'K_' : { 'x' : 625 , 'y' : 365 },
     'L_' : { 'x' : 825 , 'y' : 365 },

     'M_' : { 'x' : 625  , 'y' : 430 },
     'N_' : { 'x' : 825  , 'y' : 430 },
     'O_' : { 'x' : 950  , 'y' : 430 },
     'P_' : { 'x' : 1275 , 'y' : 430 },

     'Q_' : { 'x' : 500 , 'y' : 555 },
     'R_' : { 'x' : 825 , 'y' : 555 },
     'S_' : { 'x' : 950 , 'y' : 555 },
     'T_' : { 'x' : 1150 , 'y' : 555 },

     'U_' : { 'x' : 950 , 'y' : 620 },
     'V_' : { 'x' : 1150 , 'y' : 620 },

     'W_' : { 'x' : 825 , 'y' : 745 },
     'X_' : { 'x' : 1275 , 'y' : 745 }
}


street_class = {
     RIGHT:0,
     DOWN:1,
     LEFT:2,
     UP:3
}
#lane_number = 

streets = {
     
     RIGHT:{         # RIGHT
          CD:{
               'x':[points['C']['x'] , points['D']['x']],
               'y':[points['C']['y'] , points['D']['y']] # y max
          },
          IJ:{
               'x':[points['I']['x'] , points['J']['x']],
               'y':[points['I']['y'] , points['J']['y']]
          },
          KL:{
               'x':[points['K']['x'] , points['L']['x']],
               'y':[points['K']['y'] , points['L']['y']]
          },
          ST:{
               'x':[points['S']['x'] , points['T']['x']],
               'y':[points['S']['y'] , points['T']['y']]
          },
          QR:{
               'x':[points['Q']['x'] , points['R']['x']],
               'y':[points['Q']['y'] , points['R']['y']]
          }
          ,
          WX:{
               'x':[points['W']['x'] , points['X']['x']],
               'y':[points['W']['y'] , points['X']['y']]
          }
     },
     LEFT:{         # LEFT
          BA:{
               'x':[points['B']['x'] , points['A']['x']],
               'y':[points['B']['y'] , points['A']['y']]
          },
          FE:{
               'x':[points['F']['x'] , points['E']['x']],
               'y':[points['F']['y'] , points['E']['y']]
          },
          HG:{
               'x':[points['H']['x'] , points['G']['x']],
               'y':[points['H']['y'] , points['G']['y']]
          },
          NM:{
               'x':[points['N']['x'] , points['M']['x']],
               'y':[points['N']['y'] , points['M']['y']]
          },
          PO:{
               'x':[points['P']['x'] , points['O']['x']],
               'y':[points['P']['y'] , points['O']['y']]
          },
          VU:{
               'x':[points['V']['x'] , points['U']['x']],
               'y':[points['V']['y'] , points['U']['y']]
          }
     },
     UP:{         # UP
          E_C_:{
               'x':[points['E_']['x'] , points['C_']['x']],
               'y':[points['E_']['y'] , points['C_']['y']]
          },
          G_B_:{
               'x':[points['G_']['x'] , points['B_']['x']],
               'y':[points['G_']['y'] , points['B_']['y']]
          },
          M_K_:{
               'x':[points['M_']['x'] , points['K_']['x']],
               'y':[points['M_']['y'] , points['K_']['y']]
          },
          O_H_:{
               'x':[points['O_']['x'],points['H_']['x']],
               'y':[points['O_']['y'],points['H_']['y']]
          },
          X_P_:{
               'x':[points['X_']['x'],points['P_']['x']],
               'y':[points['X_']['y'],points['P_']['y']]
          },
          U_S_:{
               'x':[points['U_']['x'],points['S_']['x']],
               'y':[points['U_']['y'],points['S_']['y']]
          }
     },
     DOWN:{         # DOWN
          A_I_:{
               'x':[points['A_']['x'],points['I_']['x']],
               'y':[points['A_']['y'],points['I_']['y']]
          },
          D_F_:{
               'x':[points['D_']['x'],points['F_']['x']],
               'y':[points['D_']['y'],points['F_']['y']]
          },
          J_Q_:{
               'x':[points['J_']['x'],points['Q_']['x']],
               'y':[points['J_']['y'],points['Q_']['y']]
          },
          L_N_:{
               'x':[points['L_']['x'],points['N_']['x']],
               'y':[points['L_']['y'],points['N_']['y']]
          },
          R_W_:{
               'x':[points['R_']['x'],points['W_']['x']],
               'y':[points['R_']['y'],points['W_']['y']]
          },
          T_V_:{
               'x':[points['T_']['x'],points['V_']['x']],
               'y':[points['T_']['y'],points['V_']['y']]
          }
     }
}



# define for each  'maslol'  it ' netev ' number
# random :select direction {R,L,U,D}
# select street vector .For EX: AI
# Random : select 'netev' number in choosen street vector



# Font Size
font_size:int = 30

# Colours
black = (0, 0, 0)
white = (255, 255, 255)

# Screensize
screen_width:int = 1100
screen_height:int = 900 #800
screen_size = (screen_width, screen_height)

# Loading signal images and font
#ronen change all image type to be with the image name , like this
red_signal_img= pygame.image.load('images/signals/red.png')
yellow_signal_img = pygame.image.load('images/signals/yellow.png')
green_signal = pygame.image.load('images/signals/green.png')
non_signal = pygame.image.load('images/signals/non.png')
background = pygame.image.load('images/street_900.png')
background_white = pygame.image.load('images/bg-white.png')


# Default values of signal times
default_red :int = 150
default_yellow:int = 3
default_green:int = 20
default_minimum:int = 10
default_maximum:int = 60

signals =[]
number_of_signals :int = 4
sim_time :int = 300       # change this to change time of simulation
time_elapsed :int = 0

current_green :int = 0   # Indicates which signal is green
next_green :int = (current_green + 1) % number_of_signals
current_yellow :int = 0   # Indicates whether yellow signal is on or off

# Average times for vehicles to pass the intersection
car_time :int = 2
motorcycle_time :int = 1
bus_time :float = 2.5
truck_time :float = 2.5

# Count of cars at a traffic signal
number_of_cars :int= 0
number_of_buses:int = 0
number_of_trucks :int= 0
number_of_motorcycle:int = 0
number_of_lanes:int = 2


# Red signal time at which cars will be detected at a signal
detection_time:int = 5

speeds:dict = {CAR: 2.25, BUS: 1.8, TRUCK: 1.8,
          MOTORCYCLE: 2.5}  # average speeds of vehicles


# Coordinates of start
# x = direction : lane <- { 0 , 1 , 2 }
"""
x = {RIGHT: [0, 0, 0], DOWN: [755, 727, 697],
     LEFT: [1400, 1400, 1400], UP: [602, 627, 657]}
y = {RIGHT: [348, 370, 398], DOWN: [0, 0, 0],
     LEFT: [498, 466, 436], UP: [800, 800, 800]}

z = 66
x:dict = {RIGHT: [0, 0, 0], DOWN: [755-z-245, 727-z-245, 697-z-245],
     LEFT: [1400, 1400, 1400], UP: [602+z, 627+z, 657+z]}
y:dict = {RIGHT: [348+z, 370+z, 398+z], DOWN: [0, 0, 0],
     LEFT: [498-z, 466-z, 436-z], UP: [800, 800, 800]}

"""
vehicles:dict = {RIGHT: {0: [], 1: [], 2: [], 'crossed': 0}, DOWN: {0: [], 1: [], 2: [], 'crossed': 0},
            LEFT: {0: [], 1: [], 2: [], 'crossed': 0}, UP: {0: [], 1: [], 2: [], 'crossed': 0}}
#vehicleTypes = {0: CAR, 1: BUS, 2: TRUCK, 3: 'rickshaw', 4: MOTORCYCLE}


vehicles_ = {
     
     RIGHT:{         # RIGHT
          CD:
               []
          ,
          IJ:
              []
          ,
          KL:
               []
          ,
          ST:
              []
          ,
          QR:
               []
          
          ,
          WX:
              []
          
          ,'crossed': 0
     },
     LEFT:{         # LEFT
          BA:
              []
          ,
          FE:
              []
          ,
          HG:
               []
          ,
          NM:
              []
          ,
          PO:
               []
          ,
          VU:
               []
          
          ,'crossed': 0
     },
     UP:{         # UP
          E_C_:
              []
          ,
          G_B_:
               []
          ,
          M_K_:
               []
          ,
          O_H_:
               []
          ,
          X_P_:
              []
          ,
          U_S_:
               []
          
          ,'crossed': 0
     },
     DOWN:{         # DOWN
          A_I_:
             []
          ,
          D_F_:
               []
          ,
          J_Q_:
               []
          ,
          L_N_:
              []
          ,
          R_W_:
              []
          ,
          T_V_:
               []
          
          ,'crossed': 0
     }
}





vehicles_generating:dict = {
     5: CAR,
     4: BUS, 
     2: TRUCK, 
     5: MOTORCYCLE
     }


vehicle_types:dict = {
     0: CAR,
     1: BUS, 
     2: TRUCK, 
     3: MOTORCYCLE
     }
     
vehicles_weight = {
     MOTORCYCLE: 1,
     CAR: 4,
     TRUCK: 8,
     BUS: 20
     } 
direction_numbers = {0: RIGHT, 1: DOWN, 2: LEFT, 3: UP}

# Coordinates of signal image, timer, and vehicle count
signal_coordinates:list = [(350, 358), (350, 230), (440, 230), (440, 358)]
signal_timer_coordinates:list = [(355, 338), (355, 210), (445, 210), (445, 338)]
vehicle_count_coordinates:list = [(325, 338), (325, 210), (475, 210), (475, 338)]
vehicle_count_texts:list = ["0", "0", "0", "0"]

# Coordinates of stop lines
stop_lines:dict = {RIGHT: 590, DOWN: 330, LEFT: 800, UP: 535}
default_stop:dict = {RIGHT: 580, DOWN: 320, LEFT: 810, UP: 545}
stops:dict = {RIGHT: [580, 580, 580], DOWN: [320, 320, 320],
         LEFT: [810, 810, 810], UP: [545, 545, 545]}

mid:dict = {RIGHT: {'x': 705, 'y': 445}, DOWN: {'x': 695, 'y': 450},
       LEFT: {'x': 695, 'y': 425}, UP: {'x': 695, 'y': 450}}

rotate_factor = 70
directly = {RIGHT: {'x': 705-rotate_factor, 'y': 445}, DOWN: {'x': 695, 'y': 450-rotate_factor},
            LEFT: {'x': 695+rotate_factor - 20, 'y': 425}, UP: {'x': 695, 'y': 400+rotate_factor}}
   

rotation_angle = 3

# Gap between vehicles
gap = 15   # stopping gap
gap2 = 15   # moving gap
