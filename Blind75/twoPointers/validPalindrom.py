class Solution:

    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                string += i.lower()
        length = len(string)
        i = 0
        while(i<=(length-1-i)):
            if string[i]!=string[length-1-i]:
                return False
            i=i+1
        return True

sol = Solution()
res = sol.isPalindrome("A man, a plan, a canal: Panama")
print(res)
