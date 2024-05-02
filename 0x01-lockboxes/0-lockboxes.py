#!/usr/bin/env python3
"""
lockboxes module
"""
def get_item(boxes, index):
    """
    function that get the item in the box
    """
    for item in boxes:
        if item == index:
            return True
        else:
            return False
def canUnlockAll(boxes):
    """
    function that check if boxes can be
    unlocked
    """
    for index in range(0, len(boxes)):
            # if len(boxes[index]) == 1:
                # print("One item in the boxe number: ", index )
            value = boxes[index][0] if boxes[index] else None
            for j in range(0, len(boxes)):
                print(boxes[j], end=' ')
                if boxes[j] == []:
                    print(f'empty')
                else:
                    print(boxes[j][0])
                    if (index != j and boxes[j][0] == index):
                        print(j, index, boxes[j][0], value)
                        print(f'key is found')
            print()
                
            """else:
                print("More than one item in the boxe number: ", index)"""
boxes = [[0], [4], [5], [8], [1]]
canUnlockAll(boxes)