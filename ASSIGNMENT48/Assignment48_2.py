# ------------------- IMPORTING MODULES ------------------
import numpy as np
from sklearn.metrics import mean_squared_error , r2_score 
# ---------------------------------------------------------

def main():

    # --------------- 1) LOAD THE DATA ----------------------

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print(f"VALUES OF THE INDEPENDENT VARIABLES [X] : {X}")
    print(f"VALUES OF THE DEPENDENT VARIABLES [Y] : {Y}")

    print(end="\n\n")

    Sum_X = 0
    Sum_Y = 0

    for i in range(len(X)):
        Sum_X = Sum_X + X[i]
        Sum_Y = Sum_Y + Y[i]

    Mean_X = Sum_X / len(X)
    Mean_Y = Sum_Y / len(Y)

    print(f"Mean_X : {Mean_X}")
    print(f"Mean_Y : {Mean_Y}")

    n = len(X)

    Numerator = 0
    Denomerator = 0

    for i in range(n):
        Numerator = Numerator + ((X[i] - Mean_X) * (Y[i] - Mean_Y))
        Denomerator = Denomerator + ((X[i] - Mean_X)**2)

    m = Numerator / Denomerator

    # y = mx + c
    # c = y - mx
    # c = ymean - m * xmean

    c = Mean_Y - m * Mean_X
    print(f"INTERCEPT (c) : {c}")

    MSE = mean_squared_error(X,Y)    
    NMSE = np.sqrt(MSE)   
    R2 = r2_score(X,Y)
  
    print(f"MEAN SQUARE ERROR : {MSE}")
    print(f"NMSE : {NMSE}")
    print(f"R2 : {R2}")



if __name__ == "__main__":
    main()