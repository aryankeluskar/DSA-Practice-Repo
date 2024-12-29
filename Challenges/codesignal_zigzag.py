def solution(numbers):
    res = []
    for i in range(len(numbers) - 2):
        res.append(isZigzag( [numbers[i], numbers[i+1], numbers[i+2]] ))
        
    return res

def isZigzag(three):
    a = three[0]
    b = three[1]
    c = three[2]
    
    if (a < b and b > c) or (a > b and b < c) :
        return 1
        
    return 0