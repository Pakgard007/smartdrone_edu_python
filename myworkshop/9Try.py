while True:
    try:
        minput =input("Enter command :")
        if      minput =="c":
            print("command")
        elif    minput == "t":
            print("take off")
        elif    minput == "l":
            print("Landing")
        elif    minput == "pass":
            continue
        elif    minput =="q":
            break
        else:
            pass
    except KeyboardInterrupt:
        break
    except :
        pass        