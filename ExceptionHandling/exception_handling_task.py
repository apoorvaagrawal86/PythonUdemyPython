def car():
    try:
        car = {"make":"bmw","model":"i8","year":2018}
        #car = {"make","model","year"}
        print(car[color])
    except:
        print("color not part of dictionary")
    finally:
        print("Try catch block checked")

car()