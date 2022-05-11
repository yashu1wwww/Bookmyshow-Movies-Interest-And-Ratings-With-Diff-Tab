from selenium import webdriver

driver = webdriver.Chrome()
driver1 = webdriver.Chrome()
driver2= webdriver.Chrome()
driver3 = webdriver.Chrome()

driver.get("https://in.bookmyshow.com/login/?referer=/bengaluru/movies/vikrant-rona/ET00128225")
driver1.get("https://in.bookmyshow.com/login/?referer=/bengaluru/movies/vikrant-rona/ET00128225")
driver2.get("https://in.bookmyshow.com/login/?referer=/bengaluru/movies/vikrant-rona/ET00128225")
driver3.get("https://in.bookmyshow.com/login/?referer=/bengaluru/movies/vikrant-rona/ET00128225")

#add more driver you want 