def solve(s):
    words = []

    for word in s.split(" "):
        words.append(word.capitalize())

    return " ".join(words)


if __name__ == '__main__':
    s = input()
    print(solve(s))
