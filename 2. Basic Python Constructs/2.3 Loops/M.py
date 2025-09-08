countOfPlayers = int(input())
minPlayer = "ёёёёёёёёёёёё"

for i in range(countOfPlayers):
    name = input()
    if name < minPlayer:
        minPlayer = name
        
print(minPlayer)