import hashlib

i = 0
res = ""
door_id = "abc"
door_id = "reyedfim"
password = ""
while len(password) < 8:
    i += 1
    test_string = door_id + str(i)
    hsh = hashlib.md5(string=test_string.encode())
    res = hsh.hexdigest()
    if res[:5] == "00000":
        print(i)
        print(f"{res=}")
        password += res[5]

print(f"{password=}")
