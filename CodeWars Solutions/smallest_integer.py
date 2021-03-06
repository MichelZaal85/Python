# input = [[0,2],[1,4,5]] -- 3 is missing, find the smallest missing int.
def smallest_integer(matrix):
    n = set()
    for i in range(len(matrix)):
        for o in matrix[i]:
            n.add(o)
    list(n).sort()
    return n
    # for a in n:



print(smallest_integer([[0,2],[5,1,4]]))
print(smallest_integer([[4, 5, 3, 21, 3, 8], [2, 2, 6, 5, 10, 9], [7, 5, 6, 8, 2, 6], [1, 4, 7, 8, 9, 0], [1, 3, 6, 5, 5, 1], [2, 7, 3, 4, 4, 3]]))


def nums():
    a, b = 0, 0
    for i in l:
        a, b = i, a
        if b > 0 and b + 1 != a:
            return(b + 1)
    return a + 1





'''
some random tests:

[[0, 2], [5, 1]]
-- 3
[[4, 5, 3, 21, 3, 8], [2, 2, 6, 5, 10, 9], [7, 5, 6, 8, 2, 6], [1, 4, 7, 8, 9, 0], [1, 3, 6, 5, 5, 1], [2, 7, 3, 4, 4, 3]]
-- 11
[[4, 5, 3, -4, 3, 8], [2, 0, 6, 5, 4, 9], [7, 5, 6, 8, 2, 6], [1, 4, 7, 8, 9, 11], [1, 3, 10, 5, 5, 1], [12, 7, 3, 4, 4, 3]]
-- 13
[[1, 2], [3, 4]]
-- 0
[[0, 1], [2, 3]]
-- 4
[[4, 5, 13, 0, 3], [2, 6, 5, 10, 9], [7, 5, -6, 8, 6], [1, 4, 7, 8, 9], [2, 3, 4, 44, 3]]
-- 11
[[-1, 100, -1, 100], [100, -1, 100, -1], [-1, 100, -1, 100], [100, -1, 100, -1]]
-- 0
[[-1, -1], [-1, -1]]
-- 0
[[19, 4, 24], [12, 22, 2], [5, 21, 14], [-3, 19, 5], [10, 16, 26], [5, -3, -3], [3, 8, 14], [25, 23, 12], [22, 23, 19]]
-- 0
[[19, 4, 24], [12, 22, 2], [5, 21, 14], [-3, 19, 5], [10, 16, 26], [5, -3, -3], [3, 8, 14], [25, 23, 12], [22, 23, 19]]
[[16, 1, -4, 4, 20, 34], [17, 12, 6, 22, 17, 30], [23, 2, 36, 9, -3, 5], [12, 8, 25, 19, 34, -2], [23, -3, -3, 31, 16, 5], [-2, 32, 20, 3, 20, 36]]
-- 0
[[16, 1, -4, 4, 20, 34], [17, 12, 6, 22, 17, 30], [23, 2, 36, 9, -3, 5], [12, 8, 25, 19, 34, -2], [23, -3, -3, 31, 16, 5], [-2, 32, 20, 3, 20, 36]]
[[15, 20, 7, 7, -2, 20], [-4, 0, 9, 13, 18, 34], [17, 42, 0, 41, 35, 40], [19, 7, 17, 11, 16, 9], [39, 28, -3, 2, 5, 40], [3, 15, 2, 22, 25, -2], [3, 8, 2, 15, 5, 31]]
-- 1
[[15, 20, 7, 7, -2, 20], [-4, 0, 9, 13, 18, 34], [17, 42, 0, 41, 35, 40], [19, 7, 17, 11, 16, 9], [39, 28, -3, 2, 5, 40], [3, 15, 2, 22, 25, -2], [3, 8, 2, 15, 5, 31]]

[[-2, 10, 23, 21, -5, 22, 7, 18], [14, -5, -1, -2, 22, 14, 22, -5], [18, -4, 6, 5, 24, 8, 12, -2]]
-- 0
[[-2, 10, 23, 21, -5, 22, 7, 18], [14, -5, -1, -2, 22, 14, 22, -5], [18, -4, 6, 5, 24, 8, 12, -2]]
[[28, 21, 1, 22, 35, 24, 33, 29, 40], [0, 32, 18, 25, 19, 15, 0, 40, 12], [18, 17, 16, 33, 41, 14, 27, 35, -1], [9, 16, 28, -3, 19, 43, 10, 20, 8], [28, 20, 42, 22, 31, 7, 32, 38, 0]]
-- 2
[[28, 21, 1, 22, 35, 24, 33, 29, 40], [0, 32, 18, 25, 19, 15, 0, 40, 12], [18, 17, 16, 33, 41, 14, 27, 35, -1], [9, 16, 28, -3, 19, 43, 10, 20, 8], [28, 20, 42, 22, 31, 7, 32, 38, 0]]
[[-3, 19, 2], [9, -2, 16], [-4, 9, 2], [6, 3, 9], [-4, -2, 17], [24, 20, -4], [12, 5, -4], [-2, 9, 13]]
-- 0
[[-3, 19, 2], [9, -2, 16], [-4, 9, 2], [6, 3, 9], [-4, -2, 17], [24, 20, -4], [12, 5, -4], [-2, 9, 13]]
[[9, 23, 32, 26], [30, 18, 1, 28], [4, 30, -3, 23], [14, 4, 14, -4], [22, -1, -2, 13], [11, -3, 10, 28], [16, -1, 17, 10], [10, 13, 24, 29]]
-- 0
[[9, 23, 32, 26], [30, 18, 1, 28], [4, 30, -3, 23], [14, 4, 14, -4], [22, -1, -2, 13], [11, -3, 10, 28], [16, -1, 17, 10], [10, 13, 24, 29]]
[[2, 4, 0, 1]]
-- 3
[[2, 4, 0, 1]]
[[-3, 2, -2, 4, -1, -5, 6, 6, -2]]
-- 0
[[-3, 2, -2, 4, -1, -5, 6, 6, -2]]
[[1, 5, 0], [-2, 3, -4]]
-- 2
[[1, 5, 0], [-2, 3, -4]]
[[21, 2, -3, 16], [14, 3, 2, 11], [7, 5, 3, -1], [11, 4, 23, 16], [0, 19, 14, 8], [24, 3, 1, 21]]
-- 6
[[21, 2, -3, 16], [14, 3, 2, 11], [7, 5, 3, -1], [11, 4, 23, 16], [0, 19, 14, 8], [24, 3, 1, 21]]
[[30, -3, 9, 0, 26], [42, 31, 36, 20, 24], [45, 25, -3, -5, -1], [29, 21, 14, 30, 0], [27, -5, 21, 6, -3], [37, 11, 17, 10, 32], [29, 29, 10, 37, 14], [22, 34, 11, 45, 38], [-3, 1, 14, 24, 43]]
-- 2
[[30, -3, 9, 0, 26], [42, 31, 36, 20, 24], [45, 25, -3, -5, -1], [29, 21, 14, 30, 0], [27, -5, 21, 6, -3], [37, 11, 17, 10, 32], [29, 29, 10, 37, 14], [22, 34, 11, 45, 38], [-3, 1, 14, 24, 43]]
[[14, 17], [3, 0], [13, 8], [-5, 10], [7, 4], [1, 10], [3, 10], [-5, 12], [13, -2]]
-- 2
[[14, 17], [3, 0], [13, 8], [-5, 10], [7, 4], [1, 10], [3, 10], [-5, 12], [13, -2]]
[[12, 15, -3], [1, 15, 1], [15, 9, 4], [5, 18, 18], [-2, 4, 14], [-1, 13, 11]]
-- 0
[[12, 15, -3], [1, 15, 1], [15, 9, 4], [5, 18, 18], [-2, 4, 14], [-1, 13, 11]]
[[44, 14, 35, 19, 17], [23, 29, 17, 46, 17], [27, 46, 30, 48, 33], [48, 3, 2, 15, 25], [37, 28, 7, 50, 2], [6, 5, 6, 26, 44], [3, 30, 7, 31, 42], [9, 33, 16, -2, 17], [-1, 15, 7, 20, 6], [15, 50, 49, 10, 32]]
-- 0
[[44, 14, 35, 19, 17], [23, 29, 17, 46, 17], [27, 46, 30, 48, 33], [48, 3, 2, 15, 25], [37, 28, 7, 50, 2], [6, 5, 6, 26, 44], [3, 30, 7, 31, 42], [9, 33, 16, -2, 17], [-1, 15, 7, 20, 6], [15, 50, 49, 10, 32]]
[[-1, -4, -5, 5, -3, -1, 1, 2]]
-- 0
[[-1, -4, -5, 5, -3, -1, 1, 2]]
[[5, 2, -3, 5, 3, -4, 5, -4, -2]]
-- 0
[[5, 2, -3, 5, 3, -4, 5, -4, -2]]
[[15, 21, -2, 4, 35, 26, -4], [37, 48, 39, 47, 45, 17, 13], [44, 20, 46, 26, 36, 11, 36], [51, 51, 17, 15, 9, 52, 29], [38, 10, 21, 52, 44, 50, -1], [33, 52, 31, 56, 29, 53, 56], [49, 12, 17, 12, 37, 17, 35], [1, -3, 18, 9, 33, 45, 39]]
-- 0
[[15, 21, -2, 4, 35, 26, -4], [37, 48, 39, 47, 45, 17, 13], [44, 20, 46, 26, 36, 11, 36], [51, 51, 17, 15, 9, 52, 29], [38, 10, 21, 52, 44, 50, -1], [33, 52, 31, 56, 29, 53, 56], [49, 12, 17, 12, 37, 17, 35], [1, -3, 18, 9, 33, 45, 39]]
[[17, -5], [14, -2], [13, 2], [2, -2], [2, 2], [-5, 9], [1, 9], [-4, 17], [17, 4]]
-- 0
[[17, -5], [14, -2], [13, 2], [2, -2], [2, 2], [-5, 9], [1, 9], [-4, 17], [17, 4]]
[[66, 18, 68, 76, 68, 21, 53, 47, 54, 30], [38, 36, 17, 74, 46, 36, 5, 36, 6, 20], [-5, 26, 66, 68, 22, 3, 18, 75, -2, 5], [65, 10, 71, 79, 11, 56, 33, 51, 39, 60], [72, 13, 48, 67, 35, 67, 58, 1, 58, 51], [35, 37, 46, 79, 13, 46, 2, 76, 10, 65], [43, 28, -2, 2, 66, 1, 18, 68, 8, 4], [5, 21, 49, 26, 72, 44, 62, 10, 60, 9]]
-- 0
[[66, 18, 68, 76, 68, 21, 53, 47, 54, 30], [38, 36, 17, 74, 46, 36, 5, 36, 6, 20], [-5, 26, 66, 68, 22, 3, 18, 75, -2, 5], [65, 10, 71, 79, 11, 56, 33, 51, 39, 60], [72, 13, 48, 67, 35, 67, 58, 1, 58, 51], [35, 37, 46, 79, 13, 46, 2, 76, 10, 65], [43, 28, -2, 2, 66, 1, 18, 68, 8, 4], [5, 21, 49, 26, 72, 44, 62, 10, 60, 9]]
[[35, -3, 10, 37], [9, -5, -4, 18], [37, 10, 37, 20], [5, 32, 9, 35], [2, 31, 29, 17], [23, 38, -2, 10], [37, 16, 28, 27], [26, 21, -4, -3], [9, 33, 17, 40], [-4, -4, 11, 1]]
-- 0
[[35, -3, 10, 37], [9, -5, -4, 18], [37, 10, 37, 20], [5, 32, 9, 35], [2, 31, 29, 17], [23, 38, -2, 10], [37, 16, 28, 27], [26, 21, -4, -3], [9, 33, 17, 40], [-4, -4, 11, 1]]
[[26, -1, 14, -2, 18, 19, 6], [28, 22, 18, 0, 9, 13, -4], [-4, 28, 19, 12, 9, 21, 4], [5, 26, 10, 17, -2, 19, 1]]
-- 2
[[26, -1, 14, -2, 18, 19, 6], [28, 22, 18, 0, 9, 13, -4], [-4, 28, 19, 12, 9, 21, 4], [5, 26, 10, 17, -2, 19, 1]]
[[-2], [6], [1], [3], [6], [0], [6], [-5]]
-- 2
[[-2], [6], [1], [3], [6], [0], [6], [-5]]
[[-4, 2, -2], [10, 5, 5], [4, -1, 0], [8, -1, 6]]
-- 1
[[-4, 2, -2], [10, 5, 5], [4, -1, 0], [8, -1, 6]]
[[46, 1, 47, 23, 18, 1, 34, 29], [42, 37, 41, -5, 31, -2, 1, 12], [22, 16, 13, -1, 13, 46, 3, 44], [34, 19, 37, 27, 7, 7, 12, 13], [37, 5, 19, 47, 0, 30, 35, 8], [38, 5, 24, 18, 44, 0, 43, 20]]
-- 2
[[46, 1, 47, 23, 18, 1, 34, 29], [42, 37, 41, -5, 31, -2, 1, 12], [22, 16, 13, -1, 13, 46, 3, 44], [34, 19, 37, 27, 7, 7, 12, 13], [37, 5, 19, 47, 0, 30, 35, 8], [38, 5, 24, 18, 44, 0, 43, 20]]
[[6, 9, 8], [15, 16, 29], [3, -5, 5], [27, 19, 17], [1, 18, 6], [0, 16, -4], [27, 26, 28], [12, 19, 16], [16, -5, 22], [20, -4, 2]]
-- 4
[[6, 9, 8], [15, 16, 29], [3, -5, 5], [27, 19, 17], [1, 18, 6], [0, 16, -4], [27, 26, 28], [12, 19, 16], [16, -5, 22], [20, -4, 2]]
[[4, 15, 24, 53, 11, 16, 3, 14, 53, -4], [23, 53, 38, -5, 36, -5, 32, 44, 28, 15], [28, 11, 39, 41, 31, -2, 34, -1, 60, 50], [51, 44, 2, 15, -2, 54, 18, 48, 57, 34], [39, 14, 4, 39, 22, 16, 43, 4, 48, 50], [30, 16, 58, 58, 51, 46, 17, 31, 8, 35]]
-- 0
[[4, 15, 24, 53, 11, 16, 3, 14, 53, -4], [23, 53, 38, -5, 36, -5, 32, 44, 28, 15], [28, 11, 39, 41, 31, -2, 34, -1, 60, 50], [51, 44, 2, 15, -2, 54, 18, 48, 57, 34], [39, 14, 4, 39, 22, 16, 43, 4, 48, 50], [30, 16, 58, 58, 51, 46, 17, 31, 8, 35]]
[[2, 12, 19, 6, 9, 1, 8, 9, -1], [-4, 22, 16, 23, 10, 15, -5, 4, 21], [25, 10, -4, 26, 0, 27, 17, 8, 9]]
-- 3
[[2, 12, 19, 6, 9, 1, 8, 9, -1], [-4, 22, 16, 23, 10, 15, -5, 4, 21], [25, 10, -4, 26, 0, 27, 17, 8, 9]]
[[6, -2, 8, -4, 2, -1, -3, 1]]
-- 0
[[6, -2, 8, -4, 2, -1, -3, 1]]
[[26, 37, 14, 55, 14, 61, 55, 74, 74, 12], [8, 17, -2, 41, 80, 68, 43, 44, 32, 31], [9, 38, 73, 47, 66, 2, 69, 30, 59, 29], [13, 73, 8, 76, 13, 30, 70, 55, 12, 53], [79, 43, 14, 6, 27, 74, 31, 51, 42, 57], [51, 64, 14, 70, 31, 49, 70, 74, 25, 12], [54, 26, 65, 1, 61, 12, 23, 17, 20, 30], [78, 36, 63, 76, 32, 76, 80, 33, -4, 61]]
-- 0
[[26, 37, 14, 55, 14, 61, 55, 74, 74, 12], [8, 17, -2, 41, 80, 68, 43, 44, 32, 31], [9, 38, 73, 47, 66, 2, 69, 30, 59, 29], [13, 73, 8, 76, 13, 30, 70, 55, 12, 53], [79, 43, 14, 6, 27, 74, 31, 51, 42, 57], [51, 64, 14, 70, 31, 49, 70, 74, 25, 12], [54, 26, 65, 1, 61, 12, 23, 17, 20, 30], [78, 36, 63, 76, 32, 76, 80, 33, -4, 61]]
[[15, -3, 16, 12, 0, 11, 16, 1], [15, -1, 10, 6, 11, 4, -1, 2]]
-- 3
[[15, -3, 16, 12, 0, 11, 16, 1], [15, -1, 10, 6, 11, 4, -1, 2]]
[[40, 50, 41, -1, -1], [10, 32, 36, 38, 3], [34, 49, 22, 44, 2], [26, 35, 7, -1, 20], [22, 34, 36, 18, 3], [3, 12, 19, 7, 46], [23, 32, 23, 22, 49], [29, -2, 31, 2, 10], [16, -2, 6, 22, 3], [7, 30, 33, 50, 40]]
-- 0
[[40, 50, 41, -1, -1], [10, 32, 36, 38, 3], [34, 49, 22, 44, 2], [26, 35, 7, -1, 20], [22, 34, 36, 18, 3], [3, 12, 19, 7, 46], [23, 32, 23, 22, 49], [29, -2, 31, 2, 10], [16, -2, 6, 22, 3], [7, 30, 33, 50, 40]]
[[4, 9, 17], [8, 10, 3], [16, 2, 6], [12, 6, -1], [7, 12, 10], [10, -2, 2]]
-- 0
[[4, 9, 17], [8, 10, 3], [16, 2, 6], [12, 6, -1], [7, 12, 10], [10, -2, 2]]
[[17, 23, 5], [15, -4, -5], [20, 17, 11], [11, 14, 23], [-4, 24, 17], [12, 18, -4], [7, 23, 13], [13, 1, 24]]
-- 0
[[17, 23, 5], [15, -4, -5], [20, 17, 11], [11, 14, 23], [-4, 24, 17], [12, 18, -4], [7, 23, 13], [13, 1, 24]]
[[4, 22, 23, 16, 43, 14, 17], [46, 41, 16, 43, 28, 5, 43], [47, 21, 16, -2, 12, 42, 27], [3, 29, 2, 37, 45, 48, 39], [40, 44, 43, 4, 15, 4, 40], [38, 36, 27, -4, 20, 22, 22], [45, 31, 18, 16, -5, 16, 29]]
-- 0
[[4, 22, 23, 16, 43, 14, 17], [46, 41, 16, 43, 28, 5, 43], [47, 21, 16, -2, 12, 42, 27], [3, 29, 2, 37, 45, 48, 39], [40, 44, 43, 4, 15, 4, 40], [38, 36, 27, -4, 20, 22, 22], [45, 31, 18, 16, -5, 16, 29]]
[[2, 0]]
-- 1
[[2, 0]]
[[25, 55, 46, -3, 13, 85, 31, 41, 58], [74, 72, 25, 47, -1, 13, 12, 84, 69], [3, 77, 43, 18, 37, -2, 67, 50, 37], [73, 77, -3, 21, 48, 67, 17, 66, 19], [53, -3, 40, 4, 90, 2, 16, 88, 53], [3, 37, 8, 20, 49, 1, 72, 89, 16], [12, 25, 74, 16, 55, 1, 67, 11, 40], [-4, 26, 36, 8, 45, 42, 38, 9, 2], [50, 72, -1, 85, 23, 49, 68, 33, 65], [63, 4, 71, 5, 85, 72, -3, 26, 72]]
-- 0
[[25, 55, 46, -3, 13, 85, 31, 41, 58], [74, 72, 25, 47, -1, 13, 12, 84, 69], [3, 77, 43, 18, 37, -2, 67, 50, 37], [73, 77, -3, 21, 48, 67, 17, 66, 19], [53, -3, 40, 4, 90, 2, 16, 88, 53], [3, 37, 8, 20, 49, 1, 72, 89, 16], [12, 25, 74, 16, 55, 1, 67, 11, 40], [-4, 26, 36, 8, 45, 42, 38, 9, 2], [50, 72, -1, 85, 23, 49, 68, 33, 65], [63, 4, 71, 5, 85, 72, -3, 26, 72]]
[[-3, -5, -4], [-5, 3, -4]]
-- 0
[[-3, -5, -4], [-5, 3, -4]]
[[16, 17, -5], [18, 12, 21], [4, -3, 13], [17, 19, 21], [10, 26, 10], [6, 0, -5], [26, 18, 27], [14, -1, 25], [18, -1, 10]]
-- 1
[[16, 17, -5], [18, 12, 21], [4, -3, 13], [17, 19, 21], [10, 26, 10], [6, 0, -5], [26, 18, 27], [14, -1, 25], [18, -1, 10]]
[[3, 6, 3, -4, 5, -3]]
-- 0
[[3, 6, 3, -4, 5, -3]]
[[35, 55, 38, 1, 39, 15, 8], [51, 8, 1, -1, 6, 49, 23], [39, 57, 47, 5, 3, 23, 29], [2, 18, 34, 33, 15, 52, -2], [48, -2, 2, 25, 61, 55, 9], [39, 15, 42, 17, 55, 14, 55], [29, 19, 47, 34, 34, 45, 60], [-5, 52, 62, 42, 7, -3, 49], [52, 41, 49, 46, 37, 5, 8]]
-- 0
[[35, 55, 38, 1, 39, 15, 8], [51, 8, 1, -1, 6, 49, 23], [39, 57, 47, 5, 3, 23, 29], [2, 18, 34, 33, 15, 52, -2], [48, -2, 2, 25, 61, 55, 9], [39, 15, 42, 17, 55, 14, 55], [29, 19, 47, 34, 34, 45, 60], [-5, 52, 62, 42, 7, -3, 49], [52, 41, 49, 46, 37, 5, 8]]
[[1, -3, -5, -1, 5, -2, 3, -5, 3, -1]]
-- 0
[[1, -3, -5, -1, 5, -2, 3, -5, 3, -1]]
[[-4]]
-- 0
[[-4]]
[[1, -4, -4, 0], [7, 11, -1, 15], [10, 11, -1, 15], [-1, 7, 1, 16]]
-- 2
[[1, -4, -4, 0], [7, 11, -1, 15], [10, 11, -1, 15], [-1, 7, 1, 16]]
[[-4, 8], [5, -1], [-4, 10], [2, -1], [9, 7], [3, 8]]
-- 0
[[-4, 8], [5, -1], [-4, 10], [2, -1], [9, 7], [3, 8]]
[[28, 44, -1, 31, 56, -5, -3, 11, 34, 51], [43, 50, 13, 37, 46, 37, 47, 25, -5, 26], [58, 53, 16, 51, 5, 17, 45, -2, 32, 58], [-5, 40, 52, 28, 37, 37, 11, 53, 14, 54], [10, 24, 12, 16, 3, 33, 17, -1, 26, 5], [53, 58, 20, 35, 47, 22, 31, 56, 0, 45]]
-- 1
[[28, 44, -1, 31, 56, -5, -3, 11, 34, 51], [43, 50, 13, 37, 46, 37, 47, 25, -5, 26], [58, 53, 16, 51, 5, 17, 45, -2, 32, 58], [-5, 40, 52, 28, 37, 37, 11, 53, 14, 54], [10, 24, 12, 16, 3, 33, 17, -1, 26, 5], [53, 58, 20, 35, 47, 22, 31, 56, 0, 45]]
[[8], [1], [5], [2], [2], [5], [1], [2]]
-- 0
[[8], [1], [5], [2], [2], [5], [1], [2]]
[[-4, 11], [15, 13], [14, 3], [16, 11], [-3, 8], [2, 15], [-2, 0], [7, -1]]
-- 1
[[-4, 11], [15, 13], [14, 3], [16, 11], [-3, 8], [2, 15], [-2, 0], [7, -1]]
[[14, 1, 5, -1, 39], [47, 45, 13, 41, 37], [5, 25, 16, 33, 17], [7, 40, 9, 7, 20], [9, 10, 29, 21, -5], [25, 4, 42, 1, -3], [1, 21, 30, 32, 15], [20, 17, 49, 28, 20], [10, -3, 26, 43, 22], [-4, 42, -5, -5, 8]]
-- 0
[[14, 1, 5, -1, 39], [47, 45, 13, 41, 37], [5, 25, 16, 33, 17], [7, 40, 9, 7, 20], [9, 10, 29, 21, -5], [25, 4, 42, 1, -3], [1, 21, 30, 32, 15], [20, 17, 49, 28, 20], [10, -3, 26, 43, 22], [-4, 42, -5, -5, 8]]
[[9, -4, 6, -3, -2, 6, 7, 3, -2]]
-- 0
[[9, -4, 6, -3, -2, 6, 7, 3, -2]]
[[21, 86, 33, 52, 46, 41, 86, 89, 98, 23], [76, 56, 83, 72, 67, -3, 76, 5, 64, 78], [61, 14, 61, 7, 75, 20, 94, 78, 98, 91], [59, 18, 70, 87, 54, 53, 6, 82, 47, 83], [53, 78, 20, 7, 42, 4, 9, 83, 86, 42], [25, 33, 17, 2, 72, 54, 38, 77, 14, 1], [71, 73, 78, 97, 89, 19, 96, 66, 47, 74], [-1, 15, 56, 18, 59, 8, 88, 84, 58, 26], [48, 78, 93, 99, 32, 34, 89, 92, 10, 42], [67, 65, 26, 63, 18, 7, 8, 58, 22, 36]]
-- 0
[[21, 86, 33, 52, 46, 41, 86, 89, 98, 23], [76, 56, 83, 72, 67, -3, 76, 5, 64, 78], [61, 14, 61, 7, 75, 20, 94, 78, 98, 91], [59, 18, 70, 87, 54, 53, 6, 82, 47, 83], [53, 78, 20, 7, 42, 4, 9, 83, 86, 42], [25, 33, 17, 2, 72, 54, 38, 77, 14, 1], [71, 73, 78, 97, 89, 19, 96, 66, 47, 74], [-1, 15, 56, 18, 59, 8, 88, 84, 58, 26], [48, 78, 93, 99, 32, 34, 89, 92, 10, 42], [67, 65, 26, 63, 18, 7, 8, 58, 22, 36]]
[[20, 24, 12, 18, -2, 16, -1], [24, 9, 5, 9, 13, 12, 15], [3, 17, 21, -1, -5, -4, 0], [10, 18, 4, 9, 10, 21, 15]]
-- 1
[[20, 24, 12, 18, -2, 16, -1], [24, 9, 5, 9, 13, 12, 15], [3, 17, 21, -1, -5, -4, 0], [10, 18, 4, 9, 10, 21, 15]]
[[-2, 9], [15, 0], [18, -5], [2, 11], [8, 16], [10, 6], [0, 20], [-5, 13], [18, 2], [11, 1]]
-- 3
[[-2, 9], [15, 0], [18, -5], [2, 11], [8, 16], [10, 6], [0, 20], [-5, 13], [18, 2], [11, 1]]
[[-2, 8, 12, 8, 9, 14], [24, 11, 20, 15, 3, 7], [23, 4, 21, 3, 12, 6], [6, 16, -2, 17, 16, 16]]
-- 0
[[-2, 8, 12, 8, 9, 14], [24, 11, 20, 15, 3, 7], [23, 4, 21, 3, 12, 6], [6, 16, -2, 17, 16, 16]]
[[47, 4, 56, 52, 60, 3], [28, 12, 23, 19, 18, 11], [25, 60, 47, 49, 18, 28], [51, 50, 39, 29, 40, -3], [30, 1, 10, 22, -2, 29], [27, 4, 14, 60, 0, 28], [21, 60, 32, 60, 33, 28], [21, 38, 56, 14, 45, 46], [14, 37, 18, 22, 3, 47], [-5, -3, 26, 38, 39, 39]]
-- 2
[[47, 4, 56, 52, 60, 3], [28, 12, 23, 19, 18, 11], [25, 60, 47, 49, 18, 28], [51, 50, 39, 29, 40, -3], [30, 1, 10, 22, -2, 29], [27, 4, 14, 60, 0, 28], [21, 60, 32, 60, 33, 28], [21, 38, 56, 14, 45, 46], [14, 37, 18, 22, 3, 47], [-5, -3, 26, 38, 39, 39]]
[[12, 55, 8, 54, 65, 40, 3, 14, 48], [47, 1, 8, 19, 71, 58, 70, 66, 75], [29, 48, 63, 0, 13, 81, 22, -2, 62], [41, 45, 5, 89, 62, 5, -3, 0, 86], [63, 62, 55, 13, 32, 88, 23, -2, 74], [33, 58, 67, 51, 49, 74, 67, 60, 10], [61, 49, 80, 21, 15, 41, 10, 83, 41], [17, 26, 13, 51, 63, 4, 61, 35, 25], [74, 39, 26, 45, 0, 21, 10, 45, 15], [70, 39, 54, 82, 21, -4, 83, -3, -3]]
-- 2
[[12, 55, 8, 54, 65, 40, 3, 14, 48], [47, 1, 8, 19, 71, 58, 70, 66, 75], [29, 48, 63, 0, 13, 81, 22, -2, 62], [41, 45, 5, 89, 62, 5, -3, 0, 86], [63, 62, 55, 13, 32, 88, 23, -2, 74], [33, 58, 67, 51, 49, 74, 67, 60, 10], [61, 49, 80, 21, 15, 41, 10, 83, 41], [17, 26, 13, 51, 63, 4, 61, 35, 25], [74, 39, 26, 45, 0, 21, 10, 45, 15], [70, 39, 54, 82, 21, -4, 83, -3, -3]]
[[14, 64, 49, 51, 35, 34, 21, 48], [59, 33, 58, 46, 56, 19, 35, 8], [52, 61, 5, 64, 36, 44, 41, 41], [1, 19, 1, 51, 47, -3, 1, 26], [8, 54, 55, 16, 6, 55, 49, 62], [3, -5, 39, 20, 3, 25, 31, 60], [40, 15, 50, 8, 34, 29, 13, 17], [10, 20, 42, 34, 48, 28, 60, 28]]
-- 0
[[14, 64, 49, 51, 35, 34, 21, 48], [59, 33, 58, 46, 56, 19, 35, 8], [52, 61, 5, 64, 36, 44, 41, 41], [1, 19, 1, 51, 47, -3, 1, 26], [8, 54, 55, 16, 6, 55, 49, 62], [3, -5, 39, 20, 3, 25, 31, 60], [40, 15, 50, 8, 34, 29, 13, 17], [10, 20, 42, 34, 48, 28, 60, 28]]
[[2, 5], [5, -5], [16, -2], [6, 2], [8, 12], [-3, -1], [-3, 9], [6, -1]]
-- 0
[[2, 5], [5, -5], [16, -2], [6, 2], [8, 12], [-3, -1], [-3, 9], [6, -1]]
[[38, 5, 0, 16, 4], [4, 11, 17, 32, 43], [13, 22, 3, 47, 11], [10, -5, 37, 8, 44], [2, 14, 7, 20, 29], [22, 4, 26, 17, 48], [-2, 42, 10, 5, 22], [44, 12, 27, 29, 29], [3, 31, 2, 22, 36], [-3, 39, 46, 49, 37]]
-- 1
[[38, 5, 0, 16, 4], [4, 11, 17, 32, 43], [13, 22, 3, 47, 11], [10, -5, 37, 8, 44], [2, 14, 7, 20, 29], [22, 4, 26, 17, 48], [-2, 42, 10, 5, 22], [44, 12, 27, 29, 29], [3, 31, 2, 22, 36], [-3, 39, 46, 49, 37]]
[[7, 2, 3, -3, 4, 2, 1, -2]]
-- 0
[[7, 2, 3, -3, 4, 2, 1, -2]]
[[-2], [0], [-3], [-3], [-5], [-3]]
-- 1
[[-2], [0], [-3], [-3], [-5], [-3]]
[[3, 8, 1, -1, 6, 10, 2], [10, 19, 3, 1, 11, -3, -3], [-2, 2, 13, 14, -2, 1, 13]]
-- 0
[[3, 8, 1, -1, 6, 10, 2], [10, 19, 3, 1, 11, -3, -3], [-2, 2, 13, 14, -2, 1, 13]]
[[12, 7, 6, 11, 18, 1], [12, 12, 12, 13, 14, -2], [16, 3, 2, -3, 2, -2]]
-- 0
[[12, 7, 6, 11, 18, 1], [12, 12, 12, 13, 14, -2], [16, 3, 2, -3, 2, -2]]
[[0]]
-- 1
[[0]]
[[0, 6], [-5, -5], [2, 0]]
-- 1
[[0, 6], [-5, -5], [2, 0]]
[[-5], [5], [-2], [5], [5]]
-- 0
[[-5], [5], [-2], [5], [5]]
[[5, -4], [15, 13], [1, 16], [3, 4], [-3, 15], [0, -5], [-1, 15], [-5, 1]]
-- 2
[[5, -4], [15, 13], [1, 16], [3, 4], [-3, 15], [0, -5], [-1, 15], [-5, 1]]
[[10, 2, 11, 21, 14, 16, 4], [10, 19, 13, 14, -3, 19, 0], [1, 5, 16, 12, 6, 8, 14]]
-- 3
[[10, 2, 11, 21, 14, 16, 4], [10, 19, 13, 14, -3, 19, 0], [1, 5, 16, 12, 6, 8, 14]]
[[-4, 4], [1, 4]]
-- 0
[[-4, 4], [1, 4]]
[[7, 12, 34, 36], [30, 11, 11, 17], [1, 22, -3, 23], [12, 27, 20, -2], [2, -3, 11, 8], [25, 26, 17, 9], [21, 3, 12, 6], [19, 11, 11, 24], [-2, 6, 11, 25]]
-- 0
[[7, 12, 34, 36], [30, 11, 11, 17], [1, 22, -3, 23], [12, 27, 20, -2], [2, -3, 11, 8], [25, 26, 17, 9], [21, 3, 12, 6], [19, 11, 11, 24], [-2, 6, 11, 25]]
[[-1, 5, 0, 19, 20, -3, 3, 26, 8], [24, 10, 0, 18, 22, -3, 7, -5, 11], [-2, 15, -3, -3, 9, 21, 18, 15, 5]]
-- 1
[[-1, 5, 0, 19, 20, -3, 3, 26, 8], [24, 10, 0, 18, 22, -3, 7, -5, 11], [-2, 15, -3, -3, 9, 21, 18, 15, 5]]
[[6, 3], [4, 3], [10, 5], [-4, 2], [0, 12], [1, 0]]
-- 7
[[6, 3], [4, 3], [10, 5], [-4, 2], [0, 12], [1, 0]]
[[-4, -5, -4, 4], [-4, -4, 1, 5]]
-- 0
[[-4, -5, -4, 4], [-4, -4, 1, 5]]
[[1, -3], [3, 0], [-2, 0]]
-- 2
[[1, -3], [3, 0], [-2, 0]]
[[6, 7], [4, 0], [4, 8], [5, 10], [5, 7]]
-- 1
[[6, 7], [4, 0], [4, 8], [5, 10], [5, 7]]
[[5, 13, 14, 9, 41, 1, 27], [9, 0, 41, 38, 33, 18, 19], [23, 17, 10, 31, 25, 42, 19], [-1, 10, 1, 7, -4, 6, 16], [15, 36, 17, -4, 40, 10, -2], [31, 42, 2, 8, 16, 10, 13]]
-- 3
[[5, 13, 14, 9, 41, 1, 27], [9, 0, 41, 38, 33, 18, 19], [23, 17, 10, 31, 25, 42, 19], [-1, 10, 1, 7, -4, 6, 16], [15, 36, 17, -4, 40, 10, -2], [31, 42, 2, 8, 16, 10, 13]]
[[0, -2, 9], [14, 6, -5], [10, -2, 14], [2, -2, -4], [-4, 5, 12]]
-- 1
[[0, -2, 9], [14, 6, -5], [10, -2, 14], [2, -2, -4], [-4, 5, 12]]
[[5], [5], [0], [7], [0], [2], [7]]
-- 1
[[5], [5], [0], [7], [0], [2], [7]]
[[1, 37, 29, 7, 11, 20, 48], [-2, 8, 60, 60, 57, 34, 55], [29, 57, 21, 10, 28, 25, 40], [21, 67, 51, 40, 32, 3, 34], [13, 16, -3, 12, 18, 1, -1], [44, 39, 8, 31, 18, 38, 57], [38, 51, 39, -4, 62, 3, 5], [20, 61, 20, 43, 6, 23, 54], [9, 56, 21, 33, 62, 61, 1], [24, 47, 40, 67, 52, 21, 33]]
-- 0
[[1, 37, 29, 7, 11, 20, 48], [-2, 8, 60, 60, 57, 34, 55], [29, 57, 21, 10, 28, 25, 40], [21, 67, 51, 40, 32, 3, 34], [13, 16, -3, 12, 18, 1, -1], [44, 39, 8, 31, 18, 38, 57], [38, 51, 39, -4, 62, 3, 5], [20, 61, 20, 43, 6, 23, 54], [9, 56, 21, 33, 62, 61, 1], [24, 47, 40, 67, 52, 21, 33]]
[[43, 25, 35, 45, 21, 8, 0, 35, -4], [2, 30, 32, -1, 23, 32, 12, 39, 3], [5, 26, 16, 11, 5, 1, 24, -1, -5], [-5, 4, 38, 16, 20, 11, 21, 6, 7], [9, 2, 31, 30, 27, 36, 28, 21, 41]]
-- 10
[[43, 25, 35, 45, 21, 8, 0, 35, -4], [2, 30, 32, -1, 23, 32, 12, 39, 3], [5, 26, 16, 11, 5, 1, 24, -1, -5], [-5, 4, 38, 16, 20, 11, 21, 6, 7], [9, 2, 31, 30, 27, 36, 28, 21, 41]]
[[10, 5, 4, 4, -2, -4, 0, 7, 3, -3]]
-- 1
[[10, 5, 4, 4, -2, -4, 0, 7, 3, -3]]
[[18, 10, 16, 17, 16, 7, 41], [49, 49, 37, 11, 14, 30, -2], [11, 43, 41, 21, 18, -1, 37], [16, 48, 32, 12, 14, -4, 11], [0, 26, 5, 27, 43, 40, 43], [40, 23, 25, 43, 14, 47, 44], [10, 48, 33, -1, 18, 26, 18]]
-- 1
[[18, 10, 16, 17, 16, 7, 41], [49, 49, 37, 11, 14, 30, -2], [11, 43, 41, 21, 18, -1, 37], [16, 48, 32, 12, 14, -4, 11], [0, 26, 5, 27, 43, 40, 43], [40, 23, 25, 43, 14, 47, 44], [10, 48, 33, -1, 18, 26, 18]]
[[11, 0, 22, 38, 31, 39, 27, 7], [19, 24, 42, 33, 17, -2, 20, 48], [-3, 39, 33, 26, 21, 48, 0, 27], [-1, 40, 40, 26, 43, -4, 22, 32], [33, 26, 14, 14, 23, 0, 42, 6], [9, 8, -3, 29, 21, 42, 41, 21]]
-- 1
[[11, 0, 22, 38, 31, 39, 27, 7], [19, 24, 42, 33, 17, -2, 20, 48], [-3, 39, 33, 26, 21, 48, 0, 27], [-1, 40, 40, 26, 43, -4, 22, 32], [33, 26, 14, 14, 23, 0, 42, 6], [9, 8, -3, 29, 21, 42, 41, 21]]
[[6, 3, 8, 12], [-4, 4, 11, 1], [14, 16, 1, 0], [16, 10, 16, -1]]
-- 2
[[6, 3, 8, 12], [-4, 4, 11, 1], [14, 16, 1, 0], [16, 10, 16, -1]]
[[2, 40, 38, -4, 22], [28, 6, 36, 21, -5], [22, 39, 30, 29, 37], [19, 11, -5, 7, 29], [27, 23, 6, 13, -4], [39, 28, -5, -3, 35], [16, 23, 34, 29, -2], [25, 31, 31, -2, 12]]
-- 0
[[2, 40, 38, -4, 22], [28, 6, 36, 21, -5], [22, 39, 30, 29, 37], [19, 11, -5, 7, 29], [27, 23, 6, 13, -4], [39, 28, -5, -3, 35], [16, 23, 34, 29, -2], [25, 31, 31, -2, 12]]
[[15, 26, 10, 28, 9, 16], [2, 10, 2, 23, 14, 18], [-3, 28, 23, 20, 14, 29], [-3, 5, 8, 7, 20, -3], [4, 2, 10, 17, 3, 12]]
-- 0
[[15, 26, 10, 28, 9, 16], [2, 10, 2, 23, 14, 18], [-3, 28, 23, 20, 14, 29], [-3, 5, 8, 7, 20, -3], [4, 2, 10, 17, 3, 12]]
[[2, 2, 5, 2, -1, 0, -1, 8]]
-- 1
[[2, 2, 5, 2, -1, 0, -1, 8]]
[[36, 12, 14, 11, 32, 8, -1, 9, 11, 6], [-1, 9, 13, 0, 18, 6, 21, 10, 36, 11], [27, 30, 14, 28, 38, 2, 26, 19, 29, -3], [15, -5, 11, 31, 14, 6, 27, 28, 38, 26]]
-- 1
[[36, 12, 14, 11, 32, 8, -1, 9, 11, 6], [-1, 9, 13, 0, 18, 6, 21, 10, 36, 11], [27, 30, 14, 28, 38, 2, 26, 19, 29, -3], [15, -5, 11, 31, 14, 6, 27, 28, 38, 26]]
[[9, 58, 12, 46, 49, 37, 37, 54], [61, 44, 21, 7, 45, 17, 39, 51], [58, 62, 10, 24, 6, 36, 49, 60], [36, 39, 22, -4, 15, 34, 59, -4], [62, 7, 5, 8, 61, 18, 34, 37], [-5, 47, 58, 10, -2, 9, 60, 26], [13, 6, 2, 60, 50, 60, 12, 30], [7, 19, 27, 39, 59, -5, 64, -4]]
-- 0
[[9, 58, 12, 46, 49, 37, 37, 54], [61, 44, 21, 7, 45, 17, 39, 51], [58, 62, 10, 24, 6, 36, 49, 60], [36, 39, 22, -4, 15, 34, 59, -4], [62, 7, 5, 8, 61, 18, 34, 37], [-5, 47, 58, 10, -2, 9, 60, 26], [13, 6, 2, 60, 50, 60, 12, 30], [7, 19, 27, 39, 59, -5, 64, -4]]
[[-1, 11, 11, 15, 6, 1, 16, -5], [15, 7, 12, 3, 0, 2, 0, -5]]
-- 4
[[-1, 11, 11, 15, 6, 1, 16, -5], [15, 7, 12, 3, 0, 2, 0, -5]]
[[-1, 17, 21, 4, 29, 26], [-1, 11, -4, -4, 26, 24], [26, 24, 36, 12, 6, 7], [-1, 27, 2, 28, 1, 4], [36, 11, 25, 0, 26, 15], [-4, 33, 5, -2, 6, -2]]
-- 3
[[-1, 17, 21, 4, 29, 26], [-1, 11, -4, -4, 26, 24], [26, 24, 36, 12, 6, 7], [-1, 27, 2, 28, 1, 4], [36, 11, 25, 0, 26, 15], [-4, 33, 5, -2, 6, -2]]
[[20, 10, 8, 10, -1, -5, 26], [-5, 13, 13, 8, 23, 28, 25], [24, 5, 26, 14, 4, 24, 27], [2, 8, 7, 27, 22, -3, 23]]
-- 0
[[20, 10, 8, 10, -1, -5, 26], [-5, 13, 13, 8, 23, 28, 25], [24, 5, 26, 14, 4, 24, 27], [2, 8, 7, 27, 22, -3, 23]]
[[23, 5, 3, 23, 17], [28, 7, 22, 29, 14], [28, 28, 6, 16, 29], [-4, 21, -4, 20, 30], [11, 21, 25, 8, 27], [19, -3, -4, -2, 20]]
-- 0
[[23, 5, 3, 23, 17], [28, 7, 22, 29, 14], [28, 28, 6, 16, 29], [-4, 21, -4, 20, 30], [11, 21, 25, 8, 27], [19, -3, -4, -2, 20]]
[[69, 27, 54, 46, 63, 55, 63, 61, 39], [-4, 47, 35, 23, 57, 3, 79, 78, 7], [73, 30, 66, 52, 44, 20, 35, 4, 58], [1, 70, 63, 58, 60, 60, 24, 12, 53], [77, 2, 76, 70, 4, 70, 65, -2, 26], [56, 80, 36, 34, 17, 55, -4, 34, 79], [49, 1, 39, 53, 22, 15, 57, 2, 3], [26, 1, 30, 22, 30, 66, 59, 13, 51], [34, 68, 57, 74, 51, 48, 8, 69, 47]]
-- 0
[[69, 27, 54, 46, 63, 55, 63, 61, 39], [-4, 47, 35, 23, 57, 3, 79, 78, 7], [73, 30, 66, 52, 44, 20, 35, 4, 58], [1, 70, 63, 58, 60, 60, 24, 12, 53], [77, 2, 76, 70, 4, 70, 65, -2, 26], [56, 80, 36, 34, 17, 55, -4, 34, 79], [49, 1, 39, 53, 22, 15, 57, 2, 3], [26, 1, 30, 22, 30, 66, 59, 13, 51], [34, 68, 57, 74, 51, 48, 8, 69, 47]]
[[0, 4, 12, 14, 4, 8, 3], [2, 7, 10, 7, 9, 4, 8]]
-- 1
[[0, 4, 12, 14, 4, 8, 3], [2, 7, 10, 7, 9, 4, 8]]
[[3, -4, 4, 1]]
-- 0
[[3, -4, 4, 1]]
[[1, 29, 42, 38, 23, 37, 40, 25, 27, 46], [47, -4, 1, 41, 10, 9, 44, 44, 9, 27], [49, 17, 18, 19, 1, 44, 33, 7, 42, 34], [43, 44, 39, 39, 34, 17, 38, 31, 45, 8], [13, 36, 15, 43, 17, 7, -1, 21, 3, 43]]
-- 0
[[1, 29, 42, 38, 23, 37, 40, 25, 27, 46], [47, -4, 1, 41, 10, 9, 44, 44, 9, 27], [49, 17, 18, 19, 1, 44, 33, 7, 42, 34], [43, 44, 39, 39, 34, 17, 38, 31, 45, 8], [13, 36, 15, 43, 17, 7, -1, 21, 3, 43]]
[[3, 15, 32, -2, 5, 48], [21, 42, 16, 26, 44, 20], [32, 11, 47, 4, 39, 0], [-1, 16, 5, 17, 42, 41], [13, 45, 28, 0, 15, 17], [32, 24, 18, 12, -4, 8], [33, 4, 27, 13, 28, 4], [-1, 30, -5, 24, 23, 34]]
-- 1
[[3, 15, 32, -2, 5, 48], [21, 42, 16, 26, 44, 20], [32, 11, 47, 4, 39, 0], [-1, 16, 5, 17, 42, 41], [13, 45, 28, 0, 15, 17], [32, 24, 18, 12, -4, 8], [33, 4, 27, 13, 28, 4], [-1, 30, -5, 24, 23, 34]]
[[16, -1, 12, 2], [-4, -5, -3, 13], [8, 16, 10, 15], [-2, 0, -4, 14]]
-- 1
[[16, -1, 12, 2], [-4, -5, -3, 13], [8, 16, 10, 15], [-2, 0, -4, 14]]
[[1, -1], [-4, 6], [0, -3]]
-- 2
[[1, -1], [-4, 6], [0, -3]]

'''