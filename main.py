# python3

def parallel_processing(n, m, data):
    output = []
    thr=[0]*n

    for r in range(m):
        ml=thr[0]
        mt=0
        for g in range(1,n):
            if thr[g]<ml:
                ml=thr[g]
                mt=g
        output.append((mt, ml))
        thr[mt]=(thr[mt]+data[r])

    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    n,m=map(int, input().split())
    data=list(map(int, input().split()))
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line

    for thr,p in result:
        print(thr,p)


if __name__ == "__main__":
    main()
