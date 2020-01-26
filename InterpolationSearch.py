def InterpolationSearch(arr,hi,lo,x, found):
    pos = lo + ( (x-arr[lo])*(hi-lo) / (arr[hi]-arr[lo]) )
    pos = int(pos)
    if(pos<=hi):
        if(arr[pos]==x):
            return found
        elif(arr[pos]<=x):
            InterpolationSearch(arr,pos,lo,x, found)
        elif(arr[pos]>x):
            InterpolationSearch(arr,hi,pos,x, found)
    else:
        found+=1  
arr = [1,2,3,4,5,6,7,8,9,10,11,19,20]
hi = len(arr)-1
lo = 0
found=0
found = InterpolationSearch(arr,hi,lo,27,found)
if(found == 0):
    print("Found")
else:
    print("Not Found")