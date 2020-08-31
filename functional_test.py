from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class NewVisitorTest(unittest.TestCase):  
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.url = 'http://127.0.0.1:8000'
        self.url_cv = 'http://127.0.0.1:8000/cv'
        self.url_cv_new = 'http://127.0.0.1:8000/cv/new_cv'



    def tearDown(self):
        self.browser.quit()
    
    def test_1_cv_page_as_vistor(self):
        self.browser.get(self.url_cv)

        self.assertIn('My blog', self.browser.title)

        sub_headings = self.browser.find_elements_by_tag_name("h2")
        self.assertIn('Basic Information',[sub_heading.get_attribute('textContent') for sub_heading in sub_headings])
        self.assertIn('Education',[sub_heading.get_attribute('textContent') for sub_heading in sub_headings])
        self.assertIn('Work Experience',[sub_heading.get_attribute('textContent') for sub_heading in sub_headings])
        self.assertIn('Skills',[sub_heading.get_attribute('textContent') for sub_heading in sub_headings])
        self.assertIn('Voluneering',[sub_heading.get_attribute('textContent') for sub_heading in sub_headings])

        self.assertTrue(self.browser.find_element_by_link_text('Post list'))
        self.assertTrue(self.browser.find_element_by_link_text('CV page'))

        login = self.browser.find_element_by_class_name('top-menu')
        login.click()
        time.sleep(1)
        self.assertTrue(self.browser.find_element_by_tag_name("input"))

    def test_2_cv_page_as_superuser(self):
        self.browser.get(self.url_cv_new)

        #login
        username = self.browser.find_element_by_name('username')
        username.send_keys('test')
        password = self.browser.find_element_by_name('password')
        password.send_keys('ariescoco123')
        password.send_keys(Keys.ENTER)

        #add to info
        textarea = self.browser.find_element_by_id('id_text')
        textarea.send_keys('test info')
        addinfo = self.browser.find_element_by_name('info')
        addinfo.click()
        # time.sleep(10)

        #add to education
        self.browser.get(self.url_cv_new)
        textarea1 = self.browser.find_element_by_id('id_text')
        textarea1.send_keys('test education')
        addinfo = self.browser.find_element_by_name('education')
        addinfo.click()

        #add to work
        self.browser.get(self.url_cv_new)
        textarea = self.browser.find_element_by_id('id_text')
        
        textarea.send_keys('test work')
        addinfo = self.browser.find_element_by_name('work')
        addinfo.click()

        #add to skills
        self.browser.get(self.url_cv_new)
        textarea = self.browser.find_element_by_id('id_text')
        
        textarea.send_keys('test skills')
        addinfo = self.browser.find_element_by_name('skills')
        addinfo.click()

        #add to voluneering
        self.browser.get(self.url_cv_new)
        textarea = self.browser.find_element_by_id('id_text')
        
        textarea.send_keys('test voluneering')
        addinfo = self.browser.find_element_by_name('voluneering')
        addinfo.click()

        time.sleep(10)

        test_contexts = self.browser.find_elements_by_tag_name('p')
        self.assertIn('test info',[test_context.get_attribute('textContent') for test_context in test_contexts])
        self.assertIn('test education',[test_context.get_attribute('textContent') for test_context in test_contexts])
        self.assertIn('test work',[test_context.get_attribute('textContent') for test_context in test_contexts])
        self.assertIn('test skills',[test_context.get_attribute('textContent') for test_context in test_contexts])
        self.assertIn('test voluneering',[test_context.get_attribute('textContent') for test_context in test_contexts])


if __name__  == '__main__':
    unittest.main(warnings='ignore')
    