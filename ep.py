def yt(t, e):
    r = [0 for i in range(256)]
    o = 0
    i = ""
    for a in range(0,256):
        r[a] = a;
    for a in range(0,256):
        o = (o + r[a] + ord(t[a % len(t)])) % 256
        n = r[a]
        r[a] = r[o]
        r[o] = n

    u = 0
    o = 0
    a = 0
    for u in range(0,len(e)):
        a = (a + 1) % 256
        o = (o + r[a]) % 256
        n = r[a]
        r[a] = r[o]
        r[o] = n
        i += chr(ord(e[u]) ^ r[(r[a] + r[o]) % 256])
    return i

def bt(t):
    def arg1(t,e):
        n = [' ' for i in range(256)]
        for r in range(0,len(t)):
            
            if "a" <= t[r] and "z" >= t[r]:
                o = ord(t[r]) - 97 
            else:
                o = ord(t[r]) - ord("0") + 26
            for i in range(0,36):
                if (e[i] == o):
                    o = i
                    break

            if 25< o:
                n[r] = chr(o - 26 + ord("0")) 
            else:
                n[r] = chr(o + 97)
    
        return "".join(n).strip()

    a1 = arg1("d" + mt + "9", gt)
    def arg2(t):
        if not t:
            return ""

        e = n = r = o = i = a = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1];

        o = len(t)
        i = ""
        r = 0
        while r < o:
            while True:
                e = a[255 & ord(t[r])]
                r += 1
                if not (r < o and -1 == e):
                    break
            if (-1 == e):
                break
            while True:
                n = a[255 & ord(t[r])]
                r += 1
                if not (r < o and -1 == n):
                    break
            if (-1 == n):
                break
            i += chr(e << 2 | (48 & n) >> 4)
            while True:
                e = (255 & ord(t[r]))
                if 61 == e:
                    return i
                r += 1

                e = a[e]
                if not (r < o and -1 == e):
                    break
            if (-1 == e):
                break
            i += chr((15 & n) << 4 | (60 & e) >> 2);
            while True:
                n = (255 & ord(t[r]))
                if (61 == n):
                    return i
                r += 1
                n = a[n]
                if not (r < o and -1 == n):
                    break
            if (-1 == n):
                break
            i += chr((3 & e) << 6 | n)
        
        return i
    
    a2 = arg2(t)
    buy_key,sign,token,timestamp = yt(a1,a2).split('-')
    data = dict(
        buy_key=buy_key,
        sign=sign,
        token=token,
        timestamp=timestamp,
    )
    return data

mt = yt("xm", "Ä[ÜJ=Û3Áf÷N")
gt = [19, 1, 4, 7, 30, 14, 28, 8, 24, 17, 6, 35, 34, 16, 9, 10, 13, 22, 32, 29, 31, 21, 18, 3, 2, 23, 25, 27, 11, 20, 5, 15, 12, 0, 33, 26]

def ep_decode(ep):
    data = bt(ep)
    return data

if __name__ == '__main__':
    print(ep_decode('20NvOoh6T39X3qwKO4cY5g5bVhg+1nfPHIQafFTmCXihnrqF2PjczO8O0auK1KJhDrJ30XMYfKJo2uz+xgwd3rwRPi5f'))