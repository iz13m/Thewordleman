# Importing necessary packages..
import pandas as pd
import re
from english_words import english_words_lower_alpha_set
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pyperclip as pc


# Creating data Series of all 5-letter words..

words = pd.Series(list(english_words_lower_alpha_set),name='word')
fwords =words[words.str.match('^\w{5}$')].reset_index().word



true_letters = []

# Identifying objects based on their color as each color produce different regex rule ..
class Green:

    def __init__(self,letter,position):
        self.ltr = letter
        self.pos = position
        true_letters.append(self.ltr)

    def reg(self):
        regex = ['^']
        for i in range(5):
            if i == self.pos:
                regex.append(self.ltr)
            else:
                regex.append(".")
        regex.append("$")
        regex = "".join(regex)
        return [regex]

class Yellow:

    def __init__(self,letter,position):
        self.ltr = letter
        self.pos = position
        true_letters.append(self.ltr)

    def reg(self):
        regex1 = ["^"]
        for i in range(5):
            if i == self.pos:
                regex1.append(f"[^{self.ltr}]")
            else:
                regex1.append(".")
        regex1.append("$")
        regex1 = "".join(regex1)

        regex2= f"^.*{self.ltr}.*$"
        return [regex1, regex2]


class Grey:

    def __init__(self,letter,position):
        self.ltr = letter
        self.pos = position

    def reg(self):
        if self.ltr not in true_letters:
            regex = '^[^'+ self.ltr+']{5}$'
            return [regex]
        else:
            return []

def fltr(rgxs,fwords = fwords):
    for rgx in rgxs:
        fwords = fwords[fwords.str.match(rgx)]
    return fwords


# word entering letter by letter function..
def ent_click(browser):
    """
    This function takes only one argument, the webdriver.
    It clicks on Enter button on the games keyboard.
    """
    webdriver = browser.execute_script("return document.querySelector('game-app').shadowRoot.querySelector('game-keyboard').shadowRoot.querySelector('div')")
    webdriver.find_element_by_css_selector("button[data-key='↵']").click()

def ltr_click(word,browser):
    """
    This function takes two arguments, The word we need to send to the game, and the webdriver
    It iterates through the word letter by letter and clicks on its button on the game's keyboard and then clicks enter.
    """
    webdriver = browser.execute_script("return document.querySelector('game-app').shadowRoot.querySelector('game-keyboard').shadowRoot.querySelector('div')")
    for ltr in word:
        webdriver.find_element_by_css_selector(f"button[data-key='{ltr}']").click()
    ent_click(browser)

def del_word(browser):
    """
    This function takes only one argument, the webdriver
    It clicks 5 times on the backspace button on the game's keyboard
    """
    webdriver = browser.execute_script("return document.querySelector('game-app').shadowRoot.querySelector('game-keyboard').shadowRoot.querySelector('div')")
    for _ in range(5):
        webdriver.find_element_by_css_selector("button[data-key='←']").click()

def get_results(row,browser):
    """
    This function takes two arguments, Which level we're in the game, and the webdriver
    It returns list of dictionaries containing the status of every tile in the game.
    """
    webdriver = browser.execute_script(f"return document.querySelector('game-app').shadowRoot.querySelector('game-row:nth-child({row+1})').shadowRoot.querySelector('div')")
    results=[]
    for i in range(5):
        evaluation = webdriver.find_elements_by_tag_name("game-tile")[i].get_attribute("evaluation")
        letter = webdriver.find_elements_by_tag_name("game-tile")[i].get_attribute("letter")
        results.append({"letter":letter,"evaluation": evaluation,"position":i})
    return results

def click_share(browser):
    """
    This function takes only one argument, the webdriver
    It clicks on the share button on the game screen after the game is finished.
    """
    webdriver = browser.execute_script("return document.querySelector('game-app').shadowRoot.querySelector('game-stats').shadowRoot.querySelector('button')")
    webdriver.click()

def create_tiles(results):
    """
    This function takes only one argument, the result from get result fn (list of dicts)
    It iterates through every tile creating the appropriate object for it depending on its color.
    It returns a list of objects.
    """
    tiles=[]
    for result in results:
        if result['evaluation'] == 'correct':
            tile = Green(letter=result['letter'],position=result['position'])
            tiles.append(tile)
        elif result['evaluation'] == 'present':
            tile = Yellow(letter=result['letter'],position=result['position'])
            tiles.append(tile)
        elif result['evaluation'] == 'absent':
            tile = Grey(letter=result['letter'],position=result['position'])
            tiles.append(tile)
    return tiles

def create_reg(tiles_list):
    """
    This function takes only one argument, the list of tiles objects from create_tiles fn
    It iterates through every object creating the appropriate regex for it depending on its color.
    It returns a list of regex values
    """
    rgx=[]
    for tile in tiles_list:
        rgx.extend(tile.reg())
    return rgx
