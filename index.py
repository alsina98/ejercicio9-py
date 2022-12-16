from datetime import datetime

x = datetime.now() # 2022-11-10 16:18:54.795822

horaSistema = x.strftime("%X") # 16:19:14

horaEntrada = "09:30:00"
horaSalida = "19:00:00"

formatHora = "%H:%M:%S"

he = datetime.strptime(horaSistema,formatHora)
hs = datetime.strptime(horaSalida,formatHora)

if horaSistema >= horaEntrada:
    if horaSistema <= horaSalida:
        totalHoras = hs - he
        print("Hora sistema", horaSistema)
        print("Hora de salida", horaSalida)
        print("Total horas", str(totalHoras))
    else:
        print("Ya es hora de irse a casa:", horaSistema)
else:
    print("Aun no es hora de ir al trabajo:", horaSistema)