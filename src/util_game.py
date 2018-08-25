from .custom_driver import client
from .utils import log


def close_modal(browser: client):
    el = browser.find("//div[@class='modalContent']")
    el = el.find_element_by_xpath(".//a[@class='closeWindow clickable']")
    browser.click(el)


def close_welcome_screen(browser: client):
    wc = browser.find("//div[contains(@class, 'welcomeScreen')]")
    log("closing welcome-screen")
    el = wc.find_element_by_xpath(
        ".//a[@class='closeWindow clickable']")
    browser.click(el)


def check_resources(browser: client) -> {}:
    resources_list = ["wood", "clay", "iron", "crop"]
    resources = {}
    for res in resources_list:
        find_resources = browser.find("//div[@class='stockContainer {0}']".format(res))
        find_resources = find_resources.find_element_by_xpath(".//div[contains(@class, 'progressbar')]")
        value = int(find_resources.get_attribute("value"))
        resources[res] = value
    return resources

def shortcut(browser: client, shortcut: str):
    shortcut_list = ["marketplace", "barrack", "stable", "workshop"]
    shortcut_link = browser.find("//div[@id='quickLinks']")
    shortcut_link = shortcut_link.find_element_by_xpath(".//div[contains(@class, 'slotWrapper')]")
    link = shortcut_link.find_elements_by_xpath(".//div[contains(@class, 'slotContainer')]")
    browser.click(link[shortcut_list.index(shortcut.lower())], 1)

def village_list(browser: client) -> []:
    villages_list = []
    ul = browser.find("//div[contains(@class, 'villageListDropDown')]")
    ul = ul.find_element_by_xpath(".//ul")
    lis = ul.find_elements_by_xpath(".//li")
    for village in lis:
        village_name = village.find_element_by_xpath(".//div[contains(@class, 'villageEntry')]")
        village_name = village_name.get_attribute("innerHTML")
        villages_list.append(village_name)
    return villages_list

def stationed_troops(browser: client) -> dict:
    troops_dict = {}
    foo = 0
    troops_stationed = browser.find("//div[@id='troopsStationed']/ul/ul")
    lis = troops_stationed.find_elements_by_xpath(".//li")
    tribe = lis[0].get_attribute("tooltip-translate")
    troop_name = troops_name(browser, tribe)
    for listed in lis[2:]:
        div = listed.find_element_by_xpath(".//div")
        troop_amount = div.get_attribute("innerHTML")
        if len(troop_amount) == 0:
            troops_dict[troop_name[foo]] = 0
            foo += 1
        else:
            troops_dict[troop_name[foo]] = int(troop_amount)
            foo += 1
    return troops_dict

def troops_name(browser: client, tribe: str) -> list:
    troops_dict = {"tribe_1":
        ["Legionnaire","Praetorian","Imperian","Equites Legati", "Equites Imperatoris", "Equites Caesaris", "Battering Ram", "Fire Catapult", "Senator", "Settler", "Hero"],
        "tribe_3":
        ["Phalanx", "Swordsman", "Pathfinder", "Theutates Thunder", "Druidrider", "Haeduan", "Ram", "Trebuchet", "Chieftain", "Settler", "Hero"],
        "tribe_2":
        ["Clubswinger", "Spearfighter", "Axefighter", "Scout", "Paladin", "Teutonic Knight", "Ram", "Catapult", "Chief", "Settler", "Hero"]}
    return troops_dict[tribe.lower()]
