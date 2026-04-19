def split_even_odd(s: str):
    even_chars= s[::2]
    odd_chars= s[1::2]
    return even_chars, odd_chars
def main():
    t = int(input().strip())
    for i in range(t):
        s= input().strip()
        even, odd = split_even_odd(s)
        print(even, odd)
if __name__ == "__main__":
    main()