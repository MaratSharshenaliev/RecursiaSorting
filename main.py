from typing import List, Union
import datetime


def summ(arr: List[Union[List, int]] = None):
    __score: int = 0
    for i in arr:
        if type(i) == list:
            __score += summ(i)
        elif type(i) == int:
            if i < 0:
                __score += 1
    return __score


class Sorting:
    sortd = []

    def minNumberInArr(self, arr: List[int], target: int = 0, index: int = 0) -> dict[str, int]:
        if len(arr) <= 1:
            return {"__index": index, "Min": arr[target]}
        ress = self.minNumberInArr(arr=arr[target + 1:], index=index + 1)
        return {"__index": index, "Min": arr[target]} if arr[target] <= ress["Min"] else ress

    def exaclySort(self, arr: List[int]):
        newlist = []
        while arr:
            __index = self.minNumberInArr(arr)
            newlist.append(arr.pop(__index["__index"]))
        return newlist


arr = [0, 24, 5, 35, 6, 7, 8, 2, 5, 35, 6, 6, 7, 4, 3, 2, 3, 6, 5, 73, 2354, 46, 757, 346, 235, 32343]
start_time_Myself = datetime.datetime.now()
example = Sorting()
ex = example.exaclySort(arr)
end_time = datetime.datetime.now()


print("Algoritm: ", end_time - start_time_Myself)

start_time_Sorted = datetime.datetime.now()
arr = sorted(arr)
end_time = datetime.datetime.now()
print("Sorted: ", end_time - start_time_Sorted)

"""
    Algoritm:  0:00:00.000155 ms
    Sorted:  0:00:00.000002 ms
    
    😂👎🏻
"""
