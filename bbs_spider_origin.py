'''
Created on 2016-5-2
获取 BBS 相关板块的信息
@author: ThinkPad User
'''
 
import sys  
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import re
 
class BBSSpider:
    '''
    classdocs
    '''
 
    def __init__(self):
        #self.baseURL = "http://bbs.ustc.edu.cn/cgi/bbsdoc?board=" + str(board)
        self.baseURL = ""
        self.enable = True
        self.charaterset = "gb2312"
 
    # 获取最近不含回帖的帖子    
    def getHtml(self, url):        
        #self.baseURL = "http://bbs.ustc.edu.cn/cgi/bbsbfind?type=1&board=" + str(board) + "&title=&title2=&title3=&userid=&dt=7&og=on&boardordigest=0&labelabc=0"
        self.baseURL = url
 
        try:
            request = urllib.request.Request(self.baseURL)
            response = urllib.request.urlopen(request)
            #print response.read().decode(self.charaterset, 'ignore')
            return response.read().decode("gb2312", 'ignore').encode("utf-8")
        except urllib.error.URLError as e:
            if hasattr(e, "reason"):
                string = "连接bbs 失败, 原因" +  str(e.reason)
                print(string.encode(self.charaterset))
                return None
 
    # 删除 获取的网页内容中的一些噪声              
    def removeNoise(self, content):
        # 去除  
        removeNBSP = re.compile(r" ")
        content = re.sub(removeNBSP, " ", content).strip()
        removeAMP = re.compile(r"&")
        content = re.sub(removeAMP, "&", content).strip()
 
        # remove blank line
        removeN = re.compile(r"\n{1,}")
        content = re.sub(removeN, "\n", content).strip()
        return content
 
    # 获取发帖信息        
    def getItem(self, board):
        string = "http://bbs.ustc.edu.cn/cgi/bbsbfind?type=1&board=" + str(board) + "&title=&title2=&title3=&userid=&dt=7&og=on&boardordigest=0&labelabc=0"
        content = self.getHtml(string)
        if not content:
            print("加载页面失败")
            return
 
        #string = r"author.*?>(.*?).*?datetime.*?>(.*?)<.*?title>(.*?)"
        string = r"author.*?>(.*?).*?datetime.*?>(.*?)<.*?title.*?(.*?)"
        pattern = re.compile(string, re.S)
        res = re.findall(pattern, content.decode())
        stories = []
        count = 0
        for item in res:
            print('Length item: ', len(item), item)
            text = self.removeNoise(item[3])
            stories.append(item[2])
 
            # 获取内容
            string_out = str("id:%3d\t发帖人:%20s\t发帖时间:%20s\t发帖标题:%40s" % (count, item[0], item[1], text))
            print(string_out.encode(self.charaterset))
            count += 1  
        return stories 
 
    # 获取详细信息
    def getDetails(self, board):
        stories = self.getItem(board)
        if not stories:
            return
 
        total_num = len(stories)
 
        while self.enable:
            string_tip = "\n\n================【请输入需要查看的帖子的id, 按 Q 退出】=============="
            id = input(string_tip)
            if id == "Q":
                self.enable = False
                break
 
            try:    
                int_id = int(id)
                if int_id < 0 or int_id >= total_num:
                    continue
            except:
                continue
 
            string = "http://bbs.ustc.edu.cn/cgi/" + stories[int_id]
            content = self.getHtml(string)
            if not content:
                print("获取网页信息失败")
                return
 
            pattern_str = "WWWPOST(.*?)--"
            pattern = re.compile(pattern_str, re.S)
            res = re.findall(pattern, content)
            for item in res:
                text = self.removeNoise(item)
                print(text.encode(self.charaterset))
 
    # 使用常用板块信息
    def getBoard(self):
        flag = True
        self.enable = True
        boards = ['Job', 'Intern', 'SecondHand', 'PieBridge', 'Free', 'PMPI', 'Badminton', 'Swimming']
        count = 0
        for item in boards:
            print("id:%d  board:%15s" % (count, boards[count]))
            count += 1
 
        total_num = count
        while flag:
            self.enable = True
            string_tip = "\n\n===================【请输入需要查看的板块的id, 按 Q 退出】================"
            idx = input(string_tip)
            if idx == "Q":
                flag = False
                break
 
            try: 
                int_id = int(idx)
                if int_id < 0 or int_id >= total_num:
                    continue
            except:
                continue
 
            self.getDetails(boards[int_id])
 
 
 
if "__main__" == __name__:
    bbs = BBSSpider()    
    bbs.getBoard()
    #bbs.getDetails("Job")</a.*?=(.*?)></a.*?></a.*?></a.*?></code>