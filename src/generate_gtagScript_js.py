def generate_gtagScript_js(gtmtag_id, directory_path):
    js_code = f'''window.dataLayer = window.dataLayer || [];
function gtag(){{window.dataLayer.push(arguments);}}
// google Tag manager
(function(w,d,s,l,i){{
    w[l].push({{'gtm.start':
    new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    }})(window,document,'script','dataLayer', '{gtmtag_id}');
'''

    with open(f"{directory_path}/gtagScript.js", "w") as js_file:
        js_file.write(js_code)
