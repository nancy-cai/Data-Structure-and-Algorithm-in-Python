# https://leetcode.com/problems/valid-palindrome/

# def isPalindrome(s):
#   trimmedS = ''.join(c for c in s if c.isalnum()).lower()
#   reversedString = ""
#   for i in range(len(trimmedS),0,-1):
#     reversedString += trimmedS[i-1]

#   print(reversedString)
#   print (trimmedS)
#   if trimmedS == reversedString:
#     return True
#   else:
#     return False

def isPalindrome(s):
  newStr = ""
  for c in s:
    if c.isalnum():
      newStr += c.lower()
  return newStr == newStr[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))

# Fastest solution, O(n)
def isPalindromeTwoPointers(s):
  l = 0
  r = len(s)-1
  while l <= r:
    if not s[l].isalnum():
      l += 1
    elif not s[r].isalnum():
      r -= 1
    else: 
      if s[l].lower() == s[r].lower():
        l += 1
        r -= 1
      else:
        return False
  return True

print(isPalindromeTwoPointers("A man, a plan,,^ a canal: Panama"))
    