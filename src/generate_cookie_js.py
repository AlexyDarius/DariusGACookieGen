def generate_cookies_js(privacyPolicyURL, mainMessage, gatagID, cookieExpiration, directory_path):
    js_code = f'''window.addEventListener("DOMContentLoaded", function () {{

    var hardcodedConfig = {{
        "privacyPolicyURL": "https://{privacyPolicyURL}",
        "mainMessage": "{mainMessage}",
        "gatagID": "{gatagID}",
        "cookieExpiration": {cookieExpiration}
    }};

    var o = hardcodedConfig.privacyPolicyURL,
        i = "consentCookie",
        n = document.createElement("div");
    n.setAttribute("id", "cookie-msg"), n.classList.add("fixed-bottom", "rounded", "col-md-7", "col-lg-5", "col-xl-4", "col-xxl-3");
    var t = document.createElement("div");
    (t.innerHTML = hardcodedConfig.mainMessage || "Ce site utilise des cookies que vous pouvez param\xe9trer."), n.appendChild(t);
    var r = document.createElement("div");
    (r.innerHTML = "Voir notre <a href='" + o + "'>politique de confidentialit\xe9</a>"), n.appendChild(r);
    var a = mibreitCookieConsent.getConsentCookie(i);
    a
        ? (console.log("consentCookie already present:", JSON.stringify(a)), gtag("set", a), gtag("event", "ConsentConfiguredEvent"))
        : (mibreitCookieConsent.createCookieConsent(
                n,
                [{{ label: "Google Analytics", cookieName: "GA4_Active", info: hardcodedConfig.mainMessage, active: !0 }}],
                function (o) {{
                    console.log("consentCookie:", JSON.stringify(o)), o.GA4_Active && gtag("config", hardcodedConfig.gatagID, {{ cookie_expires: hardcodedConfig.cookieExpiration }}), gtag("set", o), gtag("event", "ConsentConfiguredEvent"), n.remove();
                }},
                !1,
                i
            ),
            document.querySelector("body").appendChild(n));
}})
'''

    with open(f"{directory_path}/cookie.js", "w") as js_file:
        js_file.write(js_code)
