import time
from datetime import datetime
from pytz import timezone
import time
from time import sleep

# utilizando a Lib TIME
# print(time.localtime())
# print(time.localtime().tm_year)

# utilizando a Lib DATETIME
# print(datetime.today())
# print(datetime.now().date())
# print(datetime.now().time())

# utilizando a Lib PYTZ
dthr = datetime.now()
print(dthr)
fuso_br = timezone('America/Sao_Paulo')
print(fuso_br)
sp = dthr.astimezone(fuso_br)
sp_formatado = sp.strftime('%d|%m|%Y  %H:%M')
teste_hora = sp.strftime(' %H:%M')
print(sp)
print(sp_formatado)
sleep(3)

print(teste_hora)

