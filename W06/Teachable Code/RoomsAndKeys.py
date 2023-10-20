# N^2 - runtime
# O(N) - space

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        self.dfs(0, visited, rooms)
        return all(visited)
    
    def dfs(self, curRoom, visited, roomsAndKeys):
        visited[curRoom] = True
        currentRoomKeys = roomsAndKeys[curRoom]
        for key in currentRoomKeys:
            if not visited[key]:
                self.dfs(key, visited, roomsAndKeys)