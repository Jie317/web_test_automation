from splinter.browser import Browser
from time import sleep

def auto_submit():
	print('Please input the verification code and continue')

url = 'https://kyfw.12306.cn/otn/login/init'
b = Browser(driver_name='chrome')
b.visit(url)
b.fill("loginUserDTO.user_name","hejie009")

while 1:
	b.find_by_text('查询').click()
	
	yz1154 = b.find_by_id('YZ_77000K11540A')[0].value
	if yz1154 != '无':
		b.find_by_text('预订')[4].click()
		auto_submit()
		
	yz1158 = b.find_by_id('YZ_76000K11580C')[0].value
	if yz1158 != '无':
		b.find_by_text('预订')[6].click()
		auto_submit()

	yz4456 = b.find_by_id('YZ_7m000K445601')[0].value
	if yz4456 != '无':
                b.find_by_text('预订')[5].click()
                auto_submit()


