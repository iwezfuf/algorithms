def nested_squares(n):
    def isOnSquare(x, y, size, n):
		offset = 2*(n-size)
        offset2 = 4*n-3 - offset - 1
        if x == offset and y >= offset and y <= offset2:
            return True
        if y == offset and x >= offset and x <= offset2:
            return True
        if x == offset2 and y >= offset and y <= offset2:
            return True
        if y == offset2 and x >= offset and x <= offset2:
            return True
        return False
    
    for y in range(4*n-3):
        for x in range(4*n-3):
			if any([isOnSquare(x, y, size, n) for size in range(1, n+1)]): 
                print("#", end="")
            else: print(" ", end="")
        print()
