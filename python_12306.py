from splinter.browser import Browser
import time
from time import sleep
import sched
import datetime

def buy_ticket():
	while 1:
		b.find_by_text('查询').click()
		sleep(.01)
		b.find_by_text('预订')[5].click()
		sleep(.01)
		b.find_by_xpath('//*[@id="normalPassenger_0"]')[1].click()
		b.find_by_xpath('//*[@id="dialog_xsertcj_ok"]').click()



url = 'https://kyfw.12306.cn/otn/login/init'
b = Browser(driver_name="chrome")
b.visit(url)
b.fill("loginUserDTO.user_name","hejie009")
input('Ready? ')

run_at = datetime.datetime(2018,1,29,12,59,59).timestamp()
print('Now:',time.time(), time.strftime("%H:%M:%S"),'\nRun:', run_at)

s=sched.scheduler()
s.enterabs(run_at, 1, buy_ticket)
s.run()

# //*[@id="normalPassenger_0"]
# //*[@id="dialog_xsertcj_ok"] # student ticket ok
