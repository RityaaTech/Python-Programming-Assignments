# ---------------- IMPORTING MODULES -------------------------
import pandas as pd
import matplotlib.pyplot as plt
# ------------------------------------------------------------

def Assignment44():

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
        "Math" : [np.nan,76,88],
        "Science" : [91,np.nan,85]
    }

    df2 = pd.DataFrame(data2)
    df2.fillna(df2.mean(numeric_only=True),inplace=True)
    print(df2)

    ################## Q10) ##################################

    df_dropped = df.drop(columns=["English"])
    print(df_dropped)

def main():
    Assignment44()

if __name__ == "__main__":
    main()