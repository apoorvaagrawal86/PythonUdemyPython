def exceptionHandling():
    try:

        a = 10
        b = 20
        c = 10

        d = (a+b)/c
        print(d)
    # except ZeroDivisionError:
    #     print("Zero Division")
    # except TypeError:
    #     print("Can't add string to integer")
    except:
        print("In the except block")
        #raise Exception("This is an exception")
    else:
        print("Because there was no exception, else is executed")
    finally:
        print("Finally, always executed")

exceptionHandling()