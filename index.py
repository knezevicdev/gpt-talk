from tekst_u_govor import pricaj
from govor_u_tekst import procesuiraj
from gpt import pitaj_gpt

poruke = []

while True:
    pitanje = procesuiraj()
    print("Pitanje: " + pitanje)
    poruke.append({"role": "user", "content": pitanje})
    odgovor = pitaj_gpt(pitanje, poruke)
    print("Odgovor: " + odgovor)
    pricaj(odgovor)
    poruke.append({"role": "system", "content": odgovor})

