h = 0

t = [0, 0, 0]

with open('Day1.txt') as f:
    line = f.readline()
    h = int(line)
    while line:
        line = f.readline()
        if line != "\n" and line != "":
            h = h + int(line)
        else:
            if h > min(t):
                t[t.index(min(t))] = h
            h = 0
            print(t[0] + t[1] + t[2])
            print(t)
