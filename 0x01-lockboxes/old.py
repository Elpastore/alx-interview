#!/usr/bin/env python3
"""
lockboxes module
"""
def get_item(boxes, index):
    """
    function that get the item in the box
    """
    boolen = False
    for item in boxes:
        if item == index:
            boolen = True
            break
        else:
            boolen = False
    return boolen
def canUnlockAll(boxes):
    """
    function that check if boxes can be
    unlocked
    """
    
    for index in range(0, len(boxes)):
        checked = False
        # if len(boxes[index]) == 1:
            # print("One item in the boxe number: ", index )
        value = boxes[index][0] if boxes[index] else None
        for j in range(0, len(boxes)):
            #print(boxes[j], end=' ')
            if (j != index and get_item(boxes[j], index) == True):
                print(f'key of {boxes[index]} is found')
                checked = True
                break
            if (j != index and get_item(boxes[j], index) == False):
                print("locked boxe")
        print()
    return checked

boxes = [[5], [4], [7], [8], [9]]
print(canUnlockAll(boxes))

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))