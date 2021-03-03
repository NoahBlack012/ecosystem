class Node:
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos

        self.d_start = 0
        self.d_end = 0
        self.val = 0

    def __eq__(self, x):
        return self.pos == x.pos


def a_star(x_len, y_len, animal_pos, food_pos):
    ## Create nodes for animal and food positions ##
    start = Node(None, animal_pos)
    start.d_start = start.d_end = start.val = 0
    end = Node(None, food_pos)

    open = []
    closed = []
    neighbours = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    open.append(start)

    while len(open) > 0:
        current = open[0]
        curr_ind = 0

        for n, i in enumerate(open):
            if i.val < current.val:
                current = i
                curr_ind = n

        open.pop(curr_ind)
        closed.append(current)

        if current == end:
            curr = current
            path = []
            previous = None
            while curr:
                path.append(curr.pos)
                previous = curr
                curr = curr.parent

            path = path[::-1]

            moves = ""
            for n, i in enumerate(path):
                if n == 0:
                    continue

                previous = path[n-1]
                if i[0] > previous[0]:
                    move = "R"
                elif i[0] < previous[0]:
                    move = "L"
                elif i[1] > previous[1]:
                    move = "U"
                else:
                    move = "D"
                moves += move

            return moves

        children = []
        for pos in neighbours:
            pos = [current.pos[0] + pos[0], current.pos[1] + pos[1]]
            if pos[0] < 0 or pos[0] > x_len or pos[1] < 0 or pos[1] > y_len:
                continue

            new = Node(current, pos)
            children.append(new)


        for child in children:
            for closed_child in closed:
                if child == closed_child:
                    continue

            child.d_start = current.d_start + 1
            child.d_end = (child.pos[0] - end.pos[0]) ** 2 + (child.pos[1] - end.pos[1]) ** 2
            child.val = child.d_start + child.d_end
            for open_node in open:
                if child == open_node and child.d_start > open_node.d_start:
                    continue

            open.append(child)

if __name__ == '__main__':
    out = a_star(10, 10, [15, 15], [7, 6])
    print (out)
