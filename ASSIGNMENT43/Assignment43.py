# ------------------------- IMPORTING MODULES --------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
# --------------------------------------------------------------------


def main():

    Border = "="*50

    print(Border)
    print(" Marvellous KNN Classifer ".center(50,"="))
    print(Border,end="\n\n")

    # ===== STEP 1 : LOAD THE DATA =====================

    print(Border)
    print(" STEP 1 : LOAD THE DATASET ".center(50,"="))
    print(Border,end="\n\n")

    print("-"*50,end="\n")

    Datapath = "MarvellousInfosystems_PlayPredictor.csv"

    df = pd.read_csv(Datapath)

    print("Dataset Loaded successfully...",end="\n")
    print("-"*50,end="\n\n")

    print(Border,end="\n\n")

    # ===== STEP 2 : DATA ANALYSIS  =====================

    print(Border)
    print(" STEP 2 : DATA ANALYSIS ".center(50,"="))
    print(Border,end="\n\n")
    
    print("-"*50,end="\n")

    print(f"Shape of the Dataset : {df.shape}")

    print(f"Columns names : {list(df.columns)}")

    print("-"*50,end="\n\n")
    print(Border,end="\n\n")

    # ===== STEP 3 : DECIDE THE INDEPENDENT AND DEPENDENT VARIABLES  =====================

    print(Border)
    print(" STEP 3 : DECIDE THE INDEPENDENT AND DEPENDENT VARIABLES ".center(50,"="))
    print(Border,end="\n\n")
        
    print("-"*50,end="\n")

    WeatherEncoder = LabelEncoder()
    TemperatureEncoder = LabelEncoder()
    PlayEncoder = LabelEncoder()

    df["Wether"] = WeatherEncoder.fit_transform(df["Wether"])
    df["Temperature"] = TemperatureEncoder.fit_transform(df["Temperature"])
    df["Play"] = PlayEncoder.fit_transform(df["Play"])

    Feature_Columns = [
        "Wether",
        "Temperature",
    ]

    X = df[Feature_Columns]
    Y = df["Play"]

    print(f"X shape : {X.shape}")
    print(f"Y shape : {Y.shape}")

    print("-"*50,end="\n\n")
    print(Border,end="\n\n")

    # ===== STEP 3 : SPLIT THE DATASET FOR TRAINING AND TESTING  =====================
    
    print(Border)
    print(" STEP 3 : SPLIT THE DATASET FOR TRAINING AND TESTING  ".center(50,"="))
    print(Border,end="\n\n")
        
    print("-"*50,end="\n")

    X_train , X_test , Y_train , Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    print(f"X_train : {X_train.shape}")
    print(f"X_test : {X_test.shape}")
    print(f"Y_train : {Y_train.shape}")
    print(f"Y_test : {Y_test.shape}")

    print("-"*50,end="\n\n")
    print(Border,end="\n\n")

    # ===== STEP 4 : BUILD THE MODEL   =====================

    print(Border)
    print(" STEP 4 : BUILD THE MODEL ".center(50,"="))
    print(Border,end="\n\n")
        
    print("-"*50,end="\n")

    Model = KNeighborsClassifier(n_neighbors=3)
    print("Model created successfully...")

    print("-"*50,end="\n\n")
    print(Border,end="\n\n")

    # ===== STEP 5 : TRAIN THE MODEL =====================

    print(Border)
    print(" STEP 5 : TRAIN THE MODEL ".center(50,"="))
    print(Border,end="\n\n")
            
    print("-"*50,end="\n")

    Model.fit(X_train,Y_train)
    print("Model trained successfully..")

    print("-"*50,end="\n\n")
    print(Border,end="\n\n")
    
    # ===== STEP 6 : TEST THE MODEL =====================
    
    print(Border)
    print(" STEP 6 : TEST THE MODEL ".center(50,"="))
    print(Border,end="\n\n")

    print("-"*50,end="\n")

    Y_Pred = Model.predict(X_test)
    print("Model evaluated successfully.")

    print("-"*50,end="\n\n")
    print(Border,end="\n\n")

    # ===== STEP 7 : CALCULATE THE ACCURACY =====================

    
    print(Border)
    print(" STEP 6 : TEST THE MODEL ".center(50,"="))
    print(Border,end="\n\n")

    print("-"*50,end="\n")

    Accuracy = accuracy_score(Y_test,Y_Pred)
    print(f"ACCURACY SCORE : {Accuracy*100} %")
    
if __name__ == "__main__":
    main()