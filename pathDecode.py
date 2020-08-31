
class vt():
    def __init__(self,t):
        self._randomSeed = t
        self.cg_hun()

    def ran(self):
        self._randomSeed = (211 * self._randomSeed + 30031) % 65536
        return self._randomSeed / 65536

    def cg_hun(self):
        self._cgStr = ""
        t = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/\\:._-1234567890"
        e = len(t)
        n = 0
        for i in range(e):
            r = self.ran() * len(t)
            o = int(r)
            self._cgStr += t[o]
            t = "".join(t.split(t[o]))
        
    def cg_fun(self,t):
        t = [int(i) if i else 0 for i in t.split("*")]
        e = ""
        n = 0;
        for n in range(n,len(t)-1):
            e += self._cgStr[t[n]]
        return e

def path_decode(seed,fileId):
    c = vt(seed)
    p = c.cg_fun(fileId)
    return p 

if __name__ == '__main__':
    result = path_decode(9583,"27*31*44*62*1*8*6*48*52*4*6*17*16*6*35*35*6*43*25*27*48*63*58*4*50*47*60*64*15*39*59*49*2*36*48*48*16*58*18*44*2*32*12*7*52*64*51*26*29*4*22*")
    print(result)