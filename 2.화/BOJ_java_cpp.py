name = input().strip()

if '_' in name and any(c.isupper() for c in name):
    print("ERROR!")
elif '_' in name:
    # C++ to Java
    parts = name.split('_')
    result = parts[0] + ''.join(p.capitalize() for p in parts[1:])
    print(result)
elif any(c.isupper() for c in name):
    # Java to C++
    result = ''
    for c in name:
        if c.isupper():
            result += '_' + c.lower()
        else:
            result += c
    print(result)
else:
    print("ERROR!")