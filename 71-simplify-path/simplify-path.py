class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for i in path.split("/"):
            if i == "/" or i == "//" or i == "." or i == "":
                continue
            if i == "..":
                if stack: stack.pop()
            else:
                stack.append(i)

        return "/" + "/".join(stack)










        
        # stack  = []

        # for i in path.split('/'):
        #     # if i == "/" or i=="//" we skip 
        #     if i == "..":
        #         if stack:
        #             stack.pop()
        #     elif i == "." or i == "":
        #         # skip . or an empty string
        #         continue
        #     else:
        #         stack.append(i)

        # return "/" + "/".join(stack)                
            
        