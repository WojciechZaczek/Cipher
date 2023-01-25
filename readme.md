# Content of Project

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detailed information about modules](#more-detailed-information-about-modules)
* [Application view](#application-view)









### CIPHER

Cipher program based on facade design pattern

1. ROT13, ROT47 (SZYFR CEZARA) -> [https://pl.wikipedia.org/wiki/Szyfr_Cezara](https://pl.wikipedia.org/wiki/Szyfr_Cezara)
### FUNCTIONALITIES

##### 2 FLOW
- Decrypt: wczytujesz plik: podaj user nazwe -> pakujesz to do buffer -> I dajesz mozliwosc odszyfrowanie
- Encrypt: user podaje slowo, zdanie ty szyfrujesz -> buffer -> zapis do pliku, exit: Coś znajduje się w bufferze?

- FILEHANDLER (.json)
    - Odczyt i zapis do pliku
    - User podaje nazwe pliku
    - Wyjątki -> walidacja co podal user, walidacja czy plik istnieje((moduł os) Folder np. files)
    - Gdy uzytkownik chce zapisac do tego samego pliku no to append -> Dopisanie do pliku (odpowiednie otwarcie)
- Szyfrowanie i Odszyfrowywanie
- Buffer (BUFOR) # -> Lista, która jest w pamięci []
    - Add to buffer
    - remove from buffer
- MENU
- Manager (multi inheritance < composition) # -> Klasa wykonujaca (start, end)
- Exit
- Unit Tests

### Object Structure

- Class Text
    - {"cipher": "rot47", "text": "yquu", "status": "encrypted"}

### Additional Things
- Abstract/Factory method
  - IOReader -> io.print("Cześć", "to mój program", "1.Menu"), io.read("Please provide value") # *args
  ''' class IO:
    def print(*args):
      for word in args:
          print(word)
    def read(text):
      return input(text)
  from xyz import IOReader as io


### Tools

- Bandit, black,
- - precommita

### Styling

- PEP 8
- GITFLOW
- Often commits
- Conventional commits -> [https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/) np. feat: xyz
- type hints -> (mypy*)
- Docstring
