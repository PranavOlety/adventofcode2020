def parseTrees(filename):
    with open(filename, 'r') as f:
        trees = list(map(lambda l: list(l.strip()), f.readlines()))

        return trees


def trees_count(filename, y_slope, x_slope):
    trees = parseTrees(filename)

    x, y = 0, 0
    row_length = len(trees[0])

    tree_count = 0
    while x < len(trees):
        if trees[x][y] == '#':
            tree_count += 1

        x, y = x + x_slope, y + y_slope

        y = y % row_length if y >= row_length else y

    return tree_count


def part_one(filename):
    return trees_count(filename, 3, 1)


def part_two(filename):
    return trees_count(filename, 1, 1) * trees_count(filename, 3, 1) * trees_count(filename, 5, 1) * trees_count(
        filename, 7, 1) * trees_count(filename, 1, 2)


if __name__ == '__main__':
    print(part_one('trees.txt'))
    print(part_two('trees.txt'))
