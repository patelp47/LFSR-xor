class NumberOne:

    def Crypt(self, data, initialValue):
        for i in data:
            right = initialValue & 1
            initialValue >>= 1
            if right:
                initialValue ^= 0x95
            yield i ^ initialValue

p1 = NumberOne()
print(bytes(p1.Crypt(b'apple', 0x61)))
