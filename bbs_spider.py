import sys  
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import re
from time import sleep
from splinter.browser import Browser

def handle_new_post(url, title):
    # b.execute_script('window.open("");')
    # b.windows.current = b.windows[-1]
    # b.visit(url)
    print('\nFound new post: %s\n\t%s\n\n'% (title, url))

def spider(url):
    global count

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request).read()
    response = response.decode('gb2312', 'ignore') # avoid illegal multibyte sequence
    
    ctn = re.findall(pattern_content, response)[0]
    title = re.findall(pattern_title, ctn)[0].strip()
    nxt_post = re.findall(pattern_nxt, response)


    if all([kw in ctn for kw in kw_and]):
        if any([kw in ctn for kw in kw_or]):
            handle_new_post(url, title)
    count += 1
    print(end='\r')
    sys.stdout.write("\033[K") # Clear to the end of line
    print('\rChecked post %d: %s ... ' % (count, title), end='')

    
    if nxt_post:
        href = nxt_post[0].split('href=')[1].split('>')[0]
        url_nxt = base_url + href
        return spider(url_nxt)
    else:
        return url


kw_and = ['实习']
kw_or = ['机器学习','深度学习','数据挖掘','tensorflow', 'keras', 'deep learning', 'machine learning', 'data mining']
base_url = 'https://bbs.sjtu.edu.cn/'
init_url = base_url + 'bbscon,board,JobInfo,file,M.1516965109.A.html'
count = 0

# b = Browser(driver_name = 'chrome')
pattern_nxt = re.compile('返回讨论区.*?下一篇', re.S)
pattern_title = re.compile('标  题:.*?\\n', re.S)
pattern_content = re.compile('标  题:.*?来源:・饮水思源', re.S)


url = init_url
while url:
    url = spider(url)
    if url:
        sleep(3600)

print('\n\nOoops! Something went wrong...\n')



    


