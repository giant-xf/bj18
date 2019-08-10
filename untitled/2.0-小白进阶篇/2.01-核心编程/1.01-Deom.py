import hashlib
t =hashlib.md5()
t.update(b'fengge')
print(t.hexdigest())