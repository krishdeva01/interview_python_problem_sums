"""
33. Daily Temperatures
For each day, how many days until a warmer temperature (0 if none).

Approach: monotonic decreasing stack of indices; when a warmer day arrives,
pop colder days and record the distance.
Time: O(n)   Space: O(n)

Shortcut: "stack of indices (decreasing temps); while cur > temps[top]:
           ans[top] = i - top."
"""


def daily_temperatures(temps):
    res = [0] * len(temps)
    st = []  # indices with decreasing temperatures
    for i, t in enumerate(temps):
        while st and t > temps[st[-1]]:
            j = st.pop()
            res[j] = i - j
        st.append(i)
    return res


if __name__ == "__main__":
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    