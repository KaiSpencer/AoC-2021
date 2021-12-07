from typing import List


def main():
    input_list = [int(line.strip()) for line in open("input.txt").readlines()]

    print(number_of_increased(input_list))


def number_of_increased(input_list: List[int]) -> int:
    count = 0
    for index, number in enumerate(input_list):
        if index == 0:
            continue

        if number > input_list[index - 1]:
            count += 1

    return count


if __name__ == "__main__":
    main()
