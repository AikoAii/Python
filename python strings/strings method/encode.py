txt = "My string"
x = txt.encode(encoding="utf-8", errors="strict")
print(x)
# Output: b'My string'