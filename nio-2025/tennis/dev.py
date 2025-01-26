content = open("test.txt", "r").read().splitlines()

with open("java-help.txt", "w") as file:
    for line in content:
        file.write('inputQueue.add("' + line + '");' + "\n")