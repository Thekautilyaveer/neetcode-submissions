class Solution:
    def isPalindrome(self, s: str) -> bool:
        front, back = 0, len(s)-1

        while front<back:
            if s[front].isalnum() == False :
                front+=1
                continue

            if s[back].isalnum() == False :
                back-=1
                continue

            if s[front].lower() != s[back].lower():
                return False

            front +=1
            back -=1

        return True
            


            