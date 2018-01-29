from splinter.browser import Browser
import time
import sched
import datetime

def sec_kill():
	print('Start seckill... ', datetime.datetime.now().strftime("%H%M%S.%f"))
	while 1: # timelapse 0.0048 (average on 3 tests)
		print('\nSeckill... \n%s'% datetime.datetime.now().strftime("%H%M%S.%f"))
		if refresh: 
			b.reload()
		button = b.find_by_xpath(btn)
		print(datetime.datetime.now().strftime("%H%M%S.%f"), button)
		if button:
			button.click()
			time.sleep(2)
			b.find_by_xpath(btn2).click()
			time.sleep(2)
			b.find_by_xpath(btn3).click()
			break 
		else:
			print('Not ready...')
			break
		print(datetime.datetime.now().strftime("%H%M%S.%f"))
	print('Finished')

# parameters
# url = "https://detail.ju.taobao.com/home.htm?spm=a220o.1000855.1998059529.1.69d672b0C0iecD&item_id=523871102107&"
url = 'https://kyfw.12306.cn/otn/login/init'

btn = '//*[@id="choose-btn-append"]'
btn2 = '//*[@id="GotoShoppingCart"]'
btn3 = '//*[@id="cart-floatbar"]/div/div/div/div[2]/div[4]/div[1]/div/div[1]/a'

refresh = False


# main
b = Browser(driver_name="chrome")
b.visit(url) 
input('Finished login?')
print('Ok')
run_at = datetime.datetime(2017,11,10,23,59,59).timestamp()
print('Now:',time.time(), time.strftime("%H:%M:%S"),'\nRun:', run_at)

s=sched.scheduler()
s.enterabs(run_at, 1, sec_kill)
s.run()

# b.cookies.add({"_jc_save_fromStation":"%u4E0A%u6D77%2CSHH"})
# sleep(1)
# b.cookies.add({"_jc_save_fromDate":"2018-01-20"})
# sleep(1)
# b.cookies.add({u'_jc_save_toStation':'%u6C38%u5DDE%2CAOQ'})
# sleep(1)

# b.reload()
# time.sleep(1)
# time.sleep(run_at-time.time())

# sec_kill()