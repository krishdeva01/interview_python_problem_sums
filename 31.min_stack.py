"""
31. Min Stack
Stack supporting push / pop / top / get_min all in O(1).

Approach: store (value, min-so-far) pairs, so the current min is always the
top pair's second field.
Time: O(1) per op   Space: O(n)

Shortcut: "push (val, min(val, prev_min)) -> get_min = top's min."
"""


class MinStack:
    def __init__(self):
        self.st = []  # list of (val, cur_min)

    def push(self, x):
        cur_min = min(x, self.st[-1][1]) if self.st else x
        self.st.append((x, cur_min))

    def pop(self):
        self.st.pop()

    def top(self):
        return self.st[-1][0]

    def get_min(self):
        return self.st[-1][1]


if __name__ == "__main__":
    s = MinStack()
    s.push(5)
    s.push(2)
    s.push(7)
    print(s.get_min())   # Output: 2
    print(s.top())       # Output: 7
    s.pop()              # remove 7
    print(s.get_min())   # Output: 2
    s.pop()              # remove 2
    print(s.get_min())   # Output: 5
