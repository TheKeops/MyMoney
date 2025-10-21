# modules/create_files.py

import os
import locale
import json
import random
import pip
import requests
import datetime


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
        open("app/settings.json", "x", encoding="utf-8")
        open("app/version.txt", "x", encoding="utf-8")
    except:
        pass

    settings_path = os.path.join("app", "settings.json")

    if os.path.isfile(settings_path):
        with open(settings_path, "r", encoding="utf-8") as f:
            if f.read().strip() == "":
                with open("app/version.txt", "w", encoding="utf-8") as f:
                    response = requests.get(
                        "https://raw.githubusercontent.com/TheKeops/MyMoney/main/app/version.txt"
                    )
                    f.write(response.text.strip())

                with open("app/version.txt", "r", encoding="utf-8") as f:
                    version = f.read().strip()

                default_settings = {
                    "theme": "system",
                    "language": f"{lang}",
                    "currency": f"{_currency}",
                    "version": f"{version}",
                    "auto_refresh": False,
                    "user": {
                        "name": f"user{random.randint(1000, 9999)}",
                        "surname": "default",
                    },
                    "appdata": {"first_run": True},
                }

                with open(settings_path, "w", encoding="utf-8") as f:
                    json.dump(default_settings, f, ensure_ascii=False, indent=4)

            else:
                with open(settings_path, "r", encoding="utf-8") as f:
                    _flag = json.load(f)

                with open("app/version.txt", "r", encoding="utf-8") as f:
                    version = f.read().strip()

                    if _flag["appdata"]["first_run"] == True:
                        default_settings = {
                            "theme": "system",
                            "language": f"{lang}",
                            "currency": f"{_currency}",
                            "version": f"{version}",
                            "auto_refresh": False,
                            "user": {
                                "name": f"user{random.randint(1000, 9999)}",
                                "surname": "default",
                            },
                            "appdata": {"first_run": False},
                        }

                        with open(settings_path, "w", encoding="utf-8") as f:
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
                    pip.main(["install", f"{lib}"])
                else:
                    pass


def create_paper(
    machine=False,
    analysis_type="Kar Analiz",
    report_name="DEFAULT_REPORT",
    analysis_results=None,
    machine_results=None,
    report_notes="Herhangi bir raport notu eklenmedi.",
    save_path=str,
):
    """
    Makina = Makina analizi sonuçlarını ekler.
    Analiz Türü = Kar Analizi, Son 5 Analiz, Son 2 Analiz
    """

    try:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")

        open(
            f"{desktop}/{str(report_name).strip().lower()}-report.txt",
            "x",
            encoding="utf-8",
        ).close()
    except:
        pass

    with open(
        f"{desktop}/{str(report_name).strip().lower()}-report.txt",
        "w",
        encoding="utf-8",
    ) as f:
        f.writelines(f"MyMoney Raporu ({report_name} [{save_path}])\n")
        f.writelines("====================================\n\n")

        with open("app/settings.json", "r", encoding="utf-8") as settings_file:
            settings = json.load(settings_file)
            f.writelines(
                f"Kullanıcı Adı: {settings['user']['name']} {settings['user']['surname']}\n"
            )
            f.writelines(
                f"Tarih: {str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))}\n"
            )
            f.writelines(f"Uygulama Sürümü: {settings['version']}\n")
            f.writelines(f"Dil: {str(settings['language']).upper()}\n")
            f.writelines(f"Varsayılan Para Birimi: {settings['currency']}\n\n")

        f.writelines("====================================\n\n")

        f.writelines(
            "* Yukarıda verilen bilgilere ait kullanıcı tarafından MyMoney uygulaması üzerinden talep edilen raporun detayları aşağıda belirtilmiştir.\n\n"
        )

        f.write(
            f"""
Analiz Türü: {analysis_type}
Makina Analizi: {"Evet" if machine == True else "Hayır"}
Rapor Adı: {report_name} [{save_path}]
Rapor Oluşturma Tarihi: {str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))}

Analiz Sonuçları :
------------------------------------
{analysis_results if analysis_results else "Buraya analiz sonuçları eklenecek."}

Makina Analizi Sonuçları :
------------------------------------
{machine_results if machine_results else "Buraya makina analizi sonuçları eklenecek."}

Rapor Notları :
------------------------------------
{report_notes}

MyMoney uygulamasını kullandığınız için teşekkür ederiz!
"""
        )
