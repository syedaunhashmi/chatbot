from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com')
from chatterbot import ChatBot
from selenium.webdriver.common.keys import Keys

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
	


bot_users = {} # A dictionary that stores all the users that sent activate bot 
while True:
	unread = browser.find_elements_by_class_name("VOr2j") # The green dot tells us that the message is new
	name,message  = '',''
	if len(unread) > 0:
		ele = unread[-1]
		action = webdriver.common.action_chains.ActionChains(browser)
		action.move_to_element_with_offset(ele, 0, -20)
		 # move a bit to the left from the green dot
		
		# Clicking couple of times because sometimes whatsapp web responds after two clicks
		try:
			action.click()
			action.perform()
			action.click()
			action.perform()	 		
		except Exception as e:
			pass
		try:
			name = browser.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span').text  # Contact name
			message = browser.find_elements_by_class_name("_1VzZY")[-1]  # the message content
			if 'activate bot' in message.text.lower():
				if name not in bot_users:
					bot_users[name] = True
					text_box = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
					response = "Hi "+name+". Aun's Bot here :). Now I am activated for you\n"
					text_box.send_keys(response)
					user = browser.find_element_by_xpath('//span[@title = "bot_new"]')
					user.click()
					print(bot_users)
			if name in bot_users and'deactivate' not in message.text.lower():
						text_box = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
						response = str(bot.get_response(message.text.lower()))
						text_box.send_keys(response)
						text_box.send_keys(Keys.RETURN)
						user = browser.find_element_by_xpath('//span[@title = "bot_new"]')
						user.click()
			if 'deactivate' in message.text.lower():
				if name in bot_users:
					text_box = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
					response = "Bye Take care :) "+name+".\n"
					text_box.send_keys(response)
					text_box.send_keys(Keys.RETURN)
					del bot_users[name]
					user = browser.find_element_by_xpath('//span[@title = "bot_new"]')
					user.click()
			
		except Exception as e:
			print(e)
			pass
	sleep(2) # A 2 second pause so that the program doesn't run too fast
	