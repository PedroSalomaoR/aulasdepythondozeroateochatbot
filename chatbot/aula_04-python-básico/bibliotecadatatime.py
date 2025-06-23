#Aula sobre horas, dias, meses, anos, segundos e minutos
from datetime import datetime

agora = datetime.now()
print(agora)
print(agora.year)   # Ano
print(agora.month)  # Mês
print(agora.day)    # Dia
print(agora.hour)   # Hora
print(agora.minute) # Minuto

data_formatada = agora.strftime("%d/%m/%Y %H:%M")
print("Data formatada:", data_formatada)
