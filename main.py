from datetime import datetime, time
from operator import itemgetter

HORA_INICIAL = time(6, 0, 0)
HORA_FINAL = time(22, 0, 0)
TARIFA_FIXA = 0.36
TARIFA_POR_MINUTO = 0.09

records = [
    {'source': '48-996355555',
     'destination': '48-666666666',
     'end': 1564610974,
     'start': 1564610674},

    {'source': '41-885633788',
     'destination': '41-886383097',
     'end': 1564506121,
     'start': 1564504821},

    {'source': '48-996383697',
     'destination': '41-886383097',
     'end': 1564630198,
     'start': 1564629838},

    {'source': '48-999999999',
     'destination': '41-885633788',
     'end': 1564697158,
     'start': 1564696258},

    {'source': '41-833333333',
     'destination': '41-885633788',
     'end': 1564707276,
     'start': 1564704317},

    {'source': '41-886383097',
     'destination': '48-996384099',
     'end': 1564505621,
     'start': 1564504821},

    {'source': '48-999999999',
     'destination': '48-996383697',
     'end': 1564505721,
     'start': 1564504821},

    {'source': '41-885633788',
     'destination': '48-996384099',
     'end': 1564505721,
     'start': 1564504821},

    {'source': '48-996355555',
     'destination': '48-996383697',
     'end': 1564505821,
     'start': 1564504821},

    {'source': '48-999999999',
     'destination': '41-886383097',
     'end': 1564610750,
     'start': 1564610150},

    {'source': '48-996383697',
     'destination': '41-885633788',
     'end': 1564505021,
     'start': 1564504821},

    {'source': '48-996383697',
     'destination': '41-885633788',
     'end': 1564627800,
     'start': 1564626000}
]


def classify_by_phone_number(records):

    # LISTA SEM REPETIÇÃO
    lista_com_preco = {numero['source']: 0 for numero in records}

    # ADICIONADOD AS TAXA
    for ligacao in records:
        total = TARIFA_FIXA
        for tempo_segundos in range(ligacao['start'], ligacao['end'] - 40, 60):
            tempo_horas = datetime.fromtimestamp(tempo_segundos).time()
            if HORA_INICIAL <= tempo_horas <= HORA_FINAL:
                total += TARIFA_POR_MINUTO

        lista_com_preco[ligacao['source']] += total
    lista_ordenada = sorted(lista_com_preco.items(),
                            key=itemgetter(1),
                            reverse=True)

    # FORMATANDO SAÍDA
    lista_final = []
    for tupla in lista_ordenada:
        dicionario = {'source': tupla[0], 'total': round(tupla[1], 2)}
        lista_final.append(dicionario)

    return lista_final
