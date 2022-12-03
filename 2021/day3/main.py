import pathlib

INPUT_FILE="input"

def bit_not(n, numbits=8):
    # https://stackoverflow.com/a/31151236
    return (1 << numbits) - 1 - n

def part1(data):
    num_bits = len(data[0])
    bit_counts = [0] * num_bits

    for num in data: 
        for i, c in enumerate(num):
            bit_counts[i] += int(c)

    half = len(data) / 2
    result = map(lambda x: 1 if x > half else 0, bit_counts)

    b = ''.join(str(e) for e in result)
    gamma = int(b, 2)
    epsilon = bit_not(gamma, num_bits)

    print(gamma, epsilon, gamma * epsilon)

def part2(data):
    num_bits = len(data[0])

    def get_rating(numbers, criteria): 
        bit_position = 0
        while bit_position < num_bits:
            bit_count = 0
            for num in numbers: 
                bit_count += int(num[bit_position])

            half = len(numbers) / 2
            keep = "1" if criteria(bit_count, half) else "0"
            numbers = list(filter(lambda n: n[bit_position] == keep, numbers))

            if len(numbers) == 1: 
                b = ''.join(str(e) for e in numbers[0])
                return int(b, 2)

            bit_position += 1

    o = get_rating(data, lambda bit_count, half: bit_count >= half)
    co2 = get_rating(data, lambda bit_count, half: bit_count < half)

    print(o, co2, o * co2)

if __name__ == "__main__":
    lines = pathlib.Path(INPUT_FILE).read_text().strip().split("\n")

    part1(lines)
    part2(lines)