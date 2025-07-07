from rcsa_dev_kit_edu_python_lib.fly_tello import FlyTello
my_tellos = list()

# Check Serial Tello EDU
my_tellos.append('0TQDFBHEDBTUM1') # Drone1

try :
    with FlyTello(my_tellos) as fly: 
        while (True):
            try :  
                print ("ap = setAP for RCSA-DL")
                minput = input("Enter your command : ")
                if minput == 'ap':
                    print ("Set AP for RCSA-DL")
                    fly.set_ap_wifi(ssid='staff tello SB',password= '45224522')
                    
                else :
                    pass
            except KeyboardInterrupt as e:
                break
except KeyboardInterrupt as e:
    fly.Stop()