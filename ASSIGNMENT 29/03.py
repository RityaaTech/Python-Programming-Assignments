import sys

def main():
   Source = sys.argv[1]

   #File = input("ENTER THE FILE NAME : ")

   fobj_1 = open(f"{Source}","r")
   Data = fobj_1.read()
   fobj_1.close()

   fobj_2 = open("Marvellous.txt","w")
   fobj_2.write(Data)
   fobj_2.close()


if __name__ == "__main__":
   main()
