# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:00:38 2020

@author: shyam

DICTIONARY[similar to switch]
"""
weekdays={
    "sun":"sunday",
    "mon":"monday",
    "tue":"tuesday",
    "wed":"wednesday",
    "thu":"thursday",
    "fri":"friday",
    "sat":"saturday"
}
print(weekdays["sun"])
print(weekdays.get("thu"))
print(weekdays.get("thor","invalid"))