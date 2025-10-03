# modules/create_files.py

import os
import locale
import json
import random
import pip
import requests

def create_and_insert_default_settings():
    try:
        language, _null = locale.getdefaultlocale()
        if language == "tr_TR":
            lang = "tr"
            _currency = "TRY"
        else:
            lang = "en"
            _currency = "USD"
    except:
        lang = "en"
        _currency = "USD"

    if not os.path.exists("app"):
        os.makedirs("app")
    
    if not os.path.exists("app/saves"):
        os.makedirs("app/saves")

    try:
        open("app/settings.json", 'x', encoding="utf-8")
        open("app/version.txt", 'x', encoding="utf-8")
    except:
        pass
    
    settings_path = os.path.join("app", "settings.json")
    
    if os.path.isfile(settings_path):
        with open("app/version.txt", 'r', encoding='utf-8') as f:
            version = f.read().strip()

        with open(settings_path, 'r', encoding='utf-8') as f:
            if f.read().strip() == "":
                with open("app/version.txt", 'w', encoding='utf-8') as f:
                    response = requests.get("https://raw.githubusercontent.com/TheKeops/MyMoney/main/app/version.txt")
                    f.write(response.text.strip())

                default_settings = {
                    "theme": "system", 
                    "language": f"{lang}",
                    "currency": f"{_currency}",
                    "version": f"{version}",
                    "auto_refresh": False,
                    "user": {
                        'name': f'user{random.randint(1000, 9999)}',
                        'surname': 'default'
                    },
                    "appdata": {
                        'first_run': True
                    }
                }
                
                with open(settings_path, 'w', encoding='utf-8') as f:
                    json.dump(default_settings, f, ensure_ascii=False, indent=4)

            else:
                with open(settings_path, 'r', encoding='utf-8') as f:
                    _flag = json.load(f)

                    if _flag["appdata"]["first_run"] == True:

                        default_settings = {
                            "theme": "system", 
                            "language": f"{lang}",
                            "currency": f"{_currency}",
                            "version": f"{version}",
                            "auto_refresh": False,
                            "user": {
                                'name': f'user{random.randint(1000, 9999)}',
                                'surname': 'default'
                            },
                            "appdata": {
                                'first_run': False
                            }
                        }
                        
                        with open(settings_path, 'w', encoding='utf-8') as f:
                            json.dump(default_settings, f, ensure_ascii=False, indent=4)

def control_lib(library_names=list, auto_installer=False, debug=False):
    if auto_installer == False:
        for lib in library_names:
            try:
                __import__(lib)
                if debug == True:
                    print(f"{lib} available!")
                else:
                    pass
            except ImportError:
                if debug == True:
                    print(f"{lib} not defined!")
                else:
                    pass
    else:
        for lib in library_names:
            try:
                __import__(lib)
                if debug == True:
                    print(f"{lib} available!")
                else:
                    pass
            except ImportError:
                if debug == True:
                    print(f"{lib} not defined!")
                    pip.main(["install",f"{lib}"])
                else:
                    pass
