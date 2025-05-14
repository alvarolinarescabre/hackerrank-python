from string import ascii_lowercase

def print_rangoli(size):
    # your code goes here
    alphabet = list(ascii_lowercase[:size])
    alphabet_reversed = alphabet[::-1]

    n = (size - 1) * 4 + 1

    for i in range(1, (size + 1)):
        print("-".join(alphabet_reversed[:i] + ((alphabet_reversed[:i])[::-1])[1:]).center(n, "-"))

    for i in range((size - 1), 0, -1):
        print("-".join(alphabet_reversed[:i] + ((alphabet_reversed[:i])[::-1])[1:]).center(n, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)