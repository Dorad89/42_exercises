#Subject: Given two arrays, determine whether arr2 is a rotation of arr1 
#(i.e. arr2 equals arr1 shifted circularly by some amount).

def arr_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    
    if len(arr1) != len(arr2):
        return False

    if not arr1:
        return True
    
    for i in range(len(arr1)):
        if arr1[i] == arr2[- 1 - i]:
            return True
    return False

# Claude version
def arr_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    if len(arr1) != len(arr2):
        return False
    if not arr1:
        return True
    for i in range(len(arr1)):
        if arr1[i:] + arr1[:i] == arr2:
            return True
    return False

print(arr_rotation_detector([1,2,3,4,5],[1,3,2,4,5]))
print(arr_rotation_detector([1,2,3,4,5],[1,2,3,4]))
print(arr_rotation_detector([],[]))
print(arr_rotation_detector([1,2,3,4,5],[3,4,5,1,2]))
print(arr_rotation_detector([1,2,3,4,5],[2,3,4,5,1]))  # True  → rotacion i 1 pozicionit
print(arr_rotation_detector([1,2,3,4,5],[5,1,2,3,4]))  # True  → rotacion i 4 pozicioneve
print(arr_rotation_detector([1,2,3,4,5],[1,2,3,4,5]))  # True  → rotacion i 0 pozicioneve
print(arr_rotation_detector([1,1,1],[1,1,1]))           # True  → të gjithë njësoj
print(arr_rotation_detector([1,2,3],[3,1,2]))           # True  → rotacion
print(arr_rotation_detector([1,2,3],[2,1,3]))           # False → nuk është rotacion
