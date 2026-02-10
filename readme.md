
# ⚙ Okvir za automatsko testiranje Web aplikacije

Projekt za kolegij Metode i tehnike testiranja programske podrške.

## Tehnologije, alati i tehnike korištene

- Jezik: **Python 3.13.0** 
- Okvir za automatizaciju preglednika: **Selenium WebDriver**
- Okvir za testiranje: **Pytest**
- IDE: **VS Code**
- Page Object Model (POM)
- Wait naredbe u Selenium WebDriveru

## Instalacija

1. Kloniranje
```bash
git clone https://github.com/travancicvedran/auto-test-framework.git
cd project
```
2. Dependencies (selenium + pytest)
```bash
pip install -r requirements.txt
```
3. Preuzimanje [Chrome driver-a](https://storage.googleapis.com/chrome-for-testing-public/144.0.7559.133/win64/chromedriver-win64.zip) (spremiti u novu mapu pod drivers/chromedriver.exe)

## Pokretanje

a) Svi testovi redom
```bash
pytest
```
b) Pojedinačni testovi
```bash
pytest tests/test_1.py
```

## Testovi
1. Korisnik ne može ući u razinu koju još nije otključao
2. Korisnik ne može kupiti stavku iz trgovine ukoliko nema "credits"
3. Aplikacija se prebacuje na "Game over screen" nakon što istekne dozvoljena količina vremena (60s)
4. Korisnik može kupiti stavku ukoliko ima dovoljno "credits"
5. Korisnik vraća stanje "credits-a" odabirom "Reset progress" tipke

## Napomene
- [Stranica koja se testira](https://travancicvedran.github.io/ExplosiveGrammar/) je moja kreacija, a predstavlja kviz za učenje gramatike u obliku igre
- Testovi su dizajnirani na način da se mogu pokretati beskonačno mnogo puta (počinje i završava s 0 "credits")
- Očekivani će rezultat izgledati otprilike ovako:
```
5 passed in 87.16s (0:01:27)
```