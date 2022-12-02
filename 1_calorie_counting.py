import heapq

# Run in linear time
def calorie_counting(calories):
    cur_max = 0
    best_max = 0
    for amount in calories:
        if amount == "":
            cur_max = 0
            continue
        cur_max += int(amount)
        best_max = max(best_max, cur_max)
    return best_max

# Idk if this is optimal
def calorie_counting_top_n(calories, n):
    min_heap = []
    cur_max = 0
    i = 0
    for amount in calories + [""]:
        if amount == "":
            # Populate initial heap
            if i < n:
                heapq.heappush(min_heap, cur_max)
            else:
                # pop off smallest max calories, compare to current max
                cur_min = heapq.heappop(min_heap)
                if cur_max > cur_min:
                    heapq.heappush(min_heap, cur_max)
                else:
                    heapq.heappush(min_heap, cur_min)
            i += 1
            cur_max = 0
            continue
        cur_max += int(amount)
    return sum(min_heap)


def process_file(filename):
    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
        return lines


if __name__ == '__main__':
    # part 1
    calories = process_file("data/calories.txt")
    print(calorie_counting(calories))
    # part 2
    print(calorie_counting_top_n(calories, 3))
