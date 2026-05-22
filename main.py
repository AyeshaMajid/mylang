import sys

def run(code):
    lines = code.strip().split("\n")
    variables = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("say "):
            value = line[4:].strip()
            if value.startswith('"') and value.endswith('"'):
                print(value[1:-1])
            elif value in variables:
                print(variables[value])
        elif line.startswith("set "):
            parts = line[4:].split("=", 1)
            var = parts[0].strip()
            val = parts[1].strip().strip('"')
            variables[var] = val
        elif line.startswith("ask "):
            parts = line[4:].split(" ", 1)
            var = parts[0].strip()
            prompt = parts[1].strip().strip('"')
            variables[var] = input(prompt)

with open(sys.argv[1], "r") as f:
    code = f.read()

run(code)