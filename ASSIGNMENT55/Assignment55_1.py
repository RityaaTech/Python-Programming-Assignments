# ---------------------- IMPORTING MODULES ---------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
# --------------------------------------------------------------------

def main():

    Border = "="*60
    New_Border = "-"*60

    ######################################################################
    ############### STEP 1 : LOAD THE DATASET ############################
    ######################################################################

    print(Border)
    print(" STEP 1 : LOAD THE DATASET ".center(60,"="))
    print(Border,end="\n\n")

    print(New_Border,end="\n")

    Datapath = "Customer_Loan_Approval (1).csv"

    df = pd.read_csv(Datapath)

    print("Dataset loaded successfully.",end="\n")

    print(f"First Five records : ")
    print(df.head())

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")

    ######################################################################
    ############### STEP 2 : CLEAN THE DATASET ############################
    ######################################################################

    print(Border)
    print(" STEP 2 : CLEAN THE DATASET ".center(60,"="))
    print(Border,end="\n\n")
    
    print(New_Border,end="\n")

    print("Missing Values : ")
    print(df.isnull().sum())

    print("Dataset cleaned successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")

    ######################################################################
    ############### STEP 3 : SEPARATE FEATURES AND LABLES ################
    ######################################################################

    print(Border)
    print(" STEP 3 : SEPARATE FEATURES AND LABLES ".center(60,"="))
    print(Border,end="\n\n")
        
    print(New_Border,end="\n")

    X = df.drop("LoanApproved",axis=1)
    Y = df["LoanApproved"]

    print(f"X Shape : {X.shape}")
    print(f"Y Shape : {Y.shape}")

    print("Separated Features and Labels successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")

    ######################################################################
    ########### STEP 4 : SPLIT THE DATSET FOR TRAINING AND TESTING #######
    ######################################################################

    print(Border)
    print(" STEP 4 : SPLIT THE DATSET FOR TRAINING AND TESTING ".center(60,"="))
    print(Border,end="\n\n")
            
    print(New_Border,end="\n")

    X_train , X_test , Y_train , Y_test = train_test_split(
        X,
        Y,
        random_state=42,
        test_size=0.2
    )

    print("Splitted the Dataset fot training and testing successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")

    ######################################################################
    ########### STEP 5 : SCALE THE FEATURES ##############################
    ######################################################################

    print(Border)
    print(" STEP 5 : SCALE THE FEATURES ".center(60,"="))
    print(Border,end="\n\n")
                
    print(New_Border,end="\n")

    Scalar = StandardScaler()

    X_train = Scalar.fit_transform(X_train)
    X_test = Scalar.fit_transform(X_test)

    print("Scaled the Features successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")

    ######################################################################
    ########### STEP 6 : CREATE THE INDIVIDUAL MODELS ####################
    ######################################################################

    print(Border)
    print(" STEP 6 : CREATE THE INDIVIDUAL MODELS ".center(60,"="))
    print(Border,end="\n\n")
                    
    print(New_Border,end="\n")

    Model_Log = LogisticRegression()
    Model_Det = DecisionTreeClassifier()
    Model_KNN = KNeighborsClassifier()

    print("Model created successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")

    ######################################################################
    ########### STEP 7 : CREATE THE VOTING MODEL #########################
    ######################################################################
    
    print(Border)
    print(" STEP 7 : CREATE THE VOTING MODEL ".center(60,"="))
    print(Border,end="\n\n")
                        
    print(New_Border,end="\n")

    Model = VotingClassifier(
        estimators=[
            ("Logistic",Model_Log),
            ("Decision Tree",Model_Det),
            ("Knn",Model_KNN)
        ],
        voting="hard"
    )

    print("Voting Model created successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")
    
    ######################################################################
    ########### STEP 8 : TRAIN THE MODEL #################################
    ######################################################################
        
    print(Border)
    print(" STEP 8 : TRAIN THE MODEL ".center(60,"="))
    print(Border,end="\n\n")
                            
    print(New_Border,end="\n")

    Model = Model.fit(X_train,Y_train)
    print("Model trained successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")
        
    ######################################################################
    ########### STEP 9 : TEST THE MODEL #################################
    ######################################################################
            
    print(Border)
    print(" STEP 9 : TEST THE MODEL ".center(60,"="))
    print(Border,end="\n\n")
                                
    print(New_Border,end="\n")
    
    Model = Model.fit(X_train,Y_train)
    print("Model trained successfully.")
    
    Y_Pred = Model.predict(X_test)
    print("Model tested successfully.")

    print(New_Border,end="\n\n")
    print(Border,end="\n\n")

    ######################################################################
    ########### STEP 10 : EVALUATE THE MODEL #############################
    ######################################################################
                
    print(Border)
    print(" STEP 10 : EVALUATE THE MODEL ".center(60,"="))
    print(Border,end="\n\n")
                                    
    print(New_Border,end="\n")

    Accuracy = accuracy_score(Y_test,Y_Pred)

    print(f"ACCURACY : {Accuracy*100} %")
    print(f"CONFUSION MATRIX : {confusion_matrix(Y_test,Y_Pred)}")
    
    ####################### END OF THE PROGRAM ###########################

if __name__ == "__main__":
    main()