def jumpSearch(arr, totalLength,numToFind):
    multiples = totalLength/4
    count=0
    for i in range(1,int(multiples)+1):
            if(numToFind==arr[(i*4)]):
                count+=1
            elif(numToFind<=arr[(int(multiples)*4)] and numToFind<arr[(i*4)]):
                for j in range((i*4)-4,(i*4)):  
                    if(numToFind==arr[j]):   
                        count+=1
    if(numToFind>arr[(int(multiples)*4)] and count==0):
        for k in range(((int(multiples)*4)+1),totalLength):
            if(numToFind==arr[k]):
                count+=1
                break
    return count
arr = [1,2,33,44,66,77,89,91,99,100,123,234,345,555]
count = jumpSearch(arr,len(arr),666)
if(count==1):
    print("Found")
else:
    print("Not Found")