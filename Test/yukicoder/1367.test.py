# verification-helper: PROBLEM https://yukicoder.me/problems/no/1367

def main() -> None:
    s = input()
    t = "kadomatsu"
    ind = 0
    for i in range(9):
        if s[ind] == t[i]:
            ind += 1
        if ind == len(s):
            exit(print("Yes"))
    
    print("No")


if __name__ == "__main__":
    main()