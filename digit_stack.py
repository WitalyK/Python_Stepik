def digit_stack(commands):
    a = 0
    stack = []
    summ = 0
    d = {
        "POP" : lambda x: 0 if not x else x.pop(0),
        "PEEK": lambda x: 0 if not x else x[0],
        "PUSH": lambda x: 0 if not x.insert(0, a) else 0
    }
    for command in commands:
        if command.startswith("PUSH"):
            command, a = command[:4], int(command[5:])
        summ += d[command](stack)
    return summ


if __name__ == '__main__':
    print(digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                       "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]))
    print("Example:")
    print(digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                       "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
