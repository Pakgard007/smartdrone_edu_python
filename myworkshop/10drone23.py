from rcsa_dev_kit_edu_python_lib.fly_tello import FlyTello
my_tellos = list()
import socket
import threading
import time
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
                        fly.up(dist=100, tello=1,sync=True)
                        fly.up(dist=100, tello=2,sync=True)
                        fly.up(dist=100, tello=3,sync=True)
                        fly.up(dist=100, tello=4,sync=True)
                        fly.up(dist=100, tello=5,sync=True)
                        fly.up(dist=10, tello=6,sync=True)
                        fly.up(dist=10, tello=7,sync=True)
                        fly.up(dist=10, tello=8,sync=True)
                        fly.up(dist=10, tello=9,sync=True)
                        fly.up(dist=10, tello=10,sync=True)
                   
                    with fly.sync_these():
                        fly.stop(tello=1)
                        fly.stop(tello=2)
                        fly.stop(tello=3)
                        fly.stop(tello=4)
                        fly.stop(tello=5)
                        fly.stop(tello=6)
                        fly.stop(tello=7)
                        fly.stop(tello=8)
                        fly.stop(tello=9)
                        fly.stop(tello=10)

                    with fly.sync_these():
                        fly.right(dist=60, tello=1,sync=True)
                        fly.right(dist=60, tello=2,sync=True)
                        fly.right(dist=60, tello=3,sync=True)
                        fly.right(dist=60, tello=4,sync=True)
                        fly.right(dist=60, tello=5,sync=True)
                        fly.left(dist=60, tello=6,sync=True)
                        fly.left(dist=60, tello=7,sync=True)
                        fly.left(dist=60, tello=8,sync=True)
                        fly.left(dist=60, tello=9,sync=True)
                        fly.left(dist=60, tello=10,sync=True)

                    with fly.sync_these():
                        fly.stop(tello=1)
                        fly.stop(tello=2)
                        fly.stop(tello=3)
                        fly.stop(tello=4)
                        fly.stop(tello=5)
                        fly.stop(tello=6)
                        fly.stop(tello=7)
                        fly.stop(tello=8)
                        fly.stop(tello=9)
                        fly.stop(tello=10)

                    with fly.sync_these():
                        fly.back(dist=100, tello=1,sync=True)
                        fly.back(dist=100, tello=2,sync=True)
                        fly.back(dist=100, tello=3,sync=True)
                        fly.back(dist=100, tello=4,sync=True)
                        fly.back(dist=100, tello=5,sync=True)
                        fly.forward(dist=100, tello=6,sync=True)
                        fly.forward(dist=100, tello=7,sync=True)
                        fly.forward(dist=100, tello=8,sync=True)
                        fly.forward(dist=100, tello=9,sync=True)
                        fly.forward(dist=100, tello=10,sync=True)

                    with fly.sync_these():
                        fly.stop(tello=1)
                        fly.stop(tello=2)
                        fly.stop(tello=3)
                        fly.stop(tello=4)
                        fly.stop(tello=5)
                        fly.stop(tello=6)
                        fly.stop(tello=7)
                        fly.stop(tello=8)
                        fly.stop(tello=9)
                        fly.stop(tello=10)
                      
                    
                    with fly.sync_these():
                        fly.left(dist=60, tello=1,sync=True)
                        fly.left(dist=60, tello=2,sync=True)
                        fly.left(dist=60, tello=3,sync=True)
                        fly.left(dist=60, tello=4,sync=True)
                        fly.left(dist=60, tello=5,sync=True)
                        fly.right(dist=60, tello=6,sync=True)
                        fly.right(dist=60, tello=7,sync=True)
                        fly.right(dist=60, tello=8,sync=True)
                        fly.right(dist=60, tello=9,sync=True)
                        fly.right(dist=60, tello=10,sync=True)

                    with fly.sync_these():
                        fly.stop(tello=1)
                        fly.stop(tello=2)
                        fly.stop(tello=3)
                        fly.stop(tello=4)
                        fly.stop(tello=5)
                        fly.stop(tello=6)
                        fly.stop(tello=7)
                        fly.stop(tello=8)
                        fly.stop(tello=9)
                        fly.stop(tello=10)

                    with fly.sync_these():
                        fly.down(dist=100, tello=1,sync=True)
                        fly.down(dist=100, tello=2,sync=True)
                        fly.down(dist=100, tello=3,sync=True)
                        fly.down(dist=100, tello=4,sync=True)
                        fly.down(dist=100, tello=5,sync=True)
                        fly.down(dist=10, tello=6,sync=True)
                        fly.down(dist=10, tello=7,sync=True)
                        fly.down(dist=10, tello=8,sync=True)
                        fly.down(dist=10, tello=9,sync=True)
                        fly.down(dist=10, tello=10,sync=True)

                    with fly.sync_these():
                        fly.stop(tello=1)
                        fly.stop(tello=2)
                        fly.stop(tello=3)
                        fly.stop(tello=4)
                        fly.stop(tello=5)
                        fly.stop(tello=6)
                        fly.stop(tello=7)
                        fly.stop(tello=8)
                        fly.stop(tello=9)
                        fly.stop(tello=10)
                    fly.land()
                else :
                    pass
            except KeyboardInterrupt as e:
                break
except KeyboardInterrupt as e:
    fly.Stop()