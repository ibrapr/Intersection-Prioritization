import threading
import pygame
import Simulation as sim
import sys
import GlobalData as GD

def run_thread(thread_name:str , thread_target,args=()):
    thread = threading.Thread(name=thread_name, target=thread_target, args=args)
    thread.daemon = True
    thread.start()
    return thread





screen = pygame.display.set_mode(GD.screen_size)
pygame.display.set_caption("SIMULATION")
font = pygame.font.Font(None, GD.font_size)

def turn_signal_on(intersection :int, signal_img, index:int):
    screen.blit(signal_img, GD.intersections[intersection].signal_coordinates[index])




def display_signal_timer_and_vehicle_count_for_each_signal(intersection :int, signal_number:int , signal_texts : list ):
        signal_texts[signal_number] = font.render(str(GD.intersections[intersection].signals[signal_number].signal_text), True, GD.white, GD.black)
        screen.blit(signal_texts[signal_number], GD.intersections[intersection].signal_timer_coordinates[signal_number])
        
        displayText = GD.crossed[intersection][GD.direction_numbers[signal_number]]['crossed']
        #displayText = GD.vehicles_[GD.direction_numbers[signal_number]]['crossed']
        GD.intersections[intersection].vehicle_count_texts[signal_number] = font.render(str(displayText), True, GD.black, GD.white)
        screen.blit(GD.intersections[intersection].vehicle_count_texts[signal_number], GD.intersections[intersection].vehicle_count_coordinates[signal_number])
        

def display_the_vehicles():
    for vehicle in sim.simulation:
        screen.blit(vehicle.current_image, [vehicle.x, vehicle.y])
        vehicle.move_()


def display_time_elapsed():
    time_elapsed_text = font.render(("Time Elapsed: " + str(GD.time_elapsed)), True, GD.black, GD.white)
    screen.blit(time_elapsed_text, (800, 50))

def signals_conroller(intersection):
            traffic_sign_arrow_images = []

            for dir in GD.direction_numbers.values():
                traffic_sign_arrow_images.append(pygame.image.load(f'images/traffic_signs/{dir}.png'))
            
            for i,coordinate in enumerate(GD.intersections[intersection].traffic_sign_arrow_coordinates):
                screen.blit(traffic_sign_arrow_images[i], (coordinate[0], coordinate[1]))



            for i in range(0, GD.intersections[intersection].number_of_signals):
                if(i == GD.intersections[intersection].current_green):
                    if(GD.intersections[intersection].current_yellow == 1):
                        GD.intersections[intersection].signals[i].signal_text = GD.intersections[intersection].signals[i].yellow
                        turn_signal_on(intersection ,signal_img=GD.yellow_signal_img, index=i)

                        
                    else:
                        GD.intersections[intersection].signals[i].signal_text = GD.intersections[intersection].signals[i].green
                        if(GD.intersections[intersection].signals[i].green <= 6 and GD.intersections[intersection].signals[i].green > 0 and GD.intersections[intersection].signals[i].green % 2 == 0):
                            turn_signal_on(intersection ,signal_img = GD.non_signal, index=i)
                            
                        elif(GD.intersections[intersection].signals[i].green <= 6 and GD.intersections[intersection].signals[i].green > 0 and GD.intersections[intersection].signals[i].green % 2 == 1):
                            turn_signal_on(intersection ,signal_img = GD.green_signal, index=i)
                        
                        else :
                            turn_signal_on(intersection ,signal_img = GD.green_signal, index=i)
        
                else:
                    if(GD.intersections[intersection].signals[i].red <= 10):
                        GD.intersections[intersection].signals[i].signal_text = GD.intersections[intersection].signals[i].red 
                    else:
                        GD.intersections[intersection].signals[i].signal_text = ""
                    turn_signal_on(intersection , signal_img = GD.red_signal_img, index=i)
                

            signal_texts = ["", "", "", ""]
            for i in range(0, GD.intersections[intersection].number_of_signals):
                display_signal_timer_and_vehicle_count_for_each_signal(intersection ,signal_number = i , signal_texts = signal_texts)


class Main:
    #########################################################################################################################
    ####################################################    Threads   #######################################################
    #########################################################################################################################
    run_thread(thread_name="simulationTime" ,thread_target=sim.simulation_time)
    run_thread("initialization" ,sim.initialize)
    run_thread("generateVehicles" ,sim.generate_vehicle)

    cars_number:int = 0
    for v in GD.vehicles_generating.values():
        cars_number += v
    GD.cars_number = cars_number


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    #########################################################################################################################
    #######################################      Display Background In Simulation     #######################################
    #########################################################################################################################
        screen.blit(GD.background_white, (0, 0))  
        screen.blit(GD.background, (150, 0))   
        #mouse coordination
        mousex, mousey = pygame.mouse.get_pos()
        print(f"{mousex} , {mousey}")

    #########################################################################################################################
    #######################################  display signal and set timer according   #######################################
    #######################################  to current status: green, yello, or red  #######################################
    #########################################################################################################################
        run_thread(thread_name="FGKJ signals_conroller" ,thread_target=signals_conroller,args=(GD.FGKJ,)).join()
        run_thread(thread_name="NOSR signals_conroller" ,thread_target=signals_conroller,args=(GD.NOSR,)).join()
       
        
        display_time_elapsed()

        display_the_vehicles()
        pygame.display.update()
    
