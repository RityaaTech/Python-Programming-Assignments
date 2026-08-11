import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)

def main():

    # ==============================================================
    # =============== LOAD THE DATA ================================
    # ==============================================================

    Border = "="*70
    print(Border)
    print(" LOAD THE DATASET ".center(70,"="))
    print(Border,end = "\n")

    Data_Path = "student_performance_ml.csv"

    df = pd.read_csv(Data_Path)

    print("DataSet loaded successfully.")

    print(df.head(5))

    # ==============================================================
    # =============== DATA ANALYSIS ================================
    # ==============================================================
    
    Border = "="*70
    print(Border)
    print(" DATA ANALYSIS ".center(70,"="))
    print(Border,end = "\n")

    print(f"SHAPE OF DATASET : {df.shape}")
    print(f"TOTAL COLUMNS : {list(df.columns)}")

    print("MISSING VALUES PER COLUMN : ")
    print(df.isnull().sum())

    print("CLASS DISTRIBUTION (Species Count) : ")
    print(df["FinalResult"].value_counts())

    print("Statistical Report of DataSet : ")
    print(df.describe())

    ####################################################################
    # Step 3 : Decide Independent and Dependent Variables                  
    ####################################################################

    Border = "="*70
    print(Border)
    print(" DECIDE INDEPENDENT AND DEPENDENT VARIABLES ".center(70,"="))
    print(Border,end = "\n")

    '''
    X : Independent Variables (Features)
    Y : Dependent varables    (Labeles)
    '''

    Features_Columns = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        #"SleepHours"
    ] 

    X = df[Features_Columns]
    Y = df["FinalResult"]

    print(f"X SHAPE : {X.shape}")
    print(f"Y SHAPE : {Y.shape}")

    ####################################################################
    # Step 4 : Visualization of Dataset                  
    ####################################################################

    Border = "="*70
    print(Border)
    print(" VISUALIZATION OF DATASET ".center(70,"="))
    print(Border,end = "\n")

    

    ####################################################################
    # Step 5 : Split the dataset for training and testing                 
    ####################################################################
    
    Border = "="*70
    print(Border)
    print(" SPLIT THE DATASET FOR TRAINING AND TESTING ".center(70,"="))
    print(Border,end = "\n")

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("SPLITTING DATA ACTIVITY DONE : ")
    print(f"X SHAPE : {X.shape}")
    print(f"Y SHAPE : {Y.shape}")

    print(f"X_train : {X_train.shape}")
    print(f"X_test : {X_test.shape}")

    print(f"Y_train : {Y_train.shape}")
    print(f"Y_test : {Y_test.shape}")

    ####################################################################
    # Step 6 : Build the Model                  
    ####################################################################

    Border = "="*70
    print(Border)
    print(" BUILD THE MODEL ".center(70,"="))
    print(Border,end = "\n")

    Model = DecisionTreeClassifier(max_depth=5)

    print("Model gets created successfully..")

    ####################################################################
    # Step 7 : Train the Model                  
    ####################################################################

    Border = "="*70
    print(Border)
    print(" TRAIN THE MODEL ".center(70,"="))
    print(Border,end = "\n")

    Model.fit(X_train,Y_train)
    print("Model gets successfully")

    ####################################################################
    # Step 8 : Evaluate the Model                  
    ####################################################################

    Border = "="*70
    print(Border)
    print(" EVALUATE THE MODEL ".center(70,"="))
    print(Border,end = "\n")

    Y_Pred = Model.predict(X_test)
    print("Model Evaluated Successfully")

    print("EXPECTED ANSWER : ")
    print(Y_test)

    print("PREDICTED ANSWER : ")
    print(Y_Pred)

    ####################################################################
    # Step 9 : Evaluate the Model Performance                  
    ####################################################################

    Border = "="*70
    print(Border)
    print(" EVALUATE THE MODEL ".center(70,"="))
    print(Border,end = "\n")

    Accuracy = accuracy_score(Y_test,Y_Pred)
    print(f"ACCURACY OF THE MODEL : {Accuracy*100} %")

    print("Confusion Matrix")
    Matrix = confusion_matrix(Y_test,Y_Pred)
    print(Matrix)

    print("Model Classification Report.")
    print(classification_report(Y_test,Y_Pred))
    
if __name__ == "__main__":
    main()