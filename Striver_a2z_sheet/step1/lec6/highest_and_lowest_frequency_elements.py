"""
Highest / Lowest Frequency Elements
https://www.naukri.com/code360/problems/k-most-occurrent-numbers_625382?leftPanelTabValue=PROBLEM

"""
from typing import List, Dict


def getFrequencies(v: List[int]) -> List[int]:

    freq: Dict[int: int] = {}
    for val in v:
        if val in freq:
            freq[val] +=1
        else:
            freq[val] = 1
    max_freq = max(freq.values())
    min_freq = min(freq.values())

    max_val = min([key for key, value in freq.items() if value==max_freq])
    min_val = min([key for key, value in freq.items() if value==min_freq])

    return [max_val, min_val]



l = [1, 2, 3, 1, 1, 4]
print(getFrequencies(l))

