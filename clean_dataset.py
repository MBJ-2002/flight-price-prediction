fixed_lines = []
with open("dataset/economy.csv", "r", encoding="utf-8") as f:
    buffer = ""
    for line in f:
        buffer += line.strip("\n")        
        if buffer.count('"') % 2 == 0:
            fixed_lines.append(buffer)
            buffer = ""

with open("dataset/economy_fixed.csv", "w", encoding="utf-8") as f:
    for line in fixed_lines:
        f.write(line + "\n")