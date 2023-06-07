from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import re


opt = Options()
# opt.add_argument("--headless")
driver = webdriver.Edge(options=opt)

Username = 'national_code'
Password = 'password'

driver.get('https://edu.uast.ac.ir/CAS/Account/Login?ReturnUrl=%2fEducation')

username = driver.find_element(By.NAME, 'Username')
username.send_keys(Username)

password = driver.find_element(By.NAME, 'Password')
password.send_keys(Password)

sub_but = driver.find_element(By.ID, 'btn-login')
sub_but.submit()

driver.get('https://edu.uast.ac.ir/cas/Users/Profile')

source_final = driver.page_source

FirstName = re.findall('<input class="k-textbox" disabled="disabled" id="FirstName" name="FirstName" type="text" value="(.*)">', source_final)[0]
LastName = re.findall('<input class="k-textbox" disabled="disabled" id="LastName" name="LastName" type="text" value="(.*)">', source_final)[0]

data = ("FirstName: " + FirstName + "\n" + "LastName: " + LastName).encode("utf-8")
driver.quit()

f = open("Data.txt", "wb")
f.write(data)
f.close()
