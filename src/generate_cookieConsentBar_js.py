def generate_cookieConsentBar_js(main_domain, directory_path):
    js_code = f'''var mibreitCookieConsent;
(() => {{
    "use strict";
    var n = {{
            130(n, t, e) {{
                e.d(t, {{ Z: () => r }});
                var o = e(645),
                    i = e.n(o)()(function (n) {{
                        return n[1];
                    }});
                i.push([
                    n.id,
                    ".button_v7h {{\\n  position: relative;\\n  height: 2rem;\\n  max-width: 75%;\\n  margin-top: 0.25rem;\\n  padding-left: 0.5rem;\\n  padding-right: 0.5rem;\\n  border-style: none;\\n  border-radius: var(--bs-border-radius) !important;\\n}}",
                    "",
                ]),
                    (i.locals = {{ button: "button_v7h" }});
                let r = i;
            }},
            180(n, t, e) {{
                e.d(t, {{ Z: () => r }});
                var o = e(645),
                    i = e.n(o)()(function (n) {{
                        return n[1];
                    }});
                i.push([
                    n.id,
                    ".setter_RN- {{\\n  position: relative;\\n  display: flex;\\n  justify-content: space-between;\\n  align-items: center;\\n}}\\n\\n.svgContainer_Sil {{\\n  display: contents;\\n}}\\n\\n.setter_RN- > span {{\\n  flex-grow: 1;\\n}}\\n\\n.setter_RN- svg {{\\n  width: 1.5rem;\\n  height: 1.5rem;\\n  margin-left: 0.5rem;\\n}}",
                    "",
                ]),
                    (i.locals = {{ setter: "setter_RN-", svgContainer: "svgContainer_Sil" }});
                let r = i;
            }},
            933(n, t, e) {{
                e.d(t, {{ Z: () => r }});
                var o = e(645),
                    i = e.n(o)()(function (n) {{
                        return n[1];
                    }});
                i.push([
                    n.id,
                    ".toggleButton_k5a {{\\n  position: relative;\\n  display: inline-block;\\n  cursor: pointer;\\n  width: 3rem;\\n  height: 1.5rem;\\n  border-radius: 0.75rem;\\n  overflow: hidden;\\n}}\\n\\n.toggleButton_k5a span {{\\n  position: absolute;\\n  background-color: #ccc;\\n  top: 0;\\n  left: 0;\\n  right: 0;\\n  bottom: 0;\\n}}\\n\\n.toggleButton_k5a span::before {{\\n  background-color: white;\\n  transform: translateX(-100%);\\n  border-color: #ccc;\\n  border-style: solid;\\n  border-radius: 50%;\\n  box-sizing: border-box;\\n  content: '';\\n  position: absolute;\\n  width: 50%;\\n  height: 100%;\\n}}\\n\\ninput:checked + span {{\\n  background-color: rgb(10, 117, 189);\\n}}\\n\\ninput:checked + span::before {{\\n  transform: translateX(0);\\n  border-color: rgb(10, 117, 189);\\n}}\\n\\n.toggleButton_k5a input {{\\n  display: none;\\n}}",
                    "",
                ]),
                    (i.locals = {{ toggleButton: "toggleButton_k5a" }});
                let r = i;
            }},
            370(n, t, e) {{
                e.d(t, {{ Z: () => r }});
                var o = e(645),
                    i = e.n(o)()(function (n) {{
                        return n[1];
                    }});
                i.push([
                    n.id,
                    ".main_1Tj {{\\n  position: relative;\\n  width: 100%;\\n  margin-top: 12px;\\n  }}\\n.main_1Tj > *:not(:last-child) {{\\n  margin-bottom: 0.5rem;\\n}}\\n.main_1Tj > .mibreit_CookieConsent_Button {{\\n  width: 100%;\\n}}",
                    "",
                ]),
                    (i.locals = {{ main: "main_1Tj" }});
                let r = i;
            }},
            789(n, t, e) {{
                e.d(t, {{ Z: () => r }});
                var o = e(645),
                    i = e.n(o)()(function (n) {{
                        return n[1];
                    }});
                i.push([
                    n.id,
                    ".main_8My {{\\n  position: relative;\\n  display: flex;\\n  flex-direction: column;\\n  width: 100%;\\n}}\\n\\n.main_8My > *:not(:last-child) {{\\n  margin-bottom: 0.5rem;\\n}}\\n\\n.info_3ZZ {{\\n  display: none;\\n  padding-bottom: 0.5rem;\\n}}\\n\\n.info_3ZZ.visible_sXj {{\\n  display: unset;\\n}}",
                    "",
                ]),
                    (i.locals = {{ main: "main_8My", info: "info_3ZZ", visible: "visible_sXj" }});
                let r = i;
            }},
            645(n) {{
                n.exports = function (n) {{
                    var t = [];
                    return (
                        (t.toString = function () {{
                            return this.map(function (t) {{
                                var e = n(t);
                                return t[2] ? "@media ".concat(t[2], " {{").concat(e, "}}") : e;
                            }}).join("");
                        }}),
                        (t.i = function (n, e, o) {{
                            "string" == typeof n && (n = [[null, n, ""]]);
                            var i = {{}};
                            if (o)
                                for (var r = 0; r < this.length; r++) {{
                                    var a = this[r][0];
                                    null != a && (i[a] = !0);
                                }}
                            for (var s = 0; s < n.length; s++) {{
                                var c = [].concat(n[s]);
                                (o && i[c[0]]) || (e && (c[2] ? (c[2] = "".concat(e, " and ").concat(c[2])) : (c[2] = e)), t.push(c));
                            }}
                        }}),
                        t
                    );
                }};
            }},
            379(n, t, e) {{
                var o,
                    i,
                    r =
                        ((o = {{}}),
                        function (n) {{
                            if (void 0 === o[n]) {{
                                var t = document.querySelector(n);
                                if (window.HTMLIFrameElement && t instanceof window.HTMLIFrameElement)
                                    try {{
                                        t = t.contentDocument.head;
                                    }} catch (e) {{
                                        t = null;
                                    }}
                                o[n] = t;
                            }}
                            return o[n];
                        }}),
                    a = [];
                function s(n) {{
                    for (var t = -1, e = 0; e < a.length; e++)
                        if (a[e].identifier === n) {{
                            t = e;
                            break;
                        }}
                    return t;
                }}
                function c(n, t) {{
                    for (var e = {{}}, o = [], i = 0; i < n.length; i++) {{
                        var r = n[i],
                            c = t.base ? r[0] + t.base : r[0],
                            l = e[c] || 0,
                            u = "".concat(c, " ").concat(l);
                        e[c] = l + 1;
                        var p = s(u),
                            f = {{ css: r[1], media: r[2], sourceMap: r[3] }};
                        -1 !== p ? (a[p].references++, a[p].updater(f)) : a.push({{ identifier: u, updater: $(f, t), references: 1 }}), o.push(u);
                    }}
                    return o;
                }}
                function l(n) {{
                    var t = document.createElement("style"),
                        o = n.attributes || {{}};
                    if (void 0 === o.nonce) {{
                        var i = e.nc;
                        i && (o.nonce = i);
                    }}
                    if (
                        (Object.keys(o).forEach(function (n) {{
                            t.setAttribute(n, o[n]);
                        }}),
                        "function" == typeof n.insert)
                    )
                        n.insert(t);
                    else {{
                        var a = r(n.insert || "head");
                        if (!a) throw Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");
                        a.appendChild(t);
                    }}
                    return t;
                }}
                var u,
                    p =
                        ((u = []),
                        function (n, t) {{
                            return (u[n] = t), u.filter(Boolean).join("\\n");
                        }});
                function f(n, t, e, o) {{
                    var i = e ? "" : o.media ? "@media ".concat(o.media, " {{").concat(o.css, "}}") : o.css;
                    if (n.styleSheet) n.styleSheet.cssText = p(t, i);
                    else {{
                        var r = document.createTextNode(i),
                            a = n.childNodes;
                        a[t] && n.removeChild(a[t]), a.length ? n.insertBefore(r, a[t]) : n.appendChild(r);
                    }}
                }}
                function d(n, t, e) {{
                    var o = e.css,
                        i = e.media,
                        r = e.sourceMap;
                    if (
                        (i ? n.setAttribute("media", i) : n.removeAttribute("media"),
                        r && "undefined" != typeof btoa && (o += "\\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(r)))), " */")),
                        n.styleSheet)
                    )
                        n.styleSheet.cssText = o;
                    else {{
                        for (; n.firstChild; ) n.removeChild(n.firstChild);
                        n.appendChild(document.createTextNode(o));
                    }}
                }}
                var v = null,
                    h = 0;
                function $(n, t) {{
                    var e, o, i;
                    if (t.singleton) {{
                        var r = h++;
                        (e = v || (v = l(t))), (o = f.bind(null, e, r, !1)), (i = f.bind(null, e, r, !0));
                    }} else
                        (e = l(t)),
                            (o = d.bind(null, e, t)),
                            (i = function () {{
                                !(function (n) {{
                                    if (null === n.parentNode) return !1;
                                    n.parentNode.removeChild(n);
                                }})(e);
                            }});
                    return (
                        o(n),
                        function (t) {{
                            t ? (t.css !== n.css || t.media !== n.media || t.sourceMap !== n.sourceMap) && o((n = t)) : i();
                        }}
                    );
                }}
                n.exports = function (n, t) {{
                    (t = t || {{}}).singleton || "boolean" == typeof t.singleton || (t.singleton = (void 0 === i && (i = Boolean(window && document && document.all && !window.atob)), i));
                    var e = c((n = n || []), t);
                    return function (n) {{
                        if (((n = n || []), "[object Array]" === Object.prototype.toString.call(n))) {{
                            for (var o = 0; o < e.length; o++) {{
                                var i = s(e[o]);
                                a[i].references--;
                            }}
                            for (var r = c(n, t), l = 0; l < e.length; l++) {{
                                var u = s(e[l]);
                                0 === a[u].references && (a[u].updater(), a.splice(u, 1));
                            }}
                            e = r;
                        }}
                    }};
                }};
            }},
        }},
        t = {{}};
    function e(o) {{
        var i = t[o];
        if (void 0 !== i) return i.exports;
        var r = (t[o] = {{ id: o, exports: {{}} }});
        return n[o](r, r.exports, e), r.exports;
    }}
    (e.n = (n) => {{
        var t = n && n.t ? () => n.default : () => n;
        return e.d(t, {{ a: t }}), t;
    }}),
        (e.d = (n, t) => {{
            for (var o in t) e.o(t, o) && !e.o(n, o) && Object.defineProperty(n, o, {{ enumerable: !0, get: t[o] }});
        }}),
        (e.o = (n, t) => Object.prototype.hasOwnProperty.call(n, t)),
        (e.r = (n) => {{
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(n, Symbol.toStringTag, {{ value: "Module" }}), Object.defineProperty(n, "t", {{ value: !0 }});
        }}),
        (e.nc = void 0);
    var o = {{}};
    (() => {{
        function n(n) {{
            return document.createElement(n);
        }}
        function t(n) {{
            var t = document.createElement("input");
            return (t.type = n), t;
        }}
        function i(n, t) {{
            t.appendChild(n);
        }}
        function r(n, t) {{
            n.innerHTML = t;
        }}
        function a(n, t) {{
            n.classList.contains(t) || n.classList.add(t);
        }}
        function s(n, t) {{
            n.classList.contains(t) && n.classList.remove(t);
        }}
        function c(n, t, e) {{
            n.style.setProperty(t, e);
        }}
        function l(n, t) {{
            n.style.removeProperty(t), 0 === n.style.length && n.removeAttribute("style");
        }}
        function u(n, t) {{
            n.addEventListener("click", t);
        }}
        e.r(o), e.d(o, {{ createCookieConsent: () => R, getConsentCookie: () => H }});
        var p = e(379),
            f = e.n(p),
            d = e(370),
            v = {{ injectType: "singletonStyleTag", insert: "head", singleton: !0 }};
        f()(d.Z, v);
        let h = d.Z.locals || {{}};
        var $ = e(130),
            m = {{ injectType: "singletonStyleTag", insert: "head", singleton: !0 }};
        f()($.Z, m);
        let g = $.Z.locals || {{}},
            y = (function () {{
                function t(t, e) {{
                    (this.component = n(e)), i(this.component, t);
                }}
                return (
                    (t.prototype.show = function () {{
                        l(this.component, "display");
                    }}),
                    (t.prototype.hide = function () {{
                        c(this.component, "display", "none");
                    }}),
                    t
                );
            }})();
        var _,
            b =
                ((_ = function (n, t) {{
                    return (_ =
                        Object.setPrototypeOf ||
                        ({{ __proto__: [] }} instanceof Array &&
                            function (n, t) {{
                                n.__proto__ = t;
                            }}) ||
                        function (n, t) {{
                            for (var e in t) Object.prototype.hasOwnProperty.call(t, e) && (n[e] = t[e]);
                        }})(n, t);
                }}),
                function (n, t) {{
                    if ("function" != typeof t && null !== t) throw TypeError("Class extends value " + String(t) + " is not a constructor or null");
                    function e() {{
                        this.constructor = n;
                    }}
                    _(n, t), (n.prototype = null === t ? Object.create(t) : ((e.prototype = t.prototype), new e()));
                }});
        let C = (function (n) {{
            function t(t, e, o) {{
                var r = n.call(this, t, "button") || this;
                return (r.component.innerHTML = e), a(r.component, g.button), a(r.component, "mibreit_CookieConsent_Button"), i(r.component, t), u(r.component, o), r;
            }}
            return b(t, n), t;
        }})(y);
        var k = e(789),
            w = {{ injectType: "singletonStyleTag", insert: "head", singleton: !0 }};
        f()(k.Z, w);
        let L = k.Z.locals || {{}};
        var x = e(180),
            T = {{ injectType: "singletonStyleTag", insert: "head", singleton: !0 }};
        f()(x.Z, T);
        let S = x.Z.locals || {{}};
        var Z = e(933),
            M = {{ injectType: "singletonStyleTag", insert: "head", singleton: !0 }};
        f()(Z.Z, M);
        let j = Z.Z.locals || {{}};
        var A = (function () {{
            var n = function (t, e) {{
                return (n =
                    Object.setPrototypeOf ||
                    ({{ __proto__: [] }} instanceof Array &&
                        function (n, t) {{
                            n.__proto__ = t;
                        }}) ||
                    function (n, t) {{
                        for (var e in t) Object.prototype.hasOwnProperty.call(t, e) && (n[e] = t[e]);
                    }})(t, e);
            }};
            return function (t, e) {{
                if ("function" != typeof e && null !== e) throw TypeError("Class extends value " + String(e) + " is not a constructor or null");
                function o() {{
                    this.constructor = t;
                }}
                n(t, e), (t.prototype = null === e ? Object.create(e) : ((o.prototype = e.prototype), new o()));
            }};
        }})();
        let P = (function (e) {{
            function o(o, r) {{
                void 0 === r && (r = !0);
                var s = e.call(this, o, "label") || this;
                return a(s.component, j.toggleButton), a(s.component, "mibreit_CookieConsent_ToggleButton"), (s.u = t("checkbox")), (s.u.checked = r), i(s.u, s.component), i(n("span"), s.component), s;
            }}
            return (
                A(o, e),
                (o.prototype.isActive = function () {{
                    return this.u.checked;
                }}),
                o
            );
        }})(y);
        var N = (function () {{
            var n = function (t, e) {{
                return (n =
                    Object.setPrototypeOf ||
                    ({{ __proto__: [] }} instanceof Array &&
                        function (n, t) {{
                            n.__proto__ = t;
                        }}) ||
                    function (n, t) {{
                        for (var e in t) Object.prototype.hasOwnProperty.call(t, e) && (n[e] = t[e]);
                    }})(t, e);
            }};
            return function (t, e) {{
                if ("function" != typeof e && null !== e) throw TypeError("Class extends value " + String(e) + " is not a constructor or null");
                function o() {{
                    this.constructor = t;
                }}
                n(t, e), (t.prototype = null === e ? Object.create(e) : ((o.prototype = e.prototype), new o()));
            }};
        }})();
        let B = (function (t) {{
            function e(e, o, s, c) {{
                void 0 === s && (s = !0), void 0 === c && (c = void 0);
                var l = t.call(this, e, "div") || this;
                a(l.component, S.setter);
                var p = n("span");
                if ((a(p, "mibreit_CookieConsent_Label"), (p.innerHTML = o), i(p, l.component), (l.l = new P(l.component, s)), c)) {{
                    var f = n("div");
                    a(f, S.svgContainer),
                        r(
                            f,
                            '<svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 50 50" width="100px" height="100px"><path d="M 25 2 C 12.309295 2 2 12.309295 2 25 C 2 37.690705 12.309295 48 25 48 C 37.690705 48 48 37.690705 48 25 C 48 12.309295 37.690705 2 25 2 z M 25 4 C 36.609824 4 46 13.390176 46 25 C 46 36.609824 36.609824 46 25 46 C 13.390176 46 4 36.609824 4 25 C 4 13.390176 13.390176 4 25 4 z M 25 11 A 3 3 0 0 0 22 14 A 3 3 0 0 0 25 17 A 3 3 0 0 0 28 14 A 3 3 0 0 0 25 11 z M 21 21 L 21 23 L 22 23 L 23 23 L 23 36 L 22 36 L 21 36 L 21 38 L 22 38 L 23 38 L 27 38 L 28 38 L 29 38 L 29 36 L 28 36 L 27 36 L 27 21 L 26 21 L 22 21 L 21 21 z"/></svg>'
                        ),
                        i(f, l.component),
                        u(f, function (n) {{
                            c();
                        }});
                }}
                return l;
            }}
            return (
                N(e, t),
                (e.prototype.isActive = function () {{
                    return this.l.isActive();
                }}),
                e
            );
        }})(y);
        var O = (function () {{
            var n = function (t, e) {{
                return (n =
                    Object.setPrototypeOf ||
                    ({{ __proto__: [] }} instanceof Array &&
                        function (n, t) {{
                            n.__proto__ = t;
                        }}) ||
                    function (n, t) {{
                        for (var e in t) Object.prototype.hasOwnProperty.call(t, e) && (n[e] = t[e]);
                    }})(t, e);
            }};
            return function (t, e) {{
                if ("function" != typeof e && null !== e) throw TypeError("Class extends value " + String(e) + " is not a constructor or null");
                function o() {{
                    this.constructor = t;
                }}
                n(t, e), (t.prototype = null === e ? Object.create(e) : ((o.prototype = e.prototype), new o()));
            }};
        }})();
        let E = (function (t) {{
                function e(e, o) {{
                    var r = t.call(this, e, "div") || this;
                    return (
                        (r.v = new Map()),
                        a(r.component, "mibreit_CookieConsent_Selector"),
                        a(r.component, L.main),
                        o.forEach(function (t) {{
                            if (t.info) {{
                                var e = n("span");
                                a(e, L.info), a(e, "mibreit_CookieConsent_Info"), (e.innerHTML = t.info);
                                var o = !1;
                                r.v.set(
                                    t.cookieName,
                                    new B(r.component, t.label, t.active, function () {{
                                        o ? (s(e, L.visible), (o = !1)) : (a(e, L.visible), (o = !0));
                                    }})
                                ),
                                    i(e, r.component);
                            }} else r.v.set(t.cookieName, new B(r.component, t.label, t.active));
                        }}),
                        r
                    );
                }}
                return (
                    O(e, t),
                    (e.prototype.getCookieSelection = function (n) {{
                        void 0 === n && (n = !1);
                        var t = {{}};
                        return (
                            this.v.forEach(function (e, o) {{
                                t[o] = !!n || e.isActive();
                            }}),
                            t
                        );
                    }}),
                    e
                );
            }})(y),
            z = (function () {{
                function t(t, e, o, r, s) {{
                    void 0 === r && (r = !1), void 0 === s && (s = void 0);
                    var c = this;
                    (this.h = "consentCookie"),
                        (this.p = function () {{
                            c.g(!0);
                        }}),
                        (this.m = function () {{
                            c._.show(), c.C.show(), c.j.hide(), c.k.hide();
                        }}),
                        (this.g = function (n) {{
                            void 0 === n && (n = !1);
                            var t = c._.getCookieSelection(n),
                                e = new Date();
                            e.setDate(e.getDate() + 30);
                            var o = JSON.stringify(t) + "; samesite=Lax; path=/ ; domain=.{main_domain}; expires=" + e.toUTCString();
                            (document.cookie = c.h + "=" + o), c.L(t);
                        }}),
                        s && (this.h = s),
                        (this.L = o);
                    var l = "Accepter les Cookies",
                        u = "Configurer les Cookies",
                        p = "Confirmer la s\xe9lection";
                    r && ((l = "Cookies akzeptieren"), (u = "Cookies konfigurieren"), (p = "Auswahl erlauben"));
                    var f = n("div");
                    a(f, h.main),
                        a(f, "mibreit_CookieConsent"),
                        i(f, t),
                        (this.j = new C(f, l, this.p)),
                        (this.k = new C(f, u, this.m)),
                        (this._ = new E(f, this.O(e))),
                        this._.hide(),
                        (this.C = new C(f, p, function () {{
                            c.g(!1);
                        }})),
                        this.C.hide();
                }}
                return (
                    (t.prototype.S = function () {{
                        return H(this.h);
                    }}),
                    (t.prototype.O = function (n) {{
                        var t = this.S();
                        if (t) {{
                            var e = Object.keys(t);
                            e &&
                                n.forEach(function (n) {{
                                    e.includes(n.cookieName) && (n.active = t[n.cookieName]);
                                }});
                        }}
                        return n;
                    }}),
                    t
                );
            }})();
        function H(n) {{
            for (var t = 0, e = document.cookie.split(";"); t < e.length; t++) {{
                var o = e[t],
                    i = o.indexOf("="),
                    r = o.substring(0, i).replace(/^\s+|\s+$/g, ""),
                    a = o.substring(i + 1).replace(/^\s+|\s+$/g, "");
                if (r === n)
                    try {{
                        return JSON.parse(a);
                    }} catch (s) {{
                        return;
                    }}
            }}
        }}
        function R(n, t, e, o, i) {{
            return void 0 === o && (o = !1), void 0 === i && (i = void 0), new z(n, t, e, o, i);
        }}
    }})(),
        (mibreitCookieConsent = o);
}})();

'''

    with open(f"{directory_path}/cookieConsentBar.js", "w") as js_file:
        js_file.write(js_code)
