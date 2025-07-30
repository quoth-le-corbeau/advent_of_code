import hashlib

i = 0
res = ""
door_id = "abc"
door_id = "reyedfim"
password = {n:"" for n in range(8)}
while any(val=="" for val in password.values()):
    i += 1
    test_string = door_id + str(i)
    hsh = hashlib.md5(string=test_string.encode())
    res = hsh.hexdigest()
    if res[:5] == "00000":
        print(res)
        position = res[5]
        if not position.isnumeric():
            continue
        position_i = int(position)
        if position_i <= 7:
            print(password)
            password[position_i] = res[6]

s=""
for i in range(8):
    s += password[i]
print(f"password: {s}")
