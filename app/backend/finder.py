# Transport finder

import os
import json

def get_option(city):
    shorter = ""
    cheaper = ""
    prices   = []
    options  = []
    duration = []
    

    FILE_NAME = "data.json"

    with open(FILE_NAME, 'r',encoding='utf-8') as file:
        data = json.load(file)

    if city != "":
        FILE_NAME = "data.json"

        with open(FILE_NAME, 'r',encoding='utf-8') as file:
            data = json.load(file)

        for i, j in data.items():
            data = j

        for i in data:
            if i["city"] == city:
                options.append(i)

        # Find shorter trip
        for i in options:
            duration.append(int(i["duration"][:-1]))
        

        shorter_duration = min(duration)

        shorter_index = duration.index(shorter_duration)

        shorter = options[shorter_index]

        # Find cheaper trip
        for i in options:
            prices.append(float(i["price_econ"][3:]))

        cheaper = min(prices)

        cheaper_index = prices.index(cheaper)

        cheaper = options[cheaper_index]

    result = {"shorter": shorter,"cheaper": cheaper}

    return (result)

