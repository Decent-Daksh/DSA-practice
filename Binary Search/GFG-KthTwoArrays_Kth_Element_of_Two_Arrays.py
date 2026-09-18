class Solutin:
    def findKthOfTwoArray(self, a , b,k):
        if len(a)>len(b):
            a,b = b,a
        n , m = len(a), len(b)
        l , r = max(0 , k-m), min(k,n)
        while l<=r:
            left1 = l +(r-l)//2
            left2 = k -left1

            max1 = a[left1-1] if left1>0 else float('-inf')
            min1 = a[left1] if left1 < n else float('inf')
            max2 = b[left2-1] if left2 >0 else float('-inf')
            min2 = b[left2] if left2<m else float('inf')

            if max1<=min2 and max2<=min1:
                return max (max1 , max2)
            elif max1 >min2:
                r = left1 -1
            else:
                l = left1 +1
                