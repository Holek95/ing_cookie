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
konkretny tag
```commandline
behave --tags=@fast
```
lub test konkretny scenariusz
```commandline
behave features/test_cookie.feature 
```
### Równoległe uruchomienie testów
w celu uruchomienia wybranego scenariusza należy użyć
```commandline
behavex features/test_cookie.feature --parallel-processes 4 --tags=@multiple --parallel-scheme scenario
```