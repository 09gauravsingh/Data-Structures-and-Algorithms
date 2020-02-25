from stack import stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "{" and p2 == "}":
        return True
    if p1 == "[" and p2 == "]":
        return True
    else:
        return False

def paren_index(paren):
   s=stack()
   is_balanced=True
   index=0
   while index < len(paren_index) and is_balanced:
       paren=paren_string[index]
       if paren in "([{":
           s.push(paren)
       else:
           if s.is_empty():
               is_balanced=False
           else:
               top = s.pop()
               if not is_match(top, paren):
                   is_balanced-False

       index += 1
   if s.empty() and is_balanced:
       return True
   else:
       return False
