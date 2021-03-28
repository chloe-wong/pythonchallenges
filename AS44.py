state = "CLOSED"
inputnum = int(input())
for x in range(inputnum):
    print("Door:",state)
    command = input()
    if command == "button_clicked":
        if state == "CLOSED":
            state = "OPENING"

        elif state == "CLOSING":
            state = "STOPPED_WHILE_CLOSING"

        elif state == "OPEN":
            state = "CLOSING"

        elif state == "STOPPED_WHILE_CLOSING":
            state = "OPENING"

        elif state == "STOPPED_WHILE_OPENING":
            state = "CLOSING"

        elif state == "OPENING":
            state = "STOPPED_WHILE_OPENING"

    elif command == "cycle_complete":
        if state == "OPENING":
            state = "OPEN"
        elif state == "CLOSING":
            state = "CLOSED"
print("Door:",state)