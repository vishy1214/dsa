class ContainsDuplicates:
    '''
      Time complexity: O(nlogn)   logn --> for sorting and n for iteration
      space complexity: O(n)
    '''
    def approach1_using_sort(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i] == nums[i-1]):
                return True
        return False


    '''
    Time Complexity : O(N)
    Space Complexity : O(N)
    '''
    def approach2_using_hashset(self,nums):
        uniq_num = set()
        for i in range(len(nums)):
            if nums[i] in uniq_num:
                return True
            uniq_num.add(nums[i])
        return False


if __name__  == '__main__':
    cd = ContainsDuplicates()
    print(cd.approach1_using_sort([1,2,3,4]))  # False
    print(cd.approach1_using_sort([1,2,3,1]))  # True


    print(cd.approach2_using_hashset([1,2,3,4])) # False
    print(cd.approach2_using_hashset([1,2,3,1])) # True



