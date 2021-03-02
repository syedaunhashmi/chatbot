from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random
from chatterbot import ChatBot

bot=ChatBot(
    name='GUI Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
    ],
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.db',
    read_only=True
    
)

# Login Credentials
username = 'snuhhhashmi'
password = 'Palkia786'
url = 'https://www.instagram.com/direct/inbox/'
def path():
		global chrome
	
		# starts a new chrome session 
		chrome = webdriver.Chrome() # Add path if required

def url_name(url): 
  chrome.get(url)
   
  # adjust sleep if you want
  time.sleep(4) 
def login(username, your_password):
	#log_but = chrome.find_element_by_class_name("L3NKy") 
	#time.sleep(2)
	#log_but.click()
	#time.sleep(4)
	 
	# finds the username box 
	usern = chrome.find_element_by_name("username")
	 
	# sends the entered username 
	usern.send_keys(username)
 
	# finds the password box 
	passw = chrome.find_element_by_name("password")
 
	# sends the entered password 
	passw.send_keys(your_password)
	 
	# press enter after sending password
	passw.send_keys(Keys.RETURN) 
	time.sleep(5.5)
	 
	# Finding Not Now button 
	not1k = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')  
	not1k.click()
	time.sleep(3)

	notk = chrome.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[2]")  
	notk.click()
	time.sleep(3)
	
def send_message():

	# Find message button
	message = chrome.find_element_by_class_name('_862NM ') 
	message.click()
	time.sleep(2)
	chrome.find_element_by_class_name('HoLwm ').click()
	time.sleep(1)
	l = ['Aiman Pagal', 'Nuh is best', 'Quiter', 'Selenderina', 'MOtii']
	for x in range(400):
		mbox = chrome.find_element_by_tag_name('textarea')
		mbox.send_keys(random.choice(l))
		mbox.send_keys(Keys.RETURN)
		time.sleep(1.2)
def lastmsg(msg):
	lm= msg.split('\n',-1)
	return lm[-1]
def conv():
	try:
		unread = chrome.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[3]/div')
		unread.click()
		time.sleep(5)
		name= chrome.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div/div').text 
		msg = chrome.find_elements_by_class_name('VUU41')[-1]
		time.sleep(3)
		if 'activate bot' in lastmsg(msg.text).lower():
			if name not in bot_users:
				bot_users[name] = True
				response = 'Hello '+name+' Aun Bot at your service no i will talk to you :) '
				mbox = chrome.find_element_by_tag_name('textarea')
				mbox.send_keys(response)
				mbox.send_keys(Keys.RETURN)
				time.sleep(1.2)
				back= chrome.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[6]/a/div/div[1]/div/span/img')
				back.click()
				time.sleep(1.2)
		if name in bot_users and 'deactivate' not in lastmsg(msg.text).lower():
			response = str(bot.get_response(lastmsg(msg.text)))
			mbox = chrome.find_element_by_tag_name('textarea')
			mbox.send_keys(response)
			mbox.send_keys(Keys.RETURN)
			time.sleep(1.2)
			back= chrome.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[6]/a/div/div[1]/div/span/img')
			back.click()
			time.sleep(1.2)
		if name in bot_users and 'deactivate' in lastmsg(msg.text).lower():
			del bot_users[name]
			response = 'Bye '+name+'take care :)'
			mbox = chrome.find_element_by_tag_name('textarea')
			mbox.send_keys(response)
			mbox.send_keys(Keys.RETURN)
			time.sleep(1.2)
			back= chrome.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[6]/a/div/div[1]/div/span/img')
			back.click()
			time.sleep(1.2)
	except Exception as e:
		print(e)
		pass

	




path()
time.sleep(1)
url_name(url)
login(username, password)
bot_users = {}
while True:
	try:
		if chrome.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[3]/div'):
			conv()
	except Exception as e:
		print(e)
		pass
	time.sleep(3)

#send_message()


chrome.close()

#aOOlW   HoLwm 