from rcsa_dev_kit_edu_python_lib.fly_tello import FlyTello
my_tellos = list()

# Check Serial Tello EDU
my_tellos.append('0TQDG6SEDB7WCT') # Drone1
my_tellos.append('0TQDFBHEDBTUM2') # Drone2
my_tellos.append('0TQDFBHEDBTUM2') # Drone3
my_tellos.append('0TQDFBHEDBTUM2') # Drone4
my_tellos.append('0TQDFBHEDBTUM2') # Drone5
my_tellos.append('0TQDFBHEDBTUM2') # Drone6
my_tellos.append('0TQDFBHEDBTUM2') # Drone7
my_tellos.append('0TQDFBHEDBTUM2') # Drone8
my_tellos.append('0TQDFBHEDBTUM2') # Drone9
my_tellos.append('0TQDFBHEDBTUM2') # Drone10


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
                    fly.bounce(dist=100,times=3) # dist=distance between up and down , times = Number of round bounce
                if minput == 'q' :
                    print('Exit Program')
                    break
                if minput == '1':
                    print ("Mission1")
                    fly.takeoff()
                    with fly.sync_these():
                        fly.up(dist=60, tello=1)
                        fly.up(dist=60, tello=2)
                        fly.up(dist=60, tello=3)
                        fly.up(dist=60, tello=4)
                        fly.up(dist=60, tello=5)
                        
                    with fly.sync_these():
                        fly.reorient(height=mz, pad='m1', tello=1)
                        fly.reorient(height=mz, pad='m1', tello=2)
                        fly.reorient(height=mz, pad='m1', tello=3)
                        fly.reorient(height=mz, pad='m1', tello=4)
                        fly.reorient(height=mz, pad='m1', tello=5)
                        fly.reorient(height=mz, pad='m2', tello=6)
                        fly.reorient(height=mz, pad='m2', tello=7)
                        fly.reorient(height=mz, pad='m2', tello=8)
                        fly.reorient(height=mz, pad='m2', tello=9)
                        fly.reorient(height=mz, pad='m2', tello=10)

        
                    with fly.sync_these():
                        fly.forward(dist=60, tello=1)
                        fly.forward(dist=60, tello=2)
                        fly.forward(dist=60, tello=3)
                        fly.forward(dist=60, tello=4)
                        fly.forward(dist=60, tello=5)
                        fly.back(dist=60, tello=6)
                        fly.back(dist=60, tello=7)
                        fly.back(dist=60, tello=8)
                        fly.back(dist=60, tello=9)
                        fly.back(dist=60, tello=10)
                
                    with fly.sync_these():
                        with fly.sync_these():
                        fly.reorient(height=mz, pad='m1', tello=1)
                        fly.reorient(height=mz, pad='m1', tello=2)
                        fly.reorient(height=mz, pad='m1', tello=3)
                        fly.reorient(height=mz, pad='m1', tello=4)
                        fly.reorient(height=mz, pad='m1', tello=5)
                        fly.reorient(height=mz, pad='m2', tello=6)
                        fly.reorient(height=mz, pad='m2', tello=7)
                        fly.reorient(height=mz, pad='m2', tello=8)
                        fly.reorient(height=mz, pad='m2', tello=9)
                        fly.reorient(height=mz, pad='m2', tello=10)

                    
                    fly.land()
                else :
                    pass
            except KeyboardInterrupt as e:
                break
except KeyboardInterrupt as e:
    fly.Stop()