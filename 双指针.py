#345. Reverse Vowels of a String
def reverseVowels(s):
    vowels = set(list("aeiouAEIOU"))
    #vowels： {'E', 'u', 'e', 'a', 'A', 'U', 'O', 'o', 'I', 'i'}
    #list can be modified, but str can't
    s = list(s)
    # list( "hello")->['h', 'e', 'l', 'l', 'o']
    i, j = 0, len(s) - 1
    while i<j:
        if s[i] in vowels and s[j] in vowels:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        if s[i] not in vowels:
            i+=1
        if s[j] not in vowels:
            j-=1
    return ''.join(s)

#680. Valid Palindrome II
def validPalindrome(s):
    # s = "cbbcc" --validPalindrome after deleting one char
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:#"bbc"
            #delete_left="bc",delete_right="bb"
            delete_left = s[left+1 : right+1]
            delete_right = s[left : right]
            
            #delete_left or delete_right 有一个是与自己的[::-1]相等，就return true
            return delete_left == delete_left[::-1] or delete_right == delete_right[::-1]
        left += 1
        right -=1
    return True

#88. Merge Sorted Array
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while n:
        # always put the larger one at the end of the merged list, move pointer backwards
        # if m/n is used, move m/n 
        if m and nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else: 
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
            
#141. Linked List Cycle：space:O(1)
def hasCycle(self, head: Optional[ListNode]) -> bool:
    #快指针：一次移动2位；慢指针：一次移动1位
    #如果存在loop，则这俩指针一定会相遇
    fast,slow=head, head
    while fast and fast.next:
        fast, slow=fast.next.next,slow.next
        if fast==slow:
            return True
    return False
