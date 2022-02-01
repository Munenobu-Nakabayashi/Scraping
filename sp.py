from bs4 import BeautifulSoup
import requests

"""URLを取得"""
# gets = requests.get('https://zerofromlight.com/blogs')
gets = requests.get('http://jvn.jp/report')

"""bs4にてパーサーする（HTMLを公文表示させる）"""
soup = BeautifulSoup(gets.text, 'html.parser')

"""要素の格納用に空のリストを準備"""
airs = []

"""find_allでh5タグの要素を順番に全て取得し空リストに格納"""
for tag in soup.find_all('dt'):
    print(tag.text)
    airs.append(tag.text)

"""格納されたら保存用のファイルを開き保存し閉じる。
    'at'にすることで上書きせず追記してくれる"""
for air in airs:
    file = open('newtext.txt', 'at', encoding="utf-8_sig")
    print(air, file=file)
    file.close()