# Problem 1: Find Most Frequent Element
def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    most_common = numbers[0]

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

        if counts[number] > counts.get(most_common, 0):
            most_common = number

    return most_common


"""
Time and Space Analysis for Problem 1:

Best case: O(n). Every number must be checked even if the list contains only
one repeated value. An empty list is a constant-time edge case.

Worst case: O(n). The function makes one pass through all n values.

Average case: O(n), because dictionary lookup and insertion are O(1) on
average for every value.

Space complexity: O(k), where k is the number of unique values. If every value
is unique, this becomes O(n).

Why this approach? A dictionary stores each number with its count, allowing
the most frequent value to be found in one pass.

Could it be optimized? O(n) time is optimal because every item must be read.
Sorting could avoid the dictionary, but it would take O(n log n) time and
might modify the input or require another copy.
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

Best case: O(n). Every value must be examined to preserve its original order.

Worst case: O(n) using the standard average O(1) performance of set
operations. Each value is checked once.

Average case: O(n), with average O(1) membership checks and insertions.

Space complexity: O(n). The seen set and result list may both grow with the
number of unique values.

Why this approach? The set provides fast duplicate checks, while the list
preserves the order in which values first appeared.

Could it be optimized? Memory could be reduced by checking the result list
instead of using a set, but that would increase runtime to O(n²). Modifying
the original list could reduce output memory, but it would destroy the
caller's original data.
"""


# Problem 3: Return All Pairs That Sum to Target
def find_pairs_original(nums, target):
    pairs = []

    for first_index in range(len(nums)):
        for second_index in range(first_index + 1, len(nums)):
            if nums[first_index] + nums[second_index] == target:
                pairs.append(
                    (nums[first_index], nums[second_index])
                )

    return pairs


def find_pairs(nums, target):
    # Optimized version: the original solution checked every possible pair
    # in O(n²) time. This version stores previously seen values in a set,
    # reducing average runtime to O(n) at the cost of O(n) extra space.
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

Best case: O(n). Even if no pairs exist, every value must be checked.

Worst case: O(n) using the expected O(1) performance of set operations.

Average case: O(n), because the algorithm makes one pass through the input
and performs one set lookup and insertion for each number.

Space complexity: O(n). The seen set can contain every input value, and the
returned pairs also require space based on the number of matches.

Why this approach? For each number, a set can quickly determine whether the
needed complement has already appeared.

Could it be optimized? This is the optimized solution. The original nested
loops used O(n²) time and O(1) auxiliary space. The new version uses O(n)
average time but trades O(n) extra memory for that speed. Sorting with two
pointers would take O(n log n) time and could modify the original input,
although it may require less extra memory.
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

Best case: O(n) total for adding n items. Each requested value must be stored.

Worst case: O(n) total for all n additions because the geometric series of
copied values remains below 2n. However, one resizing append can take O(n).

Average case: O(n) total, which equals O(1) amortized time per append.

When do resizes happen? A resize occurs whenever the number of stored items
reaches the capacity. Starting with capacity 1, this happens at sizes 1, 2,
4, 8, and other powers of two.

What is the worst case for one append? O(n), because a resizing append must
create larger storage and copy all existing values.

What is the amortized time per append? O(1). Most appends only place one
value into an available position. The occasional copying cost is spread
across the inexpensive appends.

Space complexity: O(n). The storage grows in proportion to n, but doubling
can temporarily create unused capacity and requires new storage while values
are copied.

Why does doubling reduce the cost? Doubling makes resizing less frequent.
The total number of copied items follows 1 + 2 + 4 + 8 and remains below 2n,
so all n insertions still require only O(n) total work.

Could it be optimized? A larger growth factor would reduce how frequently
resizing occurs but would waste more memory. A smaller factor would save some
unused space but require more frequent copying.
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

Best case: O(n), because each input number contributes to one output value.

Worst case: O(n), since the function always makes one pass through the list.

Average case: O(n) for the same reason.

Space complexity: O(n) for the returned totals list. Excluding the required
output, the additional working space is O(1) because only current_total is
maintained.

Why this approach? Keeping a running sum avoids repeatedly adding all earlier
values. A nested-loop solution would take O(n²) time.

Could it be optimized? The O(n) runtime is already optimal because every input
and output must be handled. The function could modify nums in place for O(1)
auxiliary space, but that would overwrite the caller's original list.
"""


if __name__ == "__main__":
    # Problem 1 tests
    assert most_frequent(
        [1, 3, 2, 3, 4, 1, 3]
    ) == 3
    assert most_frequent([5]) == 5
    assert most_frequent([]) is None
    assert most_frequent([-1, -1, 2]) == -1

    # Problem 2 tests
    assert remove_duplicates(
        [4, 5, 4, 6, 5, 7]
    ) == [4, 5, 6, 7]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 1, 1]) == [1]

    # Problem 3 tests
    pair_input = [1, 2, 3, 4]
    expected_pairs = {(1, 4), (2, 3)}

    assert set(
        find_pairs_original(pair_input, 5)
    ) == expected_pairs

    assert set(
        find_pairs(pair_input, 5)
    ) == expected_pairs

    assert find_pairs([], 5) == []
    assert find_pairs([1, 2, 3], 100) == []

    assert set(
        find_pairs([-3, -1, 0, 2, 4], 1)
    ) == {(-3, 4), (-1, 2)}

    # Problem 4 tests
    assert add_n_items(0) == []
    assert add_n_items(1) == [0]
    assert add_n_items(6) == [0, 1, 2, 3, 4, 5]

    try:
        add_n_items(-1)
        raise AssertionError(
            "A negative value should raise ValueError"
        )
    except ValueError:
        pass

    # Problem 5 tests
    assert running_total(
        [1, 2, 3, 4]
    ) == [1, 3, 6, 10]

    assert running_total([]) == []

    assert running_total(
        [-2, 5, -1]
    ) == [-2, 3, 2]

    assert running_total([10]) == [10]

    print("All performance lab tests passed.")
