import geocoder
import math

SKRIDT_METER = 0.59  # gennemsnitlig skridtlængde (Morgan)
JORD_RADIUS = 6373.0  # jordens radius i kilometer
# Vi skal korrigere for at man sjældent går i fugleflugtslinje
# https://math.stackexchange.com/questions/2877479/average-ratio-of-manhattan-distance-to-euclidean-distance
EUCLID_MANHATTAN = 1.27  # faktor mellem fugleflugt og faktisk afstand

def beregn_km(lat1, lon1, lat2, lon2):
    # Benytter Haversine Formula, som er beskrevet på link herunder
    # https://www.kite.com/python/answers/how-to-find-the-distance-between-two-lat-long-coordinates-in-python
    lat1 = math.radians(lat1)  # breddegrad i radianer
    lon1 = math.radians(lon1)  # længdegrad i radianer
    lat2 = math.radians(lat2)  # breddegrad i radianer
    lon2 = math.radians(lon2)  # længdegrad i radianer
    dlon = lon2 - lon1  # afstand mellem længdegrader i radianer
    dlat = lat2 - lat1  # afstand mellem længdbreddegrader i radianer
    # kompliceret matematik...
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    fugleflugt_km = JORD_RADIUS * c
    # vi estimerer hvor meget længere turen er i.f.t. fugleflugtslinjen
    afstand_km = fugleflugt_km * EUCLID_MANHATTAN
    return afstand_km

adr1 = input('Skriv den første adresse eller dudu bliver sur: ')
adr2 = input('Skriv den anden adresse eller guchigu får kød til aftensmad: ')

# https://geocoder.readthedocs.io/providers/OpenStreetMap.html
g1 = geocoder.osm(adr1.strip())
g2 = geocoder.osm(adr2.strip())
lat1, lon1 = g1.json['bbox']['northeast']
lat2, lon2 = g2.json['bbox']['northeast']

afstand_km = beregn_km(lat1, lon1, lat2, lon2)
antal_skridt = 1000*afstand_km / SKRIDT_METER
print(f'kilometer: {round(afstand_km, 2)}')
print(f'antal skridt: {int(antal_skridt)}')
