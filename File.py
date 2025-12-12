# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:00:55 2020

@author: Ali
"""

from time import sleep
from selenium import webdriver
import xlsxwriter

class fbBot:
    

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

        #chromedriver ="C:\\Users\\Ali\\Desktop\\Update\\Bot\\chromedriver"
        chromedriver ="C:\\Users\\Ali\\Desktop\\fbBot\\chromedriver"
        
        self.driver=webdriver.Chrome(chromedriver)
        self.login()
        sleep(2)
        #self.driver.switch_to.alert.dismiss()
        if self.driver.find_element_by_class_name("_3ixn"):
            self.driver.find_element_by_class_name("_3ixn").click()
            self.Group()
            sleep(2)
        else:
            self.Group()
            sleep(2)
        

    def login(self):
       # self.driver.get("https://www.instagram.com/accounts/login/")
         
        
        self.driver.get("https://www.facebook.com/login/")
        
     
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.username)
        sleep(5)  
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(self.password)  
        sleep(5) 
        self.driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
        #Home page click
        sleep(3)
        
        #Groups
    def Group(self):
            
            self.driver.find_element_by_xpath('//*[@id="navItem_1434659290104689"]/a/div').click()
            self.driver.implicitly_wait(10)     
            #self.driver.find_elements_by_xpath('//button[@class="_2yaa"]') # adding the element
        
    
            hasLoadMore = True
            while hasLoadMore:
                sleep(1)
                try:
                    if self.driver.find_element_by_link_text("See more"):
                            self.driver.find_element_by_link_text("See more").click()   
                except:
                    hasLoadMore = False
            
            users_list = [] 
            
            users = self.driver.find_elements_by_class_name('_2yaa')
     
            for user in users:
                users_list.append(user.text)
                 
            i = 0
            texts_list = [] 
           
            texts = self.driver.find_elements_by_class_name('_2yaa')
             
            for txt in texts:
                texts_list.append(txt.text.split(users_list[i]))
                i += 1
                comments_count = len(users_list)
             
             
            for i in range(1, comments_count):
                user = users_list[i] 
             
                text = texts_list[i] 
             
             
                print("User ",user)
                print("Text ",text)
                
            
            # Workbook() takes one, non-optional, argument  
            # which is the filename that we want to create. 
            workbook = xlsxwriter.Workbook('links.xlsx') 
              
            # The workbook object is then used to add new  
            # worksheet via the add_worksheet() method. 
            worksheet = workbook.add_worksheet() 
            row=0
            column=0
            #find_href = self.driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div[2]/div[1]/a')
            find_href = self.driver.find_elements_by_class_name('_2yau')
            for my_href in find_href:
                #print(my_href.get_attribute("href"))
                # write operation perform 
                worksheet.write(row, column, my_href.get_attribute("href")) 
              
                # incrementing the value of row by one 
                # with each iteratons. 
                row += 1
                  
            workbook.close() 
            
            print("Saved successfully")
            self.driver.close()
   
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    ig_bot=fbBot('Fox@gmail.com', '12345')



