import sys
import jieba
import matplotlib.pyplot as plt
import locale
from wordcloud import WordCloud,ImageColorGenerator
from scipy.misc import imread

def getridof(arr):
	f = open('filter.txt','r',encoding = 'utf-8')
	text = f.read()
	p = text.replace('\n','')
	p = p.split('  ')
	res = [];
	for item in arr:
		if item not in p:
			res.append(item)
	return res

novel="gcd2.txt"
imgmask="img"
resimg="result.jpg"

#打开文件的编码方式，与系统有关，默认为ascll ，可通过locale.getpreferredencoding()查看，修改为utf-8
novletext=open(novel,encoding="utf-8").read() 
#分词
hmseg=jieba.cut(novletext)	
_hmseg = getridof(hmseg)
seg_space=' '.join(_hmseg)
alice_color=imread(imgmask)
fwc=WordCloud(font_path='msyh.ttf',max_words=700,width=400,height = 10000,background_color='white',mask = alice_color,max_font_size=100,font_step=1).generate(seg_space)
imagecolor=ImageColorGenerator(alice_color)
plt.imshow(fwc.recolor(color_func=imagecolor))
plt.axis("off")
plt.show()
fwc.to_file(resimg)
