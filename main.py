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
    scale=1,
    prefer_horizontal=0.5,
    colormap="rainbow",
    contour_width=0,
    min_font_size=1,
    max_font_size=250,
    max_words=100000,
    mode="RGBA" 
).generate(text)

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

# plt.figure(figsize=(10, 10)) 
fig = plt.gcf()
fig.patch.set_facecolor("black")
plt.imshow(wc, interpolation="bilinear")
plt.axis("off") 
plt.tight_layout(pad=0)  
plt.show()
