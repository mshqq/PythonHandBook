start = "##"
end = "@@@"
lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

for i in range(len(lines)):
    if not (lines[i].endswith(end)):
        if lines[i].startswith(start):
            print(lines[i][2::])
        else:
            print(lines[i])