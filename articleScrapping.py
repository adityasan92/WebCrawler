import articletext

url= "http://www.bloomberg.com/news/articles/2015-12-18/goldman-sachs-21-of-the-world-s-most-interesting-charts"

article = articletext.getArticle(url)

print articletext.getKeywords(article)
