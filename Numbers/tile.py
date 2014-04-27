# Find Cost of Tile to Cover W x H Floor - Calculate
# the total cost of tile it would take to cover a floor
# plan of width and height, using a cost entered by the user.

# Use input as the input can be integer and float
# cost = input("What's the cost per sq. feet? ")
# width = input("What's the width of the floor? ")
# height = input("What's the height of the floor? ")
#
# print "The total cost is $%.2f for %.2f square feet" \
#       % (width * height * cost, width * height)


def total_cost(length, width, cost):
    return length * width * cost

if __name__ == "__main__":
    while True:
        l = raw_input("Enter your length: ")
        if not l.isdigit():
            print("Not a valid length")
        else:
            break
    while True:
        w = raw_input("Enter your width: ")
        if not w.isdigit():
            print("Not a valid width")
        else:
            break
    while True:
        c = raw_input("Enter your unit cost: ")
        if not c.isdigit():
            print("Not a valid cost")
        else:
            break
    print "Your total cost is {}".format(total_cost(int(l), int(w), int(c)))