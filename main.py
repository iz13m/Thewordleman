# Importing functions from other files..
from fn import *
from tweet import *

# Creating chrome web driver..
browser = webdriver.Chrome('/Users/iz13m/Code/wordle bot/chromedriver')
browser.set_window_position(900, 0)
browser.set_window_size(500, 800)

# Setting the url for the game ..
url = "https://www.powerlanguage.co.uk/wordle/"

# Opening URL ..
browser.get(url)
time.sleep(2)

# Clicking anywhere to get rid of the popup
browser.find_element_by_xpath("//body").click()
time.sleep(3)

# Setting up variables for starting the game ..
level = 0
regex_list = []
value = "audio"
flag = 1

# Playing ..
for j in range(6):
    ltr_click(value,browser)
    time.sleep(3)
    res = get_results(level,browser)
    #print(f"result = {res}")

    # Checking if the game is over ..
    if (pd.DataFrame(res).evaluation == "correct").all():
        break

    # Checking if the guessed word is not accepted..
    while (not bool(res[0]["evaluation"])):
        time.sleep(1)
        del_word(browser)
        time.sleep(1)
        value = str(fltr(regex_list).sample().values[0])
        time.sleep(1)
        ltr_click(value,browser)
        time.sleep(1)
        res = get_results(level,browser)

    time.sleep(1)

    # Creating objects for the results
    tiles = create_tiles(res)
    #print(f'tiles = {tiles}')
    time.sleep(1)

    # Creating regex for helping to guess the next value..
    regex_list.extend(create_reg(tiles))
    #print(regex_list)
    time.sleep(1)

    # Guessing next value
    value = str(fltr(regex_list).sample(1).values[0])
    #print(f'value = {value}')
    level += 1


# Clicking share button ..
time.sleep(10)
click_share(browser)

# Saving copied result from clipboard..
msg = pc.paste()
print("Success: We solved the puzzle",msg)
time.sleep(1)
browser.close()

# Sending result through Twitter API ..
print("Tweeting through Twitter API ..")
tweet(msg)
#man_tweet.tweet(msg)


time.sleep(3)
