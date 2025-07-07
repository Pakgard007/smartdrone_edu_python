from rcsa_dev_kit_edu_python_lib.fly_tello import FlyTello
my_tellos = list()
import time
# Check Serial Tello EDU
my_tellos.append('0TQDG6SEDB7WCT') # Drone1

mspeed = 50
mx = 135
my = 140
mz = 100

try :
    with FlyTello(my_tellos ) as fly:
        while (True):
            try :
                print ("t=takeoff,l=land,b=battery?,s=speed?,h=height,q=exit")
                minput = input("Enter your command : ")
                
                if minput == 'q' :
                    print('pad_detection_off')
                    fly.pad_detection_off()
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
                    with fly.sync_these():
                        fly.pad_detection_off(tello=1, sync=True)

                    
                    
                    fly.land()
                else :
                    pass
            except KeyboardInterrupt as e:
                break
except KeyboardInterrupt as e:
    fly.Stop()