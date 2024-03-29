import numpy as np
IniPerm = np.arange(128)
FinPerm = np.arange(128)
TAB = np.arange(128)

def swap(array,a,b):
#    print(a,b)
    tmp=array[a]
    array[a]=array[b]
    array[b]=tmp
    return array

for i in range(127):
    IniPerm[i] = (32 * i) % 127

print(IniPerm)
for i in range(127):
    FinPerm[i] =  (4 * i) % 127

for i in range(127):
    TAB[i] = FinPerm[IniPerm[i]]

print(TAB)


# From python reference implementation : https://www.cl.cam.ac.uk/~fms27/serpent/serpent-0.py.html
IPTable = [
    0, 32, 64, 96, 1, 33, 65, 97, 2, 34, 66, 98, 3, 35, 67, 99, 4, 36, 68, 100, 5, 37, 69, 101, 6, 38, 70, 
    102, 7, 39, 71, 103, 8, 40, 72, 104, 9, 41, 73, 105, 10, 42, 74, 106, 11, 43, 75, 107, 12, 44, 76, 108, 13, 45, 77, 109, 14, 46, 78, 
    110, 15, 47, 79, 111, 16, 48, 80, 112, 17, 49, 81, 113, 18, 50, 82, 114, 19, 51, 83, 115, 20, 52, 84, 116, 21, 53, 85, 117, 22, 54, 86, 
    118, 23, 55, 87, 119, 24, 56, 88, 120, 25, 57, 89, 121, 26, 58, 90, 122, 27, 59, 91, 123, 28, 60, 92, 124, 29, 61, 93, 125, 30, 62, 94, 126, 
    31, 63, 95, 127]
FPTable = [
    0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 
    124, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101, 105, 109, 113, 117, 121, 
    125, 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114, 118, 122, 126, 
    3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99, 103, 107, 111, 115, 119, 123, 127]

print(" print(IniPerm == IPTable) ")
for i in range(127):
    print( i , IniPerm[i] , IPTable[i] , IniPerm[i] == IPTable[i]) 

print(" print(FinPerm == FPTable) ")
for i in range(127):
    print( i , FinPerm[i] , FPTable[i] , FinPerm[i] == FPTable[i]) 
