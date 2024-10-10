def canVisitAllIslands(islands):
    unlocked = [False] * len(islands)
    unlocked[0] = True
    keys = [0]
    
    for key in keys:
        for new_key in islands[key]:
            if new_key < len(islands) and not unlocked[new_key]:
                unlocked[new_key] = True
                keys.append(new_key)
    return all(unlocked)        
islands = [[1], [2], [3], []]
print(canVisitAllIslands(islands))  # Output: True

islands = [[1, 3], [3, 0, 1], [2], [0]]
print(canVisitAllIslands(islands))  # Output: False