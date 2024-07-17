def test_is_number(x):
    try:
        if(x == 0):
            print("great  it works")
        else:
            print("not zero")
    except ZeroDivisionError:
        print("its a zero division error")
    finally:
        print("finally done")



test_is_number(0)