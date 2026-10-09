# Complexity analyses assume integer arithmetic takes constant time.
# Dictionary and set operations take O(1) average time, but hash
# collisions can make an individual operation O(n).


# Problem 1: Find Most Frequent Element
def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    most_common = numbers[0]

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

        if counts[number] > counts[most_common]:
            most_common = number

    return most_common


"""
Time and Space Analysis for Problem 1:

Best case: O(n). Every number must be checked, even when all values are
identical. An empty list takes O(1) time.

Worst case: O(n²). Many hash collisions could make each dictionary operation
take O(n). With normal hashing behavior, the overall runtime is O(n).

Average case: O(n). Dictionary lookups and insertions take O(1) on average,
and the function visits each number once.

Space complexity: O(k), where k is the number of unique values. This becomes
O(n) when every value is different.

Why this approach? A dictionary tracks frequencies without repeatedly
searching the original list. An empty input returns None, and ties may return
any of the most frequent values, as allowed by the problem.

Could it be optimized? The average O(n) runtime is already optimal because
every value must be examined. Sorting and counting adjacent values would
give O(n log n) worst-case time, avoiding hash-collision slowdowns, but could
modify the input or require a copy. Python's sorting also uses working memory.
"""


# Problem 2: Remove Duplicates While Preserving Order
def remove_duplicates(nums):
    seen = set()
    result = []

    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


"""
Time and Space Analysis for Problem 2:

Best case: O(n). Every value must be examined, even if all values are equal.

Worst case: O(n²). Many hash collisions could make set membership checks and
insertions take O(n) each.

Average case: O(n). Set operations take O(1) on average, and list append takes
O(1) amortized time.

Space complexity: O(k) for the seen set and the returned list, where k is the
number of unique values. In the worst case, this is O(n).

Why this approach? The set makes duplicate checks fast. The result list
preserves the order in which values first appear.

Could it be optimized? Checking membership directly in the result list would
remove the extra set, but could require O(n²) comparisons. The returned list
would still need O(k) space. The current approach trades extra memory for
faster average performance without modifying the input.
"""


# Problem 3: Return All Pairs That Sum to Target
# The input list contains no duplicate values.
def find_pairs_original(nums, target):
    pairs = []

    for first_index in range(len(nums)):
        for second_index in range(first_index + 1, len(nums)):
            if nums[first_index] + nums[second_index] == target:
                pairs.append(
                    (nums[first_index], nums[second_index])
                )

    return pairs


"""
Original Solution Analysis for Problem 3:

Best, worst, and average time: O(n²). Every distinct pair of positions is
checked, regardless of whether any matches are found.

Space: O(1) auxiliary space, excluding the returned pairs. Including the
output, space is O(p), where p is the number of matching pairs.

This approach is simple and avoids a lookup set, but its runtime grows
quickly as the input becomes larger.
"""


def find_pairs(nums, target):
    # Optimization: replace the nested loops with a set of previously seen
    # numbers. Average time improves from O(n²) to O(n), at the cost of
    # O(n) auxiliary space. Hash collisions can still cause O(n²) worst time.
    seen = set()
    pairs = []

    for number in nums:
        complement = target - number

        if complement in seen:
            pairs.append((complement, number))

        seen.add(number)

    return pairs


"""
Time and Space Analysis for Problem 3:

Best case: O(n). The function checks every number, even when no pairs exist.

Worst case: O(n²). Many hash collisions could make each set operation take
O(n), although normal hashing behavior gives O(n) overall time.

Average case: O(n). Each number requires one average O(1) membership check
and one average O(1) insertion.

Space complexity: O(n) auxiliary space for the set. The output requires O(p)
space for p matching pairs. Since the input values are unique, p is at most
n // 2, so total space remains O(n).

Why this approach? The set quickly checks whether a number's complement has
already appeared. Each pair is found only when its second value is visited,
so the same pair is not returned twice.

Could it be optimized? This refactor improves average time from O(n²) to
O(n), while increasing auxiliary space from O(1) to O(n). Sorting and using
two pointers would provide O(n log n) worst-case time without relying on
hashing, but sorting could modify the input or require a copy. Python's
sorting can also require O(n) temporary memory.
"""


# Problem 4: Simulate List Resizing
def add_n_items(n):
    if n < 0:
        raise ValueError("n cannot be negative")

    capacity = 1
    size = 0
    storage = [None] * capacity

    for value in range(n):
        if size == capacity:
            new_capacity = capacity * 2

            print(
                f"Resizing from capacity {capacity} "
                f"to {new_capacity}"
            )

            new_storage = [None] * new_capacity

            for index in range(size):
                new_storage[index] = storage[index]

            storage = new_storage
            capacity = new_capacity

        storage[size] = value
        size += 1

    return storage[:size]


