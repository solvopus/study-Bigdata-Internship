# 참고자료

[W3Schools - CSS Selector 관련 문법](https://www.w3schools.com/cssref/css_selectors.asp)

[W3Schools - XML의 Element Tree 구조](https://www.w3schools.com/xml/xml_tree.asp)

[W3Schools - Xpath Syntax](https://www.w3schools.com/xml/xpath_syntax.asp)

<br>

[정규표현식 step by step](https://regexone.com/)

[정규표현식 연습 사이트](https://regexr.com/)

[정규표현식 간략 설명](https://hamait.tistory.com/342)

<br>

[Python XML Etree 관련 레퍼런스](https://docs.python.org/ko/3/library/xml.etree.elementtree.html#elementtree-objects)

[lxml 레퍼런스](https://lxml.de/)

<br>

<br>

수업자료

```python
import time
import requests
import lxml.html
import re

def main():
    # 여러 페이지에서 크롤링을 위해 Session 사용
    session = requests.Session()  
    # scrape_list_page() 함수를 호출해서 제너레이터를 추출
    response = session.get('https://www.jobkorea.co.kr/')
    urls = scrape_list_page(response)
    for url in urls:
        response = session.get(url)  # Session을 사용해 상세 페이지를 추출
        
        
def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    #a.text에 왜 저장이 안 되어있는지 의문, 파서의 문제라고 생각됨
    for a in root.cssselect('.company > .name > a'):
        print(a.text_content())
        
        #lxml.html.element Traversal 코드
        for j in a.getiterator():
            print(j.tag, j.text)
            
            
if __name__ == '__main__':
    main()
```



