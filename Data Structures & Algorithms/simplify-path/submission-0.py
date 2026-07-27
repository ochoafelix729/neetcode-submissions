class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for item in path:
            if not item or item == '.':
                continue
            if item == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        if not stack:
            return "/"
        res = ""
        for item in stack:
            res += "/" + item
        return res