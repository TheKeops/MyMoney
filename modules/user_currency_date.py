# modules/user_currency_date.py

import random
import os
import datetime
import json


def save_currency_saves(
    file_name=f"save-{random.randint(100000, 999999)}",
    currency="USD",
    currency_to="TRY",
    available_money=float,
):
    try:
        os.makedirs(
            f"app/saves/{file_name.replace(' ', '-').lower().strip()}-{available_money}{currency}-to-{currency_to}",
            True,
        )
        try:
            file_random_id = random.randint(10000000, 90000000)
            try:
                open(
                    f"app/saves/{file_name.replace(' ', '-').lower().strip()}-{available_money}{currency}-to-{currency_to}/{file_name.replace(' ', '-').strip().lower()}-{file_random_id}-data-save-mymoney.txt",
                    "x",
                    encoding="utf-8",
                )
                open(
                    f"app/saves/{file_name.replace(' ', '-').lower().strip()}-{available_money}{currency}-to-{currency_to}/data-info.json",
                    "x",
                    encoding="utf-8",
                )
            except Exception as e:
                print(e)

            with open(
                f"app/saves/{file_name.replace(' ', '-').lower().strip()}-{available_money}{currency}-to-{currency_to}/data-info.json",
                "w",
                encoding="utf-8",
            ) as f:
                default_settings = {
                    "name": f"{file_name.lower().strip().replace(' ', '-')}",
                    "currency": f"{currency.upper().strip()}",
                    "to": f"{currency_to.upper().strip()}",
                    "first_money": f"{str(available_money).strip()}",
                    "first_import_date": f"{datetime.datetime.now()}",
                }

                json.dump(default_settings, f, ensure_ascii=False, indent=4)
        except:
            pass
    except:
        pass
