def linearSearch(dataIn, inNum, length):
    dummy = 0
    for i in range (0,length): 
        if(dataIn[i] == inNum):
            dummy = inNum
            break;           
    if(dummy==0):
        print("Not Found")
    else:
        print("Found")

number = input("Enter the number")
arr = [10, 20, 80, 30, 60, 50,110, 100, 130, 170]
n = len(arr)
linearSearch(arr,int(number),n)
