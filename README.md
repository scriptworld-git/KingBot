# king-bot

check out the insights of this project: [kingbot.scriptworld.net](https://kingbot.scriptworld.net)

feel free to join the project or __[contact me! (:](mailto:f.breuer@scriptworld.net)__

[![Build Status](https://travis-ci.org/scriptworld-git/king-bot.svg?branch=master)](https://travis-ci.org/scriptworld-git/king-bot)
[![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/scriptworld-git/king-bot/blob/master/LICENSE)
[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)

# installation

1.  install python3 for your system
    1.  [get python](https://www.python.org/downloads/)
2.  install selenium package
    1.  open console as administrator
    2.  `pip3 install selenium`
3.  clone this repository
4.  download chromedriver for your system
    1.  [get chromederiver](http://chromedriver.chromium.org)
    2.  move to `assets/` folder
    3.  edit chromedriver path in `start.py` line 7
        1.  `chromedriverPath = 'enter path here'`
5.  store your login credentials
    1.  create file named `credentials.txt` in `assets/` folder
    2.  write your email and password like following
    3.  `test@gmail.com;my_password`
    4.  save the file
6.  edit `start.py`
    1.  edit your gameworld in line 8 `world = 'COM4'`
        1.  make sure to use uppercase!
    2.  place the actions your bot have to do at the end
        1.  read documentation for this
7.  execute in console:
    1.  `python3 start.py`
    2.  read documentation for options like remote browser or headless browsing

# documentation

the first code snippet in each section always shows some example implementation of the action you want to perform.

## specify the bot

### farmlists

```python
# sends farmlist with index 1 (the one after the starter list)
# in your first village (index 0) in an interval of 60 seconds
game.startFarming(0, [1], 60)

#sends farmlist 1 and 3 in your second village in an interval of 30 seconds
game.startFarming(1, [1,3], 30)
```

**first param:**  
index of village (0 is the first village)

**second param:**  
index of farmlist (0 is the starter list with only 10 farms)  
must be an _array_! you can send multiple lists in this interval

**third param:**  
interval of sending the list _in seconds_

you can stack as many of them together if you want.  
it's also possible to send different farmlist in the same village in different intervals.

### adventures

```python
game.enableAdventures()
```

this enables auto sending the hero on adventures.  
be careful if the hero in low on health! there is no stopping mechanism for now.

### upgrade resource fields

```python
game.upgradeSlot(0, 5)
```

this function will upgrade the resource field with id 5 for one level in your first village.

on the picture below you can see all field id's.  
these stay the same no matter what kind of village you have (even in 15er crop villages).

![resource-fields](https://scriptworld.net/assets/king-bot/resourceFields.png)

## start options

### remote browser

```bash
$ python3 start.py -r
```

if the script exists because of an exception, it's possible to re-use the browser session so you don't have to go through the whole login process again.  
just don't exit the browser window and make sure to remove the functions in the script, which the bot already completed in last session.

### headless browsing

```bash
$ python3 start.py -h
```

if you don't wont a browser window to pop up, or using the script on a dedicated server with no gui, it is possible to run the script in headless mode.  
the console window will inform you about important actions the bot will do.

---

_i love lowercase_
