from requests import get

address = input()
response = get(address)

count = 0

content = int(response.content.decode('utf-8'))
while content != 0:
    count += content
    content = int(response.content.decode('utf-8'))
    
print(count)