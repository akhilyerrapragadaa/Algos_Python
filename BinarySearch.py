def binarySearch(arr,numToFind, first,last): 
    initHalf = (first+last)/2
    dummy=0
    if(dummy==0):
        dummy=last
    if(initHalf!=last):
        if(numToFind<=arr[int(initHalf)]):
            if(arr[int(initHalf)]==int(numToFind)):
               print("Number Found")
            else:
               binarySearch(arr,numToFind,first,initHalf)      
               
        else:
           if(arr[int(initHalf)]==int(numToFind)):
            print("Number Found")
           else:
            binarySearch(arr,numToFind, initHalf,last)
    else:
        print("Number Not Found")   
def sort(arr):
    dummy=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                dummy = arr[j+1]
                arr[j+1]=arr[j]
                arr[j]= dummy
    
    return arr

arr = [23,54,6,34,22,11,66,87,64]
first =0
binarySearch(sort(arr), 54, first,len(arr))