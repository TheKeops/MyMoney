import random

def save_currency(file_name=f"save-{random.randint(100000, 999999)}", currency="USD", debug=False):
    try:
        open(f"app/saves/{file_name.strip().lower()}-{currency}.txt", "x", encoding="utf-8")
        if debug == True:
            print(f"{file_name.lower().strip()}-{currency}.txt created successfully! [app/saves/{file_name.lower().strip()}-{currency}.txt]")
        else:
            pass
    except:
        pass