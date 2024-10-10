#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n  # Track which boxes are unlocked
    unlocked[0] = True      # Box 0 is already unlocked
    keys = boxes[0]         # Start with the keys in box 0
    stack = [0]             # Stack to simulate unlocking boxes

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
