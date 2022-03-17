import csv
import pandas as pd
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS #词云，颜色生成器，停止词
import imageio

d = pd.read_csv(r"moviewreview.csv",engine='python',encoding='utf-8-sig')
text = d.iloc[:,3].tolist()
 
backgroud = imageio.imread('./mask.png',format=None)
res = []
for i in text:
    words = jieba.cut(i)
    for s in words:
        if s in """都人我在也什么之间一种这个同时几乎一样一场一个真的更加那种还是那场因为出来但是一部这些所以没有就是完全对于这种不是而且其实了一定只有""":
            print("删除"+s)
        else:
            res.append(s.strip())


wc = WordCloud(
            width=1400,
            height=2200,
			background_color='white',
	        mode='RGB', 
			mask=backgroud, #添加蒙版，生成指定形状的词云，并且词云图的颜色可从蒙版里提取
			max_words=300,
			stopwords='的和与',#内置的屏蔽词,并添加自己设置的词语
			font_path='C:\Windows\Fonts\STZHONGS.ttf',
			max_font_size=200, #最大字体大小
			relative_scaling=0.5, #设置字体大小与词频的关联程度
			random_state=50, 
			scale=20,
            repeat=False

        ).generate(','.join(res))

# 保存图片
wc.to_file(r"wordcloud.png") # 按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰
# 4.显示图片
# 指定所绘图名称
plt.figure("词云图")
# 以图片的形式显示词云
plt.imshow(wc)
# 关闭图像坐标系
plt.axis("off")
plt.show()