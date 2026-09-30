import numpy as np
import math

def Euclidean_Distance(P1,P2):
    Answer = math.sqrt((P1["X"] - P2["X"])**2 + (P1["Y"] - P2["Y"])**2)
    return Answer

def MarvellousKNNClassifier():
    Border = "="*70
    
    Data = [
            {"point" : "A" , "X" : 1 , "Y" : 2 , "label" : "Red"},
            {"point" : "B" , "X" : 2 , "Y" : 3 , "label" : "Red"},
            {"point" : "C" , "X" : 3 , "Y" : 1 , "label" : "Blue"},
            {"point" : "D" , "X" : 6 , "Y" : 5 , "label" : "Blue"},
    ]
    
    print(Border)
    print(" Marvellous KNN Clasifier ".center(70,"="))
    print(Border,end="\n\n")
    
    print("-"*70,end="\n")
    
    for i in Data:
            print(i)
    
    print("-"*70,end="\n\n")
    print(Border,end="\n\n")

    #################### 2) Accept Euclidean Distance from all dataset points ###########
    print(Border)
    print(" FIND EUCLIDEAN DISTANCE FROM ALL DATASET POINTS ".center(70,"="))
    print(Border,end="\n\n")

    print("-"*70,end="\n")

    #################### 1) Accept X and Y coordinates of a new point from user ########
    New_Point = {"X" : 2 , "Y" : 2}


    #################### 3) Sort the data ##################################3
    for d in Data:
        d["distance"] = Euclidean_Distance(d,New_Point)

    for d in Data:
        print(f"{d["distance"]} : {d["label"]}")

    print("-"*70,end="\n\n")
    print(Border,end="\n\n")

    print(Border)
    print(" SORT THE DATA ".center(70,"="))
    print(Border,end="\n\n")

    Sorted_Data = sorted(Data,key=lambda item : item["distance"])

    print("-"*70,end="\n")
    print("SORTED DATA : ",end="\n")

    for d in Sorted_Data:
        print(d)

    print("-"*70,end="\n\n")
    print(Border,end="\n\n")

    ################# 4) Select K = 3 nearest neigbours ###################

    K = 3   # For nearest neigbours

    Nearest = Sorted_Data[:K]

    print(Border)
    print(" NEAREST 3 MEMBERS ARE : ")
    print(Border,end="\n\n")

    print("-"*70,end="\n")

    for d in Nearest:
        print(d)

    print("-"*70,end="\n\n")
    print(Border,end="\n\n")

    ################### Voting ###########################################

    Votes = {}

    for neighbours in Nearest:
        label = neighbours["label"]
        Votes[label] = Votes.get(label,0) + 1

    print(Border)
    print(" VOTING RESULT ".center(70,"="))
    print(Border,end="\n\n")

    print("-"*70,end="\n")

    for d in Votes:
        print(f"NAME : {d} ,NUMBER OF THE VOTES : {Votes[d]}")

    print(Votes)

    print("-"*70,end="\n\n")

    print(Border,end="\n\n")

    ##################### FINAL PREDICTION ############################

    iMAX = 0
    Name = ""

    print(Border)
    print(" FINAL PREDICTION ".center(70,"="))
    print(Border,end="\n\n")

    for d in Votes:
        if (Votes[d] > iMAX):
            iMAX = Votes[d]
            Name = d

    print("-"*70,end="\n")

    print(f"FINAL PREDICTION : {Name}")

    print("-"*70,end="\n\n")
    print(Border,end="\n\n")

   
def main():
    MarvellousKNNClassifier()


if __name__ == "__main__":
    main()