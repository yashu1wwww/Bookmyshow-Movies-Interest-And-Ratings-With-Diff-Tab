from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from threading import Thread, Barrier


def func(barrier):
    
    driver = webdriver.Chrome()

    driver.get("https://in.bookmyshow.com/bengaluru/movies/varisu/ET00332034") #for script referal i putted one movie url change to  to your required movie url  with selecting location after paste url here

    print('wait for others')
    barrier.wait()

    print('click')
    b.click()
    
   #below code was convenient to my script run so used it it available in stackoverflow 

number_of_threads = 5 #change how much tab you want i entered 5 change to your required

barrier = Barrier(number_of_threads)

threads = []

for _ in range(number_of_threads):
    t = Thread(target=func, args=(barrier,)) 
    t.start()
    threads.append(t)

for t in threads:
    t.join()
