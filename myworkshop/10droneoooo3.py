from rcsa_dev_kit_edu_python_lib.fly_tello import FlyTello
from rcsa_dev_kit_edu_python_lib.tello import Tello
from rcsa_dev_kit_edu_python_lib.comms_manager import CommsManager
my_tellos = list()


# Check Serial Tello EDU

my_tellos.append('0TQDG7BEDB4BZ6') # Drone1
my_tellos.append('0TQDG7PEDB8F91') # Drone2
my_tellos.append('0TQDG7PEDB4RP7') # Drone3
my_tellos.append('0TQDG7PEDBP5P9') # Drone4
my_tellos.append('0TQDG7PEDBQDR7') # Drone5
my_tellos.append('0TQDG7PEDB62Q9') # Drone6
my_tellos.append('0TQDG7PEDBP34F') # Drone7
my_tellos.append('0TQDG7PEDBM7CS') # Drone8
my_tellos.append('0TQDG7PEDBC030') # Drone9
my_tellos.append('0TQDG6SEDB7WCT') # Drone10

mspeed = 50
mx = 135
my = 140
mz = 100

try :
    with FlyTello(my_tellos) as fly:
        while (True):
            try :
                print ("t=takeoff,l=land,b=battery?,s=speed?,h=height,q=exit")
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
                if minput == 'speed' :
                    print('Speed?')
                    fly.get_speed()
                if minput == 'h' :
                    print('Height')
                    fly.get_height()
                if minput == 'q' :
                    print('Exit Program')
                    break
                if minput == '1':
                    print ("Mission1")
                    with fly.sync_these():
                        fly.takeoff(tello=1)
                        fly.takeoff(tello=2)
                        fly.takeoff(tello=3)
                        fly.takeoff(tello=4)
                        fly.takeoff(tello=5)
                        fly.takeoff(tello=6)
                        fly.takeoff(tello=7)
                        fly.takeoff(tello=8)
                        fly.takeoff(tello=9)
                        fly.takeoff(tello=10)
                       
  
                         
                    
                    
                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=150, speed=70, tello=1, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=2, sync=True) 
                        fly.straight(x=0, y=0, z=250, speed=70, tello=3, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=4, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=5, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=6, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=7, sync=True) 
                        fly.straight(x=0, y=0, z=250, speed=70, tello=8, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=9, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=10, sync=True) 
                        
                   
                    
                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=1, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=2, sync=True) 
                        fly.straight(x=0, y=0, z=-250, speed=70, tello=3, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=4, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=5, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=6, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=7, sync=True) 
                        fly.straight(x=0, y=0, z=-250, speed=70, tello=8, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=9, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=10, sync=True) 
                      
                   


                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=300, speed=70, tello=1, sync=True) 
                        fly.straight(x=0, y=0, z=250, speed=70, tello=2, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=3, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=4, sync=True) 
                        fly.straight(x=0, y=0, z=100, speed=70, tello=5, sync=True) 
                        fly.straight(x=0, y=0, z=100, speed=70, tello=6, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=7, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=8, sync=True) 
                        fly.straight(x=0, y=0, z=250, speed=70, tello=9, sync=True) 
                        fly.straight(x=0, y=0, z=300, speed=70, tello=10, sync=True) 
                        
                   
                   

                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=-300, speed=70, tello=1, sync=True) 
                        fly.straight(x=0, y=0, z=-250, speed=70, tello=2, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=3, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=4, sync=True) 
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=5, sync=True) 
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=6, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=7, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=8, sync=True) 
                        fly.straight(x=0, y=0, z=-250, speed=70, tello=9, sync=True) 
                        fly.straight(x=0, y=0, z=-300, speed=70, tello=10, sync=True) 
                        
                       

                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=100, speed=70, tello=1, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=2, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=3, sync=True) 
                        fly.straight(x=0, y=0, z=250, speed=70, tello=4, sync=True) 
                        fly.straight(x=0, y=0, z=300, speed=70, tello=5, sync=True) 
                        fly.straight(x=0, y=0, z=300, speed=70, tello=6, sync=True) 
                        fly.straight(x=0, y=0, z=250, speed=70, tello=7, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=8, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=9, sync=True) 
                        fly.straight(x=0, y=0, z=100, speed=70, tello=10, sync=True) 
                       

                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=1, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=2, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=3, sync=True) 
                        fly.straight(x=0, y=0, z=-250, speed=70, tello=4, sync=True) 
                        fly.straight(x=0, y=0, z=-300, speed=70, tello=5, sync=True) 
                        fly.straight(x=0, y=0, z=-300, speed=70, tello=6, sync=True) 
                        fly.straight(x=0, y=0, z=-250, speed=70, tello=7, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=8, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=9, sync=True) 
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=10, sync=True) 
                        

                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=150, speed=70, tello=1, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=2, sync=True) 
                        fly.straight(x=0, y=0, z=250, speed=70, tello=3, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=4, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=5, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=6, sync=True) 
                        fly.straight(x=0, y=0, z=100, speed=70, tello=7, sync=True) 
                        fly.straight(x=0, y=0, z=50, speed=70, tello=8, sync=True) 
                        fly.straight(x=0, y=0, z=100, speed=70, tello=9, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=10, sync=True) 
                        

                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=1, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=2, sync=True) 
                        fly.straight(x=0, y=0, z=-250, speed=70, tello=3, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=4, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=5, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=6, sync=True) 
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=7, sync=True) 
                        fly.straight(x=0, y=0, z=-50, speed=70, tello=8, sync=True) 
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=9, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=10, sync=True) 
                        
                        

                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=300, speed=70, tello=1, sync=True) 
                        fly.straight(x=0, y=0, z=250, speed=70, tello=2, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=3, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=4, sync=True) 
                        fly.straight(x=0, y=0, z=100, speed=70, tello=5, sync=True) 
                        fly.straight(x=0, y=0, z=300, speed=70, tello=6, sync=True) 
                        fly.straight(x=0, y=0, z=250, speed=70, tello=7, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=8, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=9, sync=True) 
                        fly.straight(x=0, y=0, z=100, speed=70, tello=10, sync=True) 
                        
                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=-300, speed=70, tello=1, sync=True) 
                        fly.straight(x=0, y=0, z=-250, speed=70, tello=2, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=3, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=4, sync=True) 
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=5, sync=True) 
                        fly.straight(x=0, y=0, z=-300, speed=70, tello=6, sync=True) 
                        fly.straight(x=0, y=0, z=-250, speed=70, tello=7, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=8, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=9, sync=True) 
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=10, sync=True) 
                        
                   
            
                    
                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=100, speed=70, tello=1, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=2, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=3, sync=True) 
                        fly.straight(x=0, y=0, z=250, speed=70, tello=4, sync=True) 
                        fly.straight(x=0, y=0, z=300, speed=70, tello=5, sync=True) 
                        fly.straight(x=0, y=0, z=100, speed=70, tello=6, sync=True) 
                        fly.straight(x=0, y=0, z=150, speed=70, tello=7, sync=True) 
                        fly.straight(x=0, y=0, z=200, speed=70, tello=8, sync=True) 
                        fly.straight(x=0, y=0, z=250, speed=70, tello=9, sync=True) 
                        fly.straight(x=0, y=0, z=300, speed=70, tello=10, sync=True) 
                       


                    with fly.sync_these():
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=1, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=2, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=3, sync=True) 
                        fly.straight(x=0, y=0, z=-250, speed=70, tello=4, sync=True) 
                        fly.straight(x=0, y=0, z=-300, speed=70, tello=5, sync=True) 
                        fly.straight(x=0, y=0, z=-100, speed=70, tello=6, sync=True) 
                        fly.straight(x=0, y=0, z=-150, speed=70, tello=7, sync=True) 
                        fly.straight(x=0, y=0, z=-200, speed=70, tello=8, sync=True) 
                        fly.straight(x=0, y=0, z=-250, speed=70, tello=9, sync=True) 
                        fly.straight(x=0, y=0, z=-300, speed=70, tello=10, sync=True)
                        
                    
                    with fly.sync_these():
                        fly.land(tello=1)
                        fly.land(tello=2)
                        fly.land(tello=3)
                        fly.land(tello=4)
                        fly.land(tello=5)
                        fly.land(tello=6)
                        fly.land(tello=7)
                        fly.land(tello=8)
                        fly.land(tello=9)
                        fly.land(tello=10)
                   
                    


                else :
                    pass
            except KeyboardInterrupt as e:
                break
except KeyboardInterrupt as e:
    fly.Stop()