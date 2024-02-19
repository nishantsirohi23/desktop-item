def largest_time_from_digits(arr):
    def is_valid_time(hh, mm):
        return 0 <= hh < 24 and 0 <= mm < 60

    def backtrack(start):
        nonlocal result
        if start == 4:
            hh = int("".join(arr[:2]))
            mm = int("".join(arr[2:]))
            if is_valid_time(hh, mm) and (result is None or hh * 60 + mm > result[0] * 60 + result[1]):
                result = (hh, mm)
            return

        for i in range(start, 4):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]

    result = None
    backtrack(0)

    return f"{result[0]:02d}:{result[1]:02d}" if result is not None else ""

# Example
arr = [0,0,1,0]
print(largest_time_from_digits(arr))
