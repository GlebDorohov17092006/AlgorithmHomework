class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, alf = [], "/."
        for element in path:
            if not(stack):
                stack.append("/")

            elif  not(element in alf):
                stack.append(element)

            elif element == "/":
                if stack[-1]==".":
                    k = 0
                    while stack[-1]==".":
                        k+=1
                        stack.pop()
                        if k==3:
                            stack.extend(['.', '.', '.', '/'])
                            break

                    if k==2 and stack[-1]=='/':
                        if len(stack)>1:
                            stack.pop()
                            while stack[-1]!="/":
                                stack.pop()
                    elif k==2:
                        stack.extend(['.','.','/'])
                    elif k==1 and not(stack[-1] in alf):
                        stack.extend(['.','/'])

                elif not(stack[-1] in alf):
                    stack.append(element)
            else:
                stack.append(element)
                
        if stack[-1]==".":
            k = 0
            while stack[-1]==".":
                k+=1
                stack.pop()
                if k==3:
                    stack.extend(['.', '.', '.', '/'])
                    break
            if k==2 and stack[-1]=='/':
                if len(stack)>1:
                    stack.pop()
                    while stack[-1]!="/":
                        stack.pop()
            elif k==2:
                stack.extend(['.', '.','/'])
            elif k==1 and not(stack[-1] in alf):
                stack.append('.')
        if stack[-1]=="/" and len(stack)>1:
            stack.pop()
        return ''.join(stack)