def max_sum(a,n):
    #find max element in array
    max_ele=-100
    max_index=0
    max_val=0
    for i in range(n):
        if a[i]>max_ele:
            max_ele=a[i]
            max_index=i
    #rotate array such that greatest element goes to the last index
    rot_arr=n-(i+1)
    for i in range(n):
        j=(i+rot_arr)%n
        a[j]=a[i]
    #compute the config
    for i in range(n):
       max_val=max_val+(i*a[i])
    return max_val