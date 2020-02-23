def count_positives_sum_negatives(arr):
    """Given an array of integers.

Return an array,
where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array."""

    if len(arr) == 0:
        return arr
    sum2 = sum1 = 0
    mas = []
    for s in arr:
        if s > 0:
            sum1 += 1
        elif s < 0:
            sum2 += s
        elif s == 0:
            continue
    mas.append(sum1)
    mas.append(sum2)
    return mas
