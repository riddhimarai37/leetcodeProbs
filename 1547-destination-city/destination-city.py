class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = {"a": [], "b": []}

        for path in paths:
            cityA = path[0]
            cityB = path[1]


            cities["a"].append(cityA)
            cities["b"].append(cityB)


            if cityB in cities["a"]:
                cities["b"].remove(cityB)
            if cityA in cities["b"]:
                cities["b"].remove(cityA)
    
        return cities["b"][0]


        