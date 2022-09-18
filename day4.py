from re import search


def convert_to_raw_passports(filename):
    with open(filename, 'r') as f:
        raw_input = f.read()
        return raw_input.split('\n\n')


def has_required_fields(raw_passport):
    req_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for req in req_list:
        if not (raw_passport.__contains__(req)):
            return False

    return True



def part_one(filename):
    raw_passports = convert_to_raw_passports(filename)
    return len(list(filter(lambda r: has_required_fields(r), raw_passports)))


def convert_to_passport(raw_line):
    input_line = raw_line.replace('\n', ' ')
    passport = {}
    pairs = input_line.split()

    for pair in pairs:
        key, value = pair.split(':')
        passport.update({key: value})

    return passport



def valid_passport(passport):
    def valid_by(p):
        by = int(p.get('byr'))
        return 2002 >= by >= 1920

    def valid_iy(p):
        iy = int(p.get('iyr'))
        return 2020 >= iy >= 2010

    def valid_ey(p):
        ey = int(p.get('eyr'))
        return 2030 >= ey >= 2020

    def valid_hgt(p):

        hgt = p.get('hgt')
        if hgt.__contains__('in') or hgt.__contains__('cm'):
            try:
                num, unit = int(hgt[:-2]), hgt[-2:]

                if unit == 'in':
                    return 59 <= num <= 76
                elif unit == 'cm':
                    return 150 <= num <= 193
                else:
                    return False
            except:
                return False

        else:
            return False

    def valid_hcl(p):
        hcl = p.get('hcl')

        pattern = r'[^\a-f0-9]'
        if hcl[0] == '#':
            return search(pattern, hcl[1:])
        else:
            return False

    def valid_ecl(p):
        ecl = p.get('ecl')
        valid_ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        return ecl in valid_ecls

    def valid_pid(p):
        pid = p.get('pid')

        try:
            if len(pid) == 9:
                return isinstance(int(pid), int)
            else:
                return False
        except:
            return False

    return valid_by(passport) and valid_iy(passport) and valid_ey(passport) and valid_hgt(passport) and valid_hcl(
        passport) and valid_ecl(passport) and valid_pid(passport)



def part_two(filename):
    raw_files = list(filter(lambda r: has_required_fields(r), convert_to_raw_passports(filename)))

    passports = list(map(lambda raw_line: convert_to_passport(raw_line), raw_files))
    print(passports)

    return len(list(filter(valid_passport, passports)))

if __name__ == '__main__':
    print(part_one('passports.txt'))

    print(part_two('passports.txt'))
