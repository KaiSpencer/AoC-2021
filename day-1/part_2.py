from typing import List


def main():
    input_list = [int(line.strip()) for line in open("input.txt").readlines()]

    print(number_of_increases(input_list))


def window_at_index(list_in: List[int], index: int):
    return [list_in[index], list_in[index + 1], list_in[index + 2]]


def sum_increased(window_1: List[int], window_2: List[int]) -> bool:
    return sum(window_1) < sum(window_2)


def number_of_increases(list_in: List[int]) -> int:
    count = 0
    for i in range(len(list_in) - 2):
        if i == 0:
            continue

        if sum_increased(window_at_index(list_in, i - 1), window_at_index(list_in, i)):
            count += 1

    return count


if __name__ == "__main__":
    main()
