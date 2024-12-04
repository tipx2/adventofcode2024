with open("day4/input4.txt") as f:
    lines = [x.strip() for x in f.readlines()]

xmas_count = 0

offsets = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

for i in range(len(lines)):
    for j in range(len(lines[0])):

        if lines[i][j] == "A":
            mas_count = 0

            for k in range(2):
                x1, y1 = offsets[k]
                x2, y2 = offsets[k + 2]
                
                s_pos = (i + x1, j + y1)
                m_pos = (i + x2, j + y2)

                if 0 <= s_pos[0] < len(lines) and 0 <= s_pos[1] < len(lines[0]) and 0 <= m_pos[0] < len(lines) and 0 <= m_pos[1] < len(lines[0]):
                    mas_tuple = (lines[s_pos[0]][s_pos[1]], lines[m_pos[0]][m_pos[1]])
                    if "S" in mas_tuple and "M" in mas_tuple:
                        mas_count += 1

            if mas_count == 2:
                xmas_count += 1

print(xmas_count)
