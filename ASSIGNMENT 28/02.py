def main():
    fobj = open("Demo.txt","r")
    count = 0

    for line in fobj:
        words = line.split()
        count = count + len(words)

    fobj.close()
    print(f"Total Number of Words : {count}")

if __name__ == "__main__":
    main()