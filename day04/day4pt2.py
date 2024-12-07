with open("day04/input4.txt") as f:
    lines = [x.strip() for x in f.readlines()]

xmas_count = 0

offsets = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

for i in range(len(lines)):
    for j in range(len(lines[0])):

        if lines[i][j] == "A":
            mas_count = 0

            for k in range(2):
                
                try_pos1 = (i + offsets[k][0], j + offsets[k][1])
                try_pos2 = (i + offsets[k+2][0], j + offsets[k+2][1])

                if ( 0 <= try_pos1[0] < len(lines) and 0 <= try_pos1[1] < len(lines[0]) 
                    and 0 <= try_pos2[0] < len(lines) and 0 <= try_pos2[1] < len(lines[0]) ):
                  
                    mas_tuple = (lines[try_pos1[0]][try_pos1[1]], lines[try_pos2[0]][try_pos2[1]])
                    if "S" in mas_tuple and "M" in mas_tuple:
                        mas_count += 1

            if mas_count == 2:
                xmas_count += 1

print(xmas_count)
