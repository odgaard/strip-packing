from spp.ph import phspprg
from spp import visualize
from collections import namedtuple

Rectangle = namedtuple('Rectangle', ['x', 'y', 'w', 'h'])


def main():
    boxes = []
    width = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        width = int(lines[0].rsplit(':')[1].rstrip())
        # print(width)
        for i in range(3, len(lines)-1):
            items = lines[i].rstrip().split(',')
            items[0] = int(items[0])
            items[1] = int(items[1])
            boxes.append(items)
        # print(boxes)

    w_height, w_rectangles = phspprg(width, boxes, "width")
    h_height, h_rectangles = phspprg(width, boxes, "height")
    if w_height < h_height:
        print("The height is: {}".format(w_height))
        visualize(width, w_height, w_rectangles)
    else:
        print("The height is: {}".format(h_height))
        visualize(width, h_height, h_rectangles)


if __name__ == "__main__":
    main()
