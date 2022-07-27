import time
def large(myList,rank=1):
    if len(myList)>=rank:
        l = set(myList)
        l2 = list(l)
        return l2[-rank]
    else:
        return 404
if __name__ == "__main__":
    t0 = time.time()
    l = [5,8,2,10,15,2,4,5,5,6,8,9,1,0,2,-0,8,1,5,7,8,9,6,3,7]
    r=5
    print("orginal list:\t", l)
    maxx = large(l,r)
    print("Max value in rank:\t",r,"\tis:\t",maxx)
    t1 = time.time()
    print(t1 - t0)