# ```Testy automatyczne```

## Pierwsze uruchmienie
należy pobrać wszystkie wymagane pakiety
```commandline
pip install -r requirements.txt
```
oraz driver'y przeglądarek
```commandline
playwright install
```
## Uruchamianie testów
żeby uruchomić wszystkie testy
```commandline
behave
```
lub konkretny test
```commandline
behave features/test_cookie.feature 
```