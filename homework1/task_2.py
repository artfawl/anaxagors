class my_list:
    def __init__(self, a: list):
        self.arr = a.copy()

    def __add__(self, other):
        arr1 = self.arr.copy()
        arr2 = other.arr.copy()
        if len(arr1) > len(arr2):
            while len(arr1) != len(arr2):
                arr2.append(0)
        if len(arr1) < len(arr2):
            while len(arr1) != len(arr2):
                arr1.append(0)
        for i in range(len(arr1)):
            arr1[i] += arr2[i]
        return my_list(arr1)

    def __neg__(self):
        arr = self.arr.copy()
        for i in range(len(arr)):
            arr[i] *= (-1)
        return my_list(arr)

    def __sub__(self, other):
        return self + (-other)

    def __eq__(self, other):
        sum1 = 0
        sum2 = 0
        for i in range(len(self.arr)):
            sum1 += self.arr[i]
        for i in range(len(other.arr)):
            sum2 += other.arr[i]
        if sum1 == sum2:
            return True
        return False

    def __ne__(self, other):
        if self == other:
            return False
        return True

    def __lt__(self, other):
        sum1 = 0
        sum2 = 0
        for i in range(len(self.arr)):
            sum1 += self.arr[i]
        for i in range(len(other.arr)):
            sum2 += other.arr[i]
        if sum1 < sum2:
            return True
        return False

    def __le__(self, other):
        sum1 = 0
        sum2 = 0
        for i in range(len(self.arr)):
            sum1 += self.arr[i]
        for i in range(len(other.arr)):
            sum2 += other.arr[i]
        if sum1 <= sum2:
            return True
        return False

    def __gt__(self, other):
        return (-self) < (-other)

    def __ge__(self, other):
        return (-self) <= (-other)

    def __str__(self):
        return self.arr.__str__()

    def __repr__(self):
        return "my_list(" + self.arr.__repr__() + ")"