"""
Time and Space Analysis for Problem 4:

Best, worst, and average case: O(n) total for n additions. The same operations
are performed for a given n. Empty input takes O(1) time.

When do resizes happen? Starting at capacity 1, storage doubles when it is
full and another value needs to be added. Resizes occur before additions
number 2, 3, 5, 9, and so on.

Worst case for one append: O(m), where m is the current number of stored
items, because larger storage must be allocated and existing values copied.

Amortized time per append: O(1). Copying happens only occasionally, and its
total cost is spread across all additions.

Space complexity: O(n). During resizing, both old and new storage exist.
The final slice also creates a separate output list of n values and takes
O(n) time, which does not change the total time or space complexity.

Why this approach? Explicit allocation and copying demonstrate how a dynamic
array grows when its capacity is exhausted.

Why does doubling help? The copied values form a geometric series:
1 + 2 + 4 + 8 + ... . The total stays below 2n. Allocating the new storage
also has a geometric total cost, so all additions together take O(n).

Could it be optimized? Since n is known here, allocating n slots immediately
would avoid resizing, but would not demonstrate the required behavior.
For an unknown input size, larger growth factors reduce copying but waste
more capacity. Smaller growth factors save capacity but copy more often.
"""


# Problem 5: Compute Running Totals
def running_total(nums):
    totals = []
    current_total = 0

    for number in nums:
        current_total += number
        totals.append(current_total)

    return totals


"""
Time and Space Analysis for Problem 5:

Best case: O(n). Every number contributes to one output value.

Worst case: O(n) for the complete function. Occasional list resizing does
not change the total linear cost of all appends.

Average case: O(n). The function makes one pass through the input.

Space complexity: O(n) for the returned list. Excluding the output, the
auxiliary space is O(1), using a running sum and loop variable.

Why this approach? Reusing the previous total avoids adding the same earlier
values repeatedly. Recomputing each prefix sum would take O(n²) time.

Could it be optimized? O(n) runtime is optimal because every input value must
be read and every output value produced. Updating the input in place could
avoid allocating an output list, but would change the original data and
would not meet the requirement to return a new list.
"""


def run_tests():
    # Problem 1: normal input, one item, empty input, negatives, and ties.
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
    assert most_frequent([5]) == 5
    assert most_frequent([]) is None
    assert most_frequent([-1, -1, 2]) == -1
    assert most_frequent([1, 2, 1, 2]) in (1, 2)

    # Problem 2: duplicates, empty input, all equal, and all unique.
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([3, 2, 1]) == [3, 2, 1]

    # Problem 3: compare results regardless of pair or output order.
    def normalize_pairs(pairs):
        return {tuple(sorted(pair)) for pair in pairs}

    pair_cases = [
        ([1, 2, 3, 4], 5, {(1, 4), (2, 3)}),
        ([], 5, set()),
        ([1, 2, 3], 100, set()),
        ([-3, -1, 0, 2, 4], 1, {(-3, 4), (-1, 2)}),
        ([4, 3, 2, 1], 5, {(1, 4), (2, 3)}),
        ([5], 10, set()),
        ([-2, 0, 2], 0, {(-2, 2)}),
    ]

    for nums, target, expected in pair_cases:
        original = find_pairs_original(nums, target)
        optimized = find_pairs(nums, target)

        assert normalize_pairs(original) == expected
        assert normalize_pairs(optimized) == expected
        assert len(optimized) == len(expected)

    # Problem 4: empty input, initial capacity, and multiple resizes.
    assert add_n_items(0) == []
    assert add_n_items(1) == [0]
    assert add_n_items(6) == [0, 1, 2, 3, 4, 5]

    try:
        add_n_items(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative n should raise ValueError")

    # Problem 5: normal input, empty input, negatives, and one item.
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_total([]) == []
    assert running_total([-2, 5, -1]) == [-2, 3, 2]
    assert running_total([10]) == [10]
    assert running_total([0, 0]) == [0, 0]

    # Verify that the functions preserve the original input.
    values = [4, 1, 3, 2]
    original_values = values.copy()

    most_frequent(values)
    remove_duplicates(values)
    find_pairs_original(values, 5)
    find_pairs(values, 5)
    running_total(values)

    assert values == original_values

    print("All performance lab tests passed.")


if __name__ == "__main__":
    run_tests()
