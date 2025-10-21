# modules/currency_updater_bot.py

import modules.getdata as getdata
import os
import json
import datetime


def start_currency_update():
    with open("app/settings.json") as f:
        settings = json.load(f)

    for files in os.listdir("app/saves"):
        for file in os.listdir("app/saves/" + files):
            if file.endswith(".txt"):
                with open(
                    "app/saves/" + files + "/data-info.json", "r", encoding="utf-8"
                ) as f:
                    data_info = json.load(f)

                currency = data_info["currency"]
                firts_money = data_info["first_money"]
                to = data_info["to"]

                currency_type = currency + "=" + to

                _currency = getdata.get_currency_data(currency=currency_type)

                converted = float(_currency) * float(firts_money)
                converted = round(converted, 2)

                date = datetime.datetime.now()
                date = date.strftime("%d/%m/%Y %H:%M:%S")

                with open(
                    "app/saves/" + files + "/" + file, "a", encoding="utf-8"
                ) as f:
                    f.writelines(f"{converted} TRY - {date}\n")
            else:
                pass
