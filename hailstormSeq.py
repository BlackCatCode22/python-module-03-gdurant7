def main():
    count = 1
    ncount = 0

    n = int(input("Enter the number of students: "))
    print(f"Step: {count} | Number: {n}")

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
        print(f"Step: {count} | Number: {n}")

if __name__ == "__main__":
    main()