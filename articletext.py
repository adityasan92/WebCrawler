from bs4 import BeautifulSoup
import getHtml
def getArticleText(webtext):
    articletext =""
    soup = BeautifulSoup(webtext,"html.parser")
    for tag in soup.findAll('p'):
        try:
            articletext += str(tag.contents[0])
        except:
            a =0
    return articletext

def getArticle(url):
     htmltext = getHtml.getHtmlText(url)
     return getArticleText(htmltext)

def getKeywords(articletext):
    commonWords = open("mostUsedEnglishWords.txt").read().split("\n")
    word_dict = {}
    word_list = articletext.lower().split()
    for word in word_list:
        if word in commonWords:
            continue;
        if word.isalnum():
            if word not in word_dict:
                word_dict[word] =1
            if word in word_dict:
                word_dict[word] +=1
    top_words =  sorted(word_dict.items(),key=lambda(k,v):(v,k),reverse=True)[0:25]
    top25 = []
    for w in top_words:
        top25.append(w[0])
    return top25
