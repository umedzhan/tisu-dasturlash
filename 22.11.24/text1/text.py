
file_path = 'text.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

lines = lines[:-1]

with open(file_path, 'w') as file:
    file.writelines(lines)

print("Ok...")
