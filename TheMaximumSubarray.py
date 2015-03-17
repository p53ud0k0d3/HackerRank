def findContiguous(l):
    max_ending_here = max_so_far = 0
    for x in l:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        
    if max_so_far == 0:
        return max(l)
    else:
        return max_so_far
    


def findNonContiguous(l):
    val = 0
    for n in l:
        if n > 0:
            val += n
    if val == 0:
        return max(l)
    else:
        return val

    
def main():
    arr = []
    for _ in xrange(int(raw_input())):
        temp = input()
        arr.append([int(x) for x in raw_input().strip().split()  ])
    for item in arr:
        print "%d %d" % (findContiguous(item), findNonContiguous(item)) 

if __name__ == "__main__":
    main()
