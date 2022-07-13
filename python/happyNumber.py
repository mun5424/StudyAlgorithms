def happyNumber(n) -> bool: 

    currSum = 0
    numSet = set()
    while True:
        currSum = 0
    
        while n >= 1:
            digit = n % 10
            currSum += digit * digit
            n /= 10
        if n in numSet:
            return False
        numSet.add(n)
        if n == 1:
            return True
        
