# ---------------- IMPORTING MODULES -------------------------
import pandas as pd
import matplotlib.pyplot as plt
# ------------------------------------------------------------

def Assignment45():

    ################## Q1) ##################################

    data = {
        "Name" : ["Amit","Sagar","Pooja"],
        "Math" : [85,90,78],
        "Science" : [92,88,80],
        "English" : [75,85,82]
    }

    df = pd.DataFrame(data)
    print(f"Shape : {df.shape}")
    print(f"Columns : {df.columns}")
    print(f"Data Types : {df.dtypes}")

    ################## Q2) ##################################

    print(df.describe())

    ################## Q3) ##################################

    df["Total"] = df["Math"] + df["Science"] + df["English"]
    print(df)

    ################## Q4) ##################################

    print(df[df["Science"]>85])

    ################## Q5) ##################################

    df["Name"] = df["Name"].replace("Charlie","Chris")
    print(df)

    ################## Q6) ##################################

    df_sorted = df.sort_values(by="Total",ascending=False)
    print(df)

    ################## Q7) ##################################

    plt.bar(df["Name"],df["Total"])
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.title("Total Marks by student")
    plt.show()

    ################## Q8) ##################################

    Amit_marks = df[df["Name"] == "Amit"][["Math","Science","English"]].values.flatten()
    subjects = ["Math","Science","English"]

    plt.plot(subjects,Amit_marks,marker="o")
    plt.title("Amit Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()

    ################## Q9) ##################################

    data2 = {
        "Name" : ["Amit","Sagar","Pooja"],
        "Math" : [92,76,88],
        "Science" : [91,92,85]
    }

    df2 = pd.DataFrame(data2)
    df2.fillna(df2.mean(numeric_only=True),inplace=True)
    print(df2)

    ################## Q10) ##################################

    df_dropped = df.drop(columns=["English"])
    print(df_dropped)

    ################## Q11) ##################################

    df["Math_Norm"] = (df["Math"] - df["Math"].min() / df["Math"].max() - df["Math"].min())
    print(df[["Name","Math","Math_Norm"]])  

    ################## Q12) ##################################

    df["Gender"] = ["F","M","M"]
    df_encoded = pd.get_dummies(df,columns=["Gender"])
    print(df_encoded)  

    ################## Q13) ##################################

    print(df.groupby("Gender")[["Math","Science","English"]].mean())

    ################## Q14) ##################################

    Sagar = df[df["Name"] == "Sagar"][["Math","Science","English"]].values.flatten()
    labels = ["Math","Science","English"]

    plt.pie(Sagar,labels=labels,autopct='%1.1f%%')
    plt.title("Sagar's Subject wise distribution")
    plt.show()

    ################## Q15) ##################################

    df["Status"] = df["Total"].apply(lambda x : 'Pass' if x >= 250 else 'Fail')
    print(df[["Name","Total","Status"]])

    ################## Q16) ##################################

    print(f"Total Paased : {df[df['Status'] == "Pass"].shape[0]}")

    ################## Q17) ##################################

    df.to_csv("students_result.csv",index=False)

    ################## Q18) ##################################

    plt.hist(df["Math"],bins=5,edgecolor='black')
    plt.title("Distribution of the Math Marks")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

    ################## Q19) ##################################

    df.rename(columns={"Math" : "Mathematics"},inplace=True)
    print(df.head())

    ################## Q20) ##################################

    plt.boxplot(df["English"])
    plt.title("Boxplot of English Marks")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()

def main():
    Assignment45()

if __name__ == "__main__":
    main()