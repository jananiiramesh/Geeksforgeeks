class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        union = []
        diff = []
        arr1_set = set(arr1)
        arr2_set = set(arr2)
        for num in arr1_set:
            union.append(num)
        for numb in arr2_set:
            if numb not in arr1_set:
                diff.append(numb)
        union.extend(diff)
        union.sort()
        return union