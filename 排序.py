def shell_sort(arr:list,size:int)->None:
    size:int=size
    gap=size
    while gap>1:
        gap=gap//3+1
        for i in range(0,size-gap):
            end=i
            temp=arr[end+gap]
            while end>=0 and arr[end]>temp:
                arr[end+gap]=arr[end]
                end-=gap
            arr[end+gap]=temp

def print_sort(arr)->None:
    for i in arr:
        print(i,end=" ")
    print()

arr=[5,3,2,4,1]
shell_sort(arr,len(arr))
print_sort(arr)
