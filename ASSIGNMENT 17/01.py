from ArithmeticModule import Add , Sub , Mult , Div

def main():
    x = int(input("ENTER THE NUMBER : "))
    y = int(input("ENTER THE NUMBER : "))
     
    Result_1 = Add(x,y)
    print(f"12 + 6 = {Result_1}")

    Result_2 = Sub(x,y)
    print(f"12 - 6 = {Result_2}")

    Result_3 = Mult(x,y)
    print(f"12 * 6 = {Result_3}")

    Result_4 = Div(x,y)
    print(f"12 / 6 = {Result_4}")


if __name__ == "__main__":
    main()
    