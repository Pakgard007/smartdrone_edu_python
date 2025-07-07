from rcsa_dev_kit_edu_python_lib.fly_tello import FlyTello
my_tellos = list()

# Check Serial Tello EDU
my_tellos.append('0TQDG6SEDB7WCT') # Drone1

mspeed = 55
mx = 245
my = 245
mz = 75

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
                    def takeoff(self, tello: Union[int, str]='All', sync: bool=True) -> None:
            
                    self._command('Takeoff', 'Control', tello, sync)

                    def land(self, tello: Union[int, str]='All', sync: bool=True) -> None:
                    """ Auto landing """
                    self._command('land', 'Control', tello, sync)

                    def stop(self, tello: Union[int, str]='All') -> None:
                    """ Stop Tello wherever it is, even if mid-manoeuvre. """
                    self._command('stop', 'Control', tello, sync=False)

                    def emergency(self, tello: Union[int, str]='All') -> None:
                    """ Immediately kill power to the Tello's motors. """
                    self._command('emergency', 'Control', tello, sync=False)

                    def up(self, dist: int, tello: Union[int, str]='All', sync: bool=True) -> None:
                    """ Move up by dist (in cm) """
                    self._command_with_value('up', 'Control', dist, 20, 500, 'cm', tello, sync)

                    def down(self, dist: int, tello: Union[int, str]='All', sync: bool=True) -> None:
                    """ Move down by dist (in cm) """
                    self._command_with_value('down', 'Control', dist, 20, 500, 'cm', tello, sync)

                    def left(self, dist: int, tello: Union[int, str]='All', sync: bool=True) -> None:
                    """ Move left by dist (in cm) """
                    self._command_with_value('left', 'Control', dist, 20, 500, 'cm', tello, sync)

                    def right(self, dist: int, tello: Union[int, str]='All', sync: bool=True) -> None:
                    """ Move right by dist (in cm) """
                    self._command_with_value('right', 'Control', dist, 20, 500, 'cm', tello, sync)

                    def forward(self, dist: int, tello: Union[int, str]='All', sync: bool=True) -> None:
                    """ Move forward by dist (in cm) """
                    self._command_with_value('forward', 'Control', dist, 20, 500, 'cm', tello, sync)

                    def back(self, dist: int, tello: Union[int, str]='All', sync: bool=True) -> None:
                    """ Move back by dist (in cm) """
                    self._command_with_value('back', 'Control', dist, 20, 500, 'cm', tello, sync)

                    def rotate_cw(self, angle: int, tello: Union[int, str]='All', sync: bool=True) -> None:
                    """ Rotate clockwise (turn right) by angle (in degrees) """
                    self._command_with_value('cw', 'Control', angle, 1, 360, 'degrees', tello, sync)

                    def rotate_ccw(self, angle: int, tello: Union[int, str]='All', sync: bool=True) -> None:
                    """ Rotate anti-clockwise (turn left) by angle (in degrees) """
                    self._command_with_value('ccw', 'Control', angle, 1, 360, 'degrees', tello, sync)

                    def flip(self, direction: str, tello: Union[int, str]='All', sync: bool=True) -> None:
                    """ Perform a flip in the specified direction (left/right/forward/back) - will jump ~30cm in that direction.

                    Note that Tello is unable to flip if battery is less than 50%!"""
                    fly.land()
                else :
                    pass
            except KeyboardInterrupt as e:
                break
except KeyboardInterrupt as e:
    fly.Stop()