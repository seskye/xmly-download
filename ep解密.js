bt = function(t) {
                var e = yt(function(t, e) {
                    for (var n = [], r = 0; r < t.length; r++) {
                        for (var o = "a" <= t[r] && "z" >= t[r] ? t[r].charCodeAt() - 97 : t[r].charCodeAt() - "0".charCodeAt() + 26, i = 0; 36 > i; i++)
                            if (e[i] == o) {
                                o = i;
                                break
                            }
                        n[r] = 25 < o ? String.fromCharCode(o - 26 + "0".charCodeAt()) : String.fromCharCode(o + 97)
                    }
                    return n.join("")
                }("d" + mt + "9", gt), function(t) {
                    if (!t)
                        return "";
                    var e, n, r, o, i, a = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1];
                    for (o = (t = t.toString()).length,
                    r = 0,
                    i = ""; r < o; ) {
                        do {
                            e = a[255 & t.charCodeAt(r++)]
                        } while (r < o && -1 == e);if (-1 == e)
                            break;
                        do {
                            n = a[255 & t.charCodeAt(r++)]
                        } while (r < o && -1 == n);if (-1 == n)
                            break;
                        i += String.fromCharCode(e << 2 | (48 & n) >> 4);
                        do {
                            if (61 == (e = 255 & t.charCodeAt(r++)))
                                return i;
                            e = a[e]
                        } while (r < o && -1 == e);if (-1 == e)
                            break;
                        i += String.fromCharCode((15 & n) << 4 | (60 & e) >> 2);
                        do {
                            if (61 == (n = 255 & t.charCodeAt(r++)))
                                return i;
                            n = a[n]
                        } while (r < o && -1 == n);if (-1 == n)
                            break;
                        i += String.fromCharCode((3 & e) << 6 | n)
                    }
                    return i
                }(t)).split("-")
                  , n = tt(e, 4)
                  , r = n[0];
                return {
                    sign: n[1],
                    buy_key: r,
                    token: n[2],
                    timestamp: n[3]
                }
            }