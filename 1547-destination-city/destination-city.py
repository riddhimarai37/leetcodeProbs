class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        startCities, endCities = set(), set()

        for path in paths:
            startCities.add(path[0])
            endCities.add(path[1])

        for city in endCities:
            if city not in startCities:
                return city
        
        