function vt(t) {
                this._randomSeed = t,
                this.cg_hun()
            }
            vt.prototype = {
                cg_hun: function() {
                    this._cgStr = "";
                    var t = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/\\:._-1234567890"
                      , e = t.length
                      , n = 0;
                    for (n = 0; n < e; n++) {
                        var r = this.ran() * t.length
                          , o = parseInt(r);
                        this._cgStr += t.charAt(o),
                        t = t.split(t.charAt(o)).join("")
                    }
                },
                cg_fun: function(t) {
                    t = t.split("*");
                    var e = ""
                      , n = 0;
                    for (n = 0; n < t.length - 1; n++)
                        e += this._cgStr.charAt(t[n]);
                    return e
                },
                ran: function() {
                    this._randomSeed = (211 * this._randomSeed + 30031) % 65536;
                    return this._randomSeed / 65536
                },

            };

c = function(t, e) {
    var n = new vt(t).cg_fun(e);
    return "/" === n[0] ? n : "/".concat(n)
}

console.log(c(9583,"27*31*44*62*1*8*6*48*52*4*6*17*16*6*35*35*6*43*25*27*48*63*58*4*50*47*60*64*15*39*59*49*2*36*48*48*16*58*18*44*2*32*12*7*52*64*51*26*29*4*22*"))