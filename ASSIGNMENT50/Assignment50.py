# ------------------------- IMPORTING MODULES ----------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix
# -----------------------------------------------------------------------

def main():

    Border = "="*60
    New_Border = "-"*60

    # --------------- STEP 1 : LOAD THE DATASET --------------------------

    print(Border)
    print(" STEP 1 : LOAD THE DATASET ".center(60,"="))
    print(Border,end="\n\n")

    print(New_Border,end="\n")

    Datapath = "breast_cancer.csv"
    df = pd.read_csv(Datapath)

    print("Dataset loaded successfully..",end="\n")

    print(f"Shape of the Datset : {df.shape}")

    print("First 5 records : ")
    print(df.head())

    print(Border,end="\n\n")
    print(New_Border,end="\n\n")


    # --------------- STEP 2 : SEPARATE FEATURES AND LABLES  --------------------------
    
    print(Border)
    print(" STEP 2 : SEPARATE FEATURES AND LABLES ".center(60,"="))
    print(Border,end="\n\n")
    
    print(New_Border,end="\n")

    X = df.drop("target",axis=1)
    Y = df["target"]

    print(f"X Shape : {X.shape}")
    print(f"Y Shape : {Y.shape}")

    print(Border,end="\n\n")
    print(New_Border,end="\n\n")

    # --------------- STEP 3 : SPLIT THE DATASET FOR TRAINING AND TESTING --------------------------
        
    print(Border)
    print(" STEP 3 : SPLIT THE DATASET FOR TRAINING AND TESTING ".center(60,"="))
    print(Border,end="\n\n")
        
    print(New_Border,end="\n")

    X_train , X_test , Y_train , Y_test = train_test_split(
        X,
        Y,
        random_state=42,
        test_size=0.2
    )

    print("Splitted the Dataset for the training and testing..")

    print(Border,end="\n\n")
    print(New_Border,end="\n\n")
    
    # --------------- STEP 4 : SCALE THE FEATURES --------------------------
            
    print(Border)
    print(" STEP 4 : SCALE THE FEATURES ".center(60,"="))
    print(Border,end="\n\n")
            
    print(New_Border,end="\n")

    Scaler = StandardScaler()

    X_train = Scaler.fit_transform(X_train)
    X_test = Scaler.fit_transform(X_test)

    print("Scaled the features successfully.")

    print(Border,end="\n\n")
    print(New_Border,end="\n\n")
        
    # --------------- STEP 5 : CREATE THE MODEL  --------------------------
                
    print(Border)
    print(" STEP 5 : CREATE THE MODEL ".center(60,"="))
    print(Border,end="\n\n")
    print(New_Border,end="\n")

    Model = LogisticRegression(max_iter=1000)
    print("Model created successfully.")

    print(Border,end="\n\n")
    print(New_Border,end="\n\n")
            
    # --------------- STEP 6 : TRAIN THE MODEL  --------------------------
                    
    print(Border)
    print(" STEP 6 : TRAIN THE MODEL ".center(60,"="))
    print(Border,end="\n\n")
    print(New_Border,end="\n")

    Model = Model.fit(X_train,Y_train)
    print("Trained the Model..")

    print(Border,end="\n\n")
    print(New_Border,end="\n\n")
                
    # --------------- STEP 7 :TEST THE MODEL --------------------------
                        
    print(Border)
    print(" STEP 7 :TEST THE MODEL ".center(60,"="))
    print(Border,end="\n\n")
    print(New_Border,end="\n")

    Y_Pred = Model.predict(X_test)
    print("Tested the Model..")

    print(Border,end="\n\n")
    print(New_Border,end="\n\n")
                    
    # --------------- STEP 8 : EVALUATE THE MODEL --------------------------
                            
    print(Border)
    print(" STEP 8 : EVALUATE THE MODEL ".center(60,"="))
    print(Border,end="\n\n")
    print(New_Border,end="\n")

    Accuracy = accuracy_score(Y_test,Y_Pred)
    print(f"ACCURACY SCORE : {Accuracy*100} %")

    print(f"CONFUSION MATRIX : {confusion_matrix(Y_test,Y_Pred)}")

    # ----------------------------------------------------------------------
if __name__ == "__main__":
    main()