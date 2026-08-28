########################## IMPORTING MODULES WHICH WE WANT #####################
import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
#################################################################################


def WinePredictor(DataPath):
    Border = "="*90

    ############### STEP 1 : LOAD THE DATA #################################
    
    print(Border)
    print(" STEP 1 : LOAD THE DATASET FROM CSV FILE ".center(90,"="))
    print(Border,end="\n\n")
    print("-"*90)

    df = pd.read_csv(DataPath)

    print("Some entries of Dataset : ")
    print(df.head())
    print("-"*90,end="\n\n")
    print(Border,end="\n\n")

    ############## STEP 2 : CLEAN THE DATASET #################################

    print(Border)
    print(" STEP 2 : CLEAN THE DATASET ".center(90,"="))
    print(Border,end="\n\n")
    print("-"*90)

    df.dropna(inplace=True)

    print(f"SHAPE OF THE DATASET : {df.shape}")
    print(f"TOTAL RECORDS : {df.shape[0]}")
    print(f"TOTAL COLUMNS : {df.shape[1]}",end="\n")

    print("-"*90,end="\n\n")
    print(Border,end="\n\n")

    
    ############## STEP 3 : SEPARATE INDEPENDENT AND DEPENDENT VARIABLES #################################

    print(Border)
    print(" STEP 3 : SEPARATE INDEPENDENT AND DEPENDENT VARIABLES ".center(90,"="))
    print(Border,end="\n\n")
    print("-"*90)

    X = df.drop(columns=["Class"])
    Y = df["Class"]

    print(f"SHAPE OF THE X : {X.shape}")
    print(f"SHAPE OF THE Y : {Y.shape}")

    print(f"INPUT COLUMNS : {X.columns.to_list()}")
    print(f"OUTPUT COLUMN : Class ",end="\n")
    print("-"*90,end="\n\n")
    print(Border,end="\n\n")

    ############## STEP 4 : SPLIT THE DATASET FOR TRAINING AND TESTING ##########

    print(Border)
    print(" STEP 4 : SPLIT THE DATASET FOR TRAINING AND TESTING ".center(90,"="))
    print(Border,end="\n\n")
   
    X_train , X_test , Y_train , Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("-"*90,end="\n")
    print("SHAPE OF THE TRAINING AND TESTING DATA : ",end="\n")

    print(f"SHAPE OF THE X_train : {X_train.shape}")
    print(f"SHAPE OF THE X_test : {X_test.shape}")
    print(f"SHAPE OF THE Y_train : {Y_train.shape}")
    print(f"SHAPE OF THE Y_test : {Y_test.shape}",end="\n")
    print("-"*90,end="\n\n")
    print(Border,end="\n\n")

    ############## STEP 5 : FEATURE SCALING #########################
    
    print(Border)
    print(" STEP 5 : FEATURE SCALING ".center(90,"="))
    print(Border,end="\n\n")
  
    print("-"*90,end="\n")
    Scalar = StandardScaler()
    X_train_scaled = Scalar.fit_transform(X_train)
    X_test_scaled = Scalar.fit_transform(X_test)

    print("FEATURE SCALING DONE.....",end="\n")
    print("-"*90,end="\n\n")
    print(Border,end="\n\n")

    ############## STEP 6 : HYPER PARAMETER TUNING #########################
    #
    #                We are creating the model 
    #                We are training the model
    #                We are testing the model as well
    #
    #########################################################################
    
    print(Border)
    print(" STEP 6 : HYPER PARAMETER TUNING ".center(90,"="))
    print(Border,end="\n\n")
      
    print("-"*90,end="\n")

    Accuracy_Scores = []
    K_values = range(1,21)

    for K in K_values:
        Model = KNeighborsClassifier(n_neighbors=K)   # Model Creation
        Model = Model.fit(X_train_scaled,Y_train)     # Model training
        Y_Pred = Model.predict(X_test_scaled)         # Model Training
        Accuracy = accuracy_score(Y_test,Y_Pred)      # Finding accuracy score
        Accuracy_Scores.append(Accuracy)              

    print("ACCURACY REPORT :  ")
    for no in Accuracy_Scores:
        print(no)

    print("-"*90,end="\n\n")
    print(Border,end="\n\n")

    ############## STEP 7 : GRAPHICAL REPRESENTATION #########################

    print(Border)
    print(" STEP 7 : GRAPHICAL REPRESENTATION ".center(90,"="))
    print(Border,end="\n\n")
          
    print("-"*90,end="\n")

    plt.figure(figsize=(8,5))
    plt.plot(K_values,Accuracy_Scores,marker="o")
    plt.title("K VALUES VS ACCURACY")
    plt.xlabel("VALUES OF THE K")
    plt.ylabel("ACCURACY")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()

def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()
