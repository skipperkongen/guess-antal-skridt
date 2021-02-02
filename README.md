# Antal skridt mellem to steder på jorden

Dette er et program, som gætter på hvor mange skridt der er mellem to steder på jorden. Programmet er skrevet i Python3 og benytter geocoding biblioteket `geocoder`.

## Installation

Opret og brug virtual environment i samme mappe som programmet:

```
# Mac eller Linux
python3 -m venv venv
source venv/bin/activate
```

Installer geocoding bibliotek:

```bash
pip install geocoder
```

## Eksempel

Kør programmet:

```
$ python skridt.py                                                                                                                          [12:01:06]
Skriv den første adresse: Hannovergade 2, 2300
Skriv den anden adresse: Lybækgade 20, 2300
kilometer: 0.46
antal skridt: 781
```
