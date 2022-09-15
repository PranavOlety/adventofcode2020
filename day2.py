def extract_passwords(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

        letters = []
        passwords = []
        nums = []

        for line in lines:
            rule, password = line.split(':')

            passwords.append(password.strip())

            num, letter = rule.split(' ')

            low, high = num.split('-')

            val = int(low), int(high)
            nums.append(val)

            letters.append(letter)

    return nums, letters, passwords


def part_one(filename):
    nums, letters, passwords = extract_passwords(filename)

    def is_valid_password(num_range, char, p):
        count = p.count(char)
        return num_range[0] <= count <= num_range[1]

    return len(list(
        filter(lambda t: t is True, map(lambda n, c, p: is_valid_password(n, c, p), nums, letters, passwords))))


def part_two(filename):
    nums, letters, passwords = extract_passwords(filename)

    def is_valid_password(num_range, char, p):
        return not (not (p[num_range[0] - 1] == char and p[num_range[1] - 1] != char) and not (
                p[num_range[0] - 1] != char and p[num_range[1] - 1] == char))

    return len(list(
        filter(lambda t: t is True, map(lambda n, c, p: is_valid_password(n, c, p), nums, letters, passwords))))


if __name__ == '__main__':
    print(part_one('passwords.txt'))
    print(part_two('passwords.txt'))

