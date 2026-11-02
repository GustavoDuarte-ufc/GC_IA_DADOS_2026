frutas_traducao = {
    # Frutas comuns
    "apple": "maçã",
    "banana": "banana",
    "orange": "laranja",
    "grape": "uva",
    "strawberry": "morango",
    "pineapple": "abacaxi",
    "watermelon": "melancia",
    "melon": "melão",
    "mango": "manga",
    "papaya": "mamão",
    "peach": "pêssego",
    "pear": "pera",
    "cherry": "cereja",
    "lemon": "limão",
    "coconut": "coco",
    "kiwi": "kiwi",
    "avocado": "abacate",
    "plum": "ameixa",
    "raspberry": "framboesa",
    "blueberry": "mirtilo",

    # Frutas cítricas
    "lime": "lima",
    "tangerine": "tangerina",
    "mandarin": "mandarina",
    "grapefruit": "toranja",
    "pomelo": "pomelo",
    "kumquat": "quincã",
    "citron": "cidra",
    "clementine": "clementina",
    "blood orange": "laranja sanguínea",
    "bitter orange": "laranja amarga",
    "key lime": "limão-galego",
    "bergamot orange": "bergamota",

    # Frutas tropicais
    "passion fruit": "maracujá",
    "guava": "goiaba",
    "dragon fruit": "pitaya",
    "star fruit": "carambola",
    "lychee": "lichia",
    "jackfruit": "jaca",
    "durian": "durião",
    "rambutan": "rambutã",
    "longan": "longana",
    "mangosteen": "mangostão",
    "breadfruit": "fruta-pão",
    "soursop": "graviola",
    "custard apple": "fruta-do-conde",
    "sugar apple": "pinha",
    "cherimoya": "cherimoia",
    "sapodilla": "sapoti",
    "tamarind": "tamarindo",
    "persimmon": "caqui",
    "fig": "figo",
    "date": "tâmara",
    "pomegranate": "romã",
    "prickly pear": "figo-da-índia",
    "salak": "salaca",
    "langsat": "langsat",
    "marula": "marula",
    "ackee": "aki",
    "noni": "noni",

    # Frutas vermelhas e silvestres
    "blackberry": "amora",
    "cranberry": "oxicoco",
    "gooseberry": "groselha-espim",
    "redcurrant": "groselha vermelha",
    "blackcurrant": "groselha preta",
    "white currant": "groselha branca",
    "elderberry": "sabugueiro",
    "boysenberry": "amora-boysen",
    "loganberry": "amora-logan",
    "mulberry": "amora-da-amoreira",
    "cloudberry": "amora-ártica",
    "lingonberry": "airela",
    "huckleberry": "huckleberry",
    "acai berry": "açaí",
    "jabuticaba": "jabuticaba",

    # Frutas brasileiras
    "acerola": "acerola",
    "cashew apple": "caju",
    "cupuacu": "cupuaçu",
    "pitanga": "pitanga",
    "caja": "cajá",
    "umbu": "umbu",
    "seriguela": "seriguela",
    "bacuri": "bacuri",
    "buriti": "buriti",
    "pequi": "pequi",
    "murici": "murici",
    "araca": "araçá",
    "camu camu": "camu-camu",
    "grumichama": "grumixama",
    "mangaba": "mangaba",
    "genipap": "jenipapo",
    "guarana": "guaraná",
    "baru": "baru",
    "abiu": "abiu",
    "biriba": "biribá",
    "bacaba": "bacaba",
    "tucuma": "tucumã",
    "pupunha": "pupunha",

    # Outras frutas e variedades
    "nectarine": "nectarina",
    "apricot": "damasco",
    "quince": "marmelo",
    "loquat": "nêspera",
    "medlar": "nêspera-europeia",
    "jujube": "jujuba",
    "olive": "azeitona",
    "plantain": "banana-da-terra",
    "horned melon": "kiwano",
    "pepino melon": "pepino-doce",
    "feijoa": "goiaba-serrana",
    "tamarillo": "tomate-de-árvore",
    "physalis": "fisális",
    "ground cherry": "fisális",
    "miracle fruit": "fruta-do-milagre",
    "monstera fruit": "fruta-da-costela-de-adão",
    "buddha's hand": "mão-de-buda",
    "rose apple": "jambo",
    "wax apple": "jambo-d'água",
    "ambarella": "cajá-manga",
    "bilimbi": "bilibim",
    "elephant apple": "maçã-de-elefante"
}

def traduzir_fruta(nome_fruta: str) -> str:
    global frutas_traducao
    return frutas_traducao.get(nome_fruta.lower(), False)

def fruta_em_ingles(nome_fruta: str):
    global frutas_traducao
    
    chave = next(
        (chave for chave, valor in frutas_traducao.items() if valor == nome_fruta.lower()),
        nome_fruta if traduzir_fruta(nome_fruta) is not False else False
    )
    
    return chave


