from selenium import webdriver

driver = webdriver.Chrome('tests/chromedriver')
driver.set_window_size(1920,1080)
driver.get('https://fabrykatestow.pl')

window_before = driver.window_handles[0]
driver.find_element_by_link_text('ZAPISZ MNIE NA NEWSLETTER!').click()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
url = 'https://fabrykatestow.pl/ciekawostki/'
current_url = driver.current_url


if current_url == url:
    print('OK')
else:
    print(current_url)
    print('NOT OK')


driver.quit()
