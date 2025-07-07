from rcsa_dev_kit_edu_python_lib.fly_tello import FlyTello
my_tellos = list()


# Check Serial Tello EDU

my_tellos.append('0TQDG6SEDB7WCT')# Drone10


mspeed = 50
mx = 135
my = 140
mz = 100

try :
    with FlyTello(my_tellos) as fly:
        while (True):
            try :
                print ("t=takeoff,l=land,b=battery?,q=exit")
                minput = input("Enter your command : ")
                if minput == 't' :
                    print('Takeoff')
                    fly.takeoff()
                if minput == 'l' :
                    print('Land')
                    fly.land()
                if minput == 'b' :
                    print('Battery?')
                    fly.get_battery()
                if minput == 'q' :
                    print('Exit Program')
                    break
                if minput == '1':
                    print ("Mission1")
                    with fly.sync_these():
                        fly.takeoff(tello=1, sync=True)            
                    
                        
                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=100, speed=70, tello=1, sync=True) 
                       
                   
                    
                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=1, sync=True) 
                        

                   


                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=100, speed=70, tello=1, sync=True) 
                    
                   

                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=1, sync=True) 
                       
                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=100, speed=70, tello=1, sync=True) 
                        
                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=1, sync=True) 
                      
                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=50, speed=70, tello=1, sync=True) 
                        

                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=-50, speed=70, tello=1, sync=True) 
                    

                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=100, speed=70, tello=1, sync=True) 
                        

                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=1, sync=True) 
                        
                   
                   
                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=100, speed=70, tello=1, sync=True) 
                     

        
                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=100, speed=70, tello=1, sync=True) 
                       

                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=-0, speed=70, tello=1, sync=True) 
                        
       
                   
                    with fly.sync_these():
                      
                       fly.land(tello=1, sync=True)
                    


                else :
                    pass
            except KeyboardInterrupt as e:
                break
except KeyboardInterrupt as e:
    fly.Stop()