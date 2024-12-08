from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

text = open('name.txt', 'r').read()

python_mask = np.array(PIL.Image.open("Rakibul.png"))


wc = WordCloud(
    stopwords=STOPWORDS,
    mask=python_mask,
    background_color="black",  
    contour_width=0,
    min_font_size=1,
    max_words=100000
).generate(text)


plt.figure(figsize=(10, 10)) 
plt.imshow(wc, interpolation="bilinear")
plt.axis("off") 
plt.tight_layout(pad=0)  
plt.show()
