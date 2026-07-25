def main():
    fobj = open("Demo.txt","r")
    count = 0

    for line in fobj:
        count = count + 1

    fobj.close()
    print(f"Total Number of Lines : {count}")

if __name__ == "__main__":
    main()