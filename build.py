import re
b=open(r'C:/Users/Admin/Downloads/Wylinka/strona/public/znak/badge.html',encoding='utf-8').read()
st=re.findall(r'<style>\s*(\.wylinka-badge.*?)</style>',b,re.S)[0].strip()
ln=re.findall(r'(<a class="wylinka-badge".*?</a>)',b,re.S)[0].replace('przykladowa-firma.pl','szklokolor.pl')
ff=open('_src_fonts/fontface.css',encoding='utf-8').read().strip().replace('font-weight:400 800;','font-weight:400 800;font-stretch:100% 125%;')
s=open('src.html',encoding='utf-8').read().replace('{{FONTFACE}}',ff).replace('{{BADGE_STYLE}}',st).replace('{{BADGE_LINK}}',ln)
open('index.html','w',encoding='utf-8',newline='\n').write(s)
print(len(s))
