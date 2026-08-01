import sys
import os 
import hashlib

def Calculate_CheckSum(File_Name):
    fobj = open(File_Name,"rb")
    hobj = hashlib.md5() 
    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)   # 1024 Bytes = 1 KB

    fobj.close()

    return hobj.hexdigest()

def Find_Duplicate(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if (Ret == False):
        print("Path is Invalid")
        return 

    Ret = os.path.isdir(DirectoryName)

    if (Ret == False):
            print("It is not a Directory")
            return

    Duplicate = {}
  
    for FolderName,Subfolder,Filename in os.walk(DirectoryName):
         for fname in Filename:
              fname = os.path.join(FolderName,fname)

              CheckSum = Calculate_CheckSum(fname)

              #print(f"{fname} : {CheckSum}")

              if CheckSum in Duplicate:
                   Duplicate[CheckSum].append(fname)
              else:
                   Duplicate[CheckSum] = [fname]
                      
    return Duplicate

def Delete_Duplicate(DirectoryName):

     My_Dict = Find_Duplicate(DirectoryName)

     
     Result = list(filter(lambda x : len(x) > 1,My_Dict.values()))

     count = 0
     TotalDeleted = 0

     for value in Result:
        for subvalue in value:
           
           count = count + 1

           if (count>1):
                print(f"DUPLICATE FOUND {subvalue}")
                TotalDeleted = TotalDeleted + 1
                os.remove(subvalue)
        count = 0

     print(f"Total Deleted Files : {TotalDeleted}")
             
def main():
    Data = Delete_Duplicate("Test")

if __name__ == "__main__":
    main()