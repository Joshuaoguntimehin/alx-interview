#!/usr/bin/python3
def canUnlockAll(boxes):
    """Track if each box is unlocked"""
    n = len(boxes)  # Total number of boxes

    # List to track whether each box is unlocked; initially, only box 0 is unlocked
    unlocked = [False] * n  
    unlocked[0] = True  # The first box (box 0) is always unlocked

    # Get the keys from the first box (box 0) to start unlocking other boxes
    keys = boxes[0]

    # Stack to track the boxes to be processed; start with box 0
    stack = [0]

    # Process each box in the stack until there are no more boxes to process
    while stack:
        # Pop the last box added to the stack (LIFO behavior)
        box = stack.pop()

        # Iterate through each key in the current box to unlock more boxes
        for key in boxes[box]:
            # If the key is valid (within the range of available boxes) and the box is still locked
            if key < n and not unlocked[key]:
                unlocked[key] = True  # Mark the box as unlocked
                stack.append(key)     # Add this newly unlocked box to the stack to process its keys later

    # If all boxes are unlocked, return True, otherwise return False
    return all(unlocked)