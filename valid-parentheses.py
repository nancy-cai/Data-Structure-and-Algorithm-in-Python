# https://leetcode.com/problems/valid-parentheses/

def isValid(s):
  stack = []
  dict = {')':'(', '}':'{', ']':'['}
  for c in s:
    if c in dict: # It checks c against the keys in the dict, which are closing parenthese
      print('last element in stack is ' + stack[-1])
      print('Value of the current key is ' + dict[c])
      if stack and stack[-1] == dict[c]: # If stack is not empty and the last element in stack = the value of the current key, we remove the last element from stack
        stack.pop()
      else:
        return False
    else: # If c is NOT a closing parenthese, we append it to stack
      stack.append(c)
  if not(stack):
    return True
  else:
    return False

print(isValid("()[]{"))
print(isValid("()[{]}"))