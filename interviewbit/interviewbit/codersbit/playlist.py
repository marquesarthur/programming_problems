def is_old_box(box):
    aux = box.replace("[", "")
    aux = aux.replace("]", "")
    aux = aux.split(" ", 1)[1]

    return not aux.replace(" ", "").isdigit()

def compare_boxes(a, b):
    prefix_a = a.split(" ", 1)[0]
    prefix_b = b.split(" ", 1)[0]

    suffix_a = a.split(" ", 1)[1]
    suffix_b = b.split(" ", 1)[1]


    if suffix_a == suffix_b:
        if prefix_a < prefix_b:
            return -1
        elif prefix_a > prefix_b:
            return 1
    else:
        if suffix_a < suffix_b:
            return -1
        elif suffix_a > suffix_b:
            return 1

    return 0

def sort_old_boxes(boxes):
    return sorted(boxes, cmp=compare_boxes)



def orderedJunctionBoxes(numberOfBoxes, boxList):
    # WRITE YOUR CODE HERE
    old_boxes = []
    new_boxes = []
    for box in boxList:
        if is_old_box(box):
            old_boxes.append(box)
        else:
            new_boxes.append(box)

    result = sort_old_boxes(old_boxes) + new_boxes
    return result


numberOfBoxes = 4
boxList = ["mi2 jog mid pet", "wz3 34 54 398", "a1 alps cow bar", "x4 45 21 7"]


print(orderedJunctionBoxes(numberOfBoxes, boxList))


numberOfBoxes = 6
boxList = ["t2 13 121", "r1 box ape bit", "b4 xi me nu", "br8 eat nin did", "w1 has uni gry", "f3 52 54 31"]


print(orderedJunctionBoxes(numberOfBoxes, boxList))