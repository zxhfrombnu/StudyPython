# tuna = int(input("what's your fav number?\n"))
# print(tuna)

while True:
    try:
        number = int(input("What's your fav number\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure to entry a number")
    except ZeroDivisionError:
        print("Please don't input zero")
    except:
        break
    finally:
        print("loop complete")