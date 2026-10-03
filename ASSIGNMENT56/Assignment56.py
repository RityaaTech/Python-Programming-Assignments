# ======================= IMPORTING THE MODULES ===========================
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
# =========================================================================

def MarvellousEnsemble():

    Border = "="*70
    New_Border = "-"*70

    ######################################################################
    ##################### STEP 1 : LOAD THE DATSET #######################
    ######################################################################

    print(Border)
    print(" STEP 1 : LOAD THE DATASET ".center(70,"="))
    print(Border,end="\n\n")

    print(New_Border,end="\n")

    Datapath = "Fraudulent_Transaction_Detection.csv"

    df = pd.read_csv(Datapath)
    print("Dataset loaded successfully.")

    print("First 5 records : ")
    print(df.head())

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")

    ######################################################################
    ##################### STEP 2 : DATA ANALYSIS (EDA) ###################
    ######################################################################

    print(Border)
    print(" STEP 2 : DATA ANALYSIS (EDA) ".center(70,"="))
    print(Border,end="\n\n")
    
    print(New_Border,end="\n")

    print("Missing Values : ")
    print(df.isnull().sum())

    print("Data Analysis done successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")
    
    ######################################################################
    ############### STEP 3 : SEPARATE FEATURES AND LABELS ################
    ###################################################################### 

    print(Border)
    print(" STEP 3 : SEPARATE FEATURES AND LABELS ".center(70,"="))
    print(Border,end="\n\n")
        
    print(New_Border,end="\n")

    X = df.drop("Fraud",axis=1)
    Y = df["Fraud"]

    print(f"X Shape : {X.shape}")
    print(f"Y Shape : {Y.shape}")

    print("Separated the Features and Labels successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")
        
    ######################################################################
    ######### STEP 4 : SPLIT THE DATASET FOR TRAINING AND TESTING ########
    ###################################################################### 

    print(Border)
    print(" STEP 4 : SPLIT THE DATASET FOR TRAINING AND TESTING ".center(70,"="))
    print(Border,end="\n\n")
            
    print(New_Border,end="\n")

    X_train , X_test , Y_train , Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Splitted the Dataset for Training and Testing successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")
            
    ######################################################################
    ################### STEP 5 : SCALE THE FEATURES  #####################
    ######################################################################

    print(Border)
    print(" STEP 5 : SCALE THE FEATURES ".center(70,"="))
    print(Border,end="\n\n")
                
    print(New_Border,end="\n")

    Scaler = StandardScaler()

    X_train = Scaler.fit_transform(X_train)
    X_test = Scaler.fit_transform(X_test)

    print("Scaled the Features successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")

    ######################################################################
    ################ STEP 6 : CREATE THE INDIVIDUAL MODELS  ##############
    ######################################################################
    
    print(Border)
    print(" STEP 6 : CREATE THE INDIVIDUAL MODELS ".center(70,"="))
    print(Border,end="\n\n")
    print(New_Border,end="\n")

    #######################################################################

    Model_Det = DecisionTreeClassifier(random_state=42)

    Model_Det = Model_Det.fit(X_train,Y_train)
    Model_Det_Pred = Model_Det.predict(X_test)
    Accuracy_Model_Det = accuracy_score(Y_test,Model_Det_Pred)

    #######################################################################

    #######################################################################

    Model_Bag = BaggingClassifier(
        estimator=Model_Det,
        n_estimators=10,
        random_state=42
    )

    Model_Bag = Model_Bag.fit(X_train,Y_train)
    Model_Bag_Pred = Model_Bag.predict(X_test)
    Accuracy_Model_Bag = accuracy_score(Y_test,Model_Bag_Pred)

    #######################################################################

    #######################################################################

    Model_AdaBoosting = AdaBoostClassifier(
        n_estimators=50,
        learning_rate=1.0,
        random_state=42
    )

    Model_AdaBoosting = Model_AdaBoosting.fit(X_train,Y_train)
    Model_AdaBoosting_Pred = Model_AdaBoosting.predict(X_test)
    Accuracy_Model_AdaBoosting = accuracy_score(Y_test,Model_AdaBoosting_Pred)

    #######################################################################

    #######################################################################

    Model_RandomForest = RandomForestClassifier(
        n_estimators=10,
        random_state=42
    )

    Model_RandomForest = Model_RandomForest.fit(X_train,Y_train)
    Model_RandomForest_Pred = Model_RandomForest.predict(X_test)
    Accuracy_Model_RandomForest = accuracy_score(Y_test,Model_RandomForest_Pred)

    #######################################################################

    print("Individual trained Successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")

    ######################################################################
    ################ STEP 7 : CREATE THE VOTING MODELS  ##################
    ######################################################################
        
    print(Border)
    print(" STEP 7 : CREATE THE VOTING MODELS ".center(70,"="))
    print(Border,end="\n\n")
    print(New_Border,end="\n")

    Model = VotingClassifier(
        estimators=[
            ("Decision Tree",Model_Det),
            ("Bagging",Model_Bag),
            ("Ada Boost",Model_AdaBoosting),
            ("Random Forest",Model_RandomForest)
        ],
        voting="hard"
    )

    print("Voting Model created successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")

    ######################################################################
    ################ STEP 8 : TRAIN THE MODEL  ###########################
    ######################################################################
            
    print(Border)
    print(" STEP 8 : TRAIN THE MODEL ".center(70,"="))
    print(Border,end="\n\n")
    print(New_Border,end="\n")

    Model = Model.fit(X_train,Y_train)
    print("Model Trained successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")
    
    ######################################################################
    ################ STEP 9 : TEST THE MODEL  ###########################
    ######################################################################
                
    print(Border)
    print(" STEP 9 : TEST THE MODEL ".center(70,"="))
    print(Border,end="\n\n")
    print(New_Border,end="\n")

    Y_Pred = Model.predict(X_test)
    print("Model Tested successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")
    
    ######################################################################
    ################ STEP 10 : EVALUATE THE MODEL  #######################
    ######################################################################
                
    print(Border)
    print(" STEP 10 : EVALUATE THE MODEL ".center(70,"="))
    print(Border,end="\n\n")
    print(New_Border,end="\n")

    Accuracy_Model = accuracy_score(Y_test,Y_Pred)

    print("ACCURACY OF THE FOLLOWING MODELS : ")
    print(New_Border,end="\n")

    print(f"1) DECISION TREE CLASSIFIER : {Accuracy_Model_Det*100} %")
    print(f"2) BAGGING CLASSIFER : {Accuracy_Model_Bag*100} %")
    print(f"3) ADA BOOST CLASSIFIER : {Accuracy_Model_AdaBoosting*100} %")
    print(f"4) RANDOM FOREST CLASSIFIER : {Accuracy_Model_RandomForest*100} %")
    print(f"5) VOTING CLASSIFIER : {Accuracy_Model*100} %")
    print(New_Border,end="\n")

    print("CONFUSION MATRIX : ")
    print(f"{confusion_matrix(Y_test,Y_Pred)}")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")

def main():
    MarvellousEnsemble()

if __name__ == "__main__":
    main()