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
