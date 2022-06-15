Champlist={"volibear": "Rammus",
           "Shyvana": "Morderkaiser",
           "rammus": "Morderkaiser",
           "morderkaiser": "Elise",
           "trundle": "Ekko",
           "zac": "Morderkaiser",
           "warwick": "Rammus",
           "wukong": "Shyvana",
           "skarner": "Morderkaiser",
           "poppy": "Rammus",
           "diana": "Volibear",
           "nunu": "Wukong",
           "sejuani": "Shyvana",
           "ekko": "Rammus",
           "nocturne": "Shyvana",
           "amumu": "Morderkaiser",
           "vi": "Zac",
           "kayn": "Trundle",
           "fiddlesticks": "Morderkaiser",
           "reksai": "Volibear",
           "lillia": "Diana",
           "gragas": "Rammus",
           "belveth": "Rammus",
           "khasix": "Volibear",
           "elise": "Volibear",
           "talon": "Olaf",
           "udyr": "Morderkaiser",
           "kindred": "Rammus",
           "viego": "Rammus",
           "shaco": "Volibear",
           "jax": "Zed",
           "xin zhao": "Volibear",
           "qiyana": "Morderkaiser",
           "evelynn": "Rengar",
           "olaf": "Trundle",
           "graves": "Poppy",
           "master yi": "Rammus",
           "hecarim": "Morderkaiser",
           "jarvan iv": "Morderkaiser",
           "rengar": "Shyvana",
           "zed": "Poppy",
           "karthus": "Fiddlesticks",
           "nidalee": "Morderkaiser",
           "ivern": "Gragas",
           "gwen": "Hecarim",
           "twitch": "Elise",
           "taliyah": "Shyvana",
           "lee sin": "Rammus"
           }
print("Welcome to the Jungle Matchup calculator!")
print("This was developed by a suspected hypergenius with an interest in League of Legends")
print("This hypergenius had a specific interest in the Jungle role, as it requires the highest IQ")
print("To use this cyberbot, please enter the enemy Junglers champ pick, and the bot will spit out exactly (highly calculated) who you should pick")
Enemychamp=input(print("Please select the enemy champion"))
Choice=Enemychamp.lower()
print(Champlist[Choice])

number = ""
while number != "123":
   Enemychamp=input()
   Choice = Enemychamp.lower()
   print(Champlist[Choice])
