import numpy as np
import math
from sklearn.neighbors import KNeighborsClassifier

def main():
    X = np.array([       # INDEPENDENT VARIABLES
        [2,60],
        [5,80],
        [6,85],
        [1,50]
    ])

    Y = np.array(["Fail","Pass","Pass","Fail"])   # DEPENDENT VARIABLES

    New_Point = np.array([[4,70]])

    print("="*70)
    print(" DISPLAYING VARIABLES ".center(70,"="))
    print("="*70,end="\n\n")

    print("-"*70,end="\n")

    print("INDEPENDENT VARIABLES : ")
    print(X)
    print(end="\n")

    print("DEPENDENT VARIABLES : ")
    print(Y)
    print(end="\n")

    print("TESTING POINTS : ")
    print(New_Point)

    print("-"*70,end="\n\n")
    print("="*70,end="\n\n")

    print("="*70)
    print(" MODEL CREATION ".center(70,"="))
    print("="*70,end="\n\n")

    print("-"*70,end="\n")

    Model = KNeighborsClassifier(n_neighbors=3)

    Model = Model.fit(X,Y)

    Y_Pred = Model.predict(New_Point)

    print(f"PREDICTED LABEL : {Y_Pred}")
    print("-"*70,end="\n\n")

    print("="*70)

if __name__ == "__main__":
    main()