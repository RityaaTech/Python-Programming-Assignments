# ===================== IMPORTING MODULES =================================
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
# =========================================================================

def main():

    # ============= LOAD THE DATASET =================================

    Study_Hours = np.array(([1],[2],[3],[4],[5])) # X
    Marks = np.array([50,55,60,65,70])            # Y

    print(f"Values of the Independent Variables (X) : {Study_Hours}")
    print(f"Values of the Dependent Variables (Y) : {Marks}")

    # =========== CREATE THE MODEL ====================================

    Model = LinearRegression()
    print("Model created successfully.")

    # =========== TRAIN THE MODEL ====================================
    
    Model = Model.fit(Study_Hours,Marks)
    print("Model trained successfully.")

    # =========== TEST THE MODEL ====================================

    print(Model.predict([[6]]))
    print("Model tested successfully.")

    # =========== FIND THE COEFFICIENT AND INTERCEPT ===============

    Coefficient = Model.coef_
    Intercept = Model.intercept_

    print(f"COEFFICIENT OF THE MODEL : {Coefficient}")
    print(f"INTERCEPT OF THE MODEL : {Intercept}")

    # ================================================================

if __name__ == "__main__":
    main()