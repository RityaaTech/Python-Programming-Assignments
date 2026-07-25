import sys 

def main():
 File_1 = sys.argv[1] 
 File_2 = sys.argv[2]

 F1 = open(File_1,"r")
 F2 = open(File_2,"r")

 Data_1 = F1.read()
 Data_2 = F2.read()

 F1.close()
 F2.close()

 if (Data_1 == Data_2):
    print("Success")
 else:
    print("Failure")

if __name__ == "__main__":
  main()