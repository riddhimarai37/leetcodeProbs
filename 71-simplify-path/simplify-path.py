class Solution:
    def simplifyPath(self, path: str) -> str:
        dirOrFiles = []
        path = path.split('/')
        for element in path:
            if dirOrFiles and element == "..":
                dirOrFiles.pop()
            elif element not in [".", "", ".."]:
                dirOrFiles.append(element)

        return "/" + "/".join(dirOrFiles)

            
        