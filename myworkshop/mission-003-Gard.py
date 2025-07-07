from rcsa_dev_kit_edu_python_lib.fly_tello import FlyTello
my_tellos = list()
import time
# Check Serial Tello EDU
my_tellos.append('0TQDG7PEDB8F91') # Drone1

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
                if minput == "bounce":
                    print('Bounce')
                    fly.bounce(dist=100,times=3) 
                if minput == 'q' :
                    print('Exit Program')
                    break
                if minput == '1':
                    print ("Mission1")
                    fly.takeoff()
                    
                    with fly.sync_these():    
                        fly.straight(x=100, y=0, z=50, speed=60, tello=1)
                    
                    with fly.sync_these():    
                        fly.forward(dist=30, tello=1)
                    
                    with fly.sync_these():    
                        fly.bounceleft(dist=30,times=1, tello=1)

                    with fly.sync_these():    
                        fly.forward(dist=30, tello=1)

                    with fly.sync_these():    
                        fly.bounce(dist=30,times=1, tello=1)

                    with fly.sync_these():    
                        fly.forward(dist=30, tello=1)

                    with fly.sync_these():    
                        fly.bounceright(dist=30,times=1, tello=1) 

                    with fly.sync_these():    
                        fly.forward(dist=30, tello=1)

                    with fly.sync_these():    
                        fly.bouncedown(dist=30,times=1, tello=1) 

                    with fly.sync_these():    
                        fly.forward(dist=30, tello=1)

                    with fly.sync_these():    
                        fly.rotate_cw(angle=180, tello=1)

                    with fly.sync_these():    
                        fly.straight(x=-100, y=0, z=-50, speed=60, tello=1)

                    with fly.sync_these():    
                        fly.forward(dist=340, tello=1)

                    with fly.sync_these():    
                        fly.rotate_cw(angle=180, tello=1)
            

                    fly.land()
                else :
                    pass
            except KeyboardInterrupt as e:
                break
except KeyboardInterrupt as e:
    fly.Stop()