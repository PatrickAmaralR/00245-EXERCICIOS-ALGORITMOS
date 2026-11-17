
total_t = 10
contador = 0
contador_v = 0
urgentes = 0
total_m = 0
maior = 0

while contador < total_t:

    print("Ticket", contador + 1)

    prioridade = int(input("Introduza a prioridade (1 a 5): "))
    tempo = int(input("Introduza o tempo estimado (minutos): "))

    if prioridade < 1 or prioridade > 5 or tempo < 1:
        print("NO PRIORITY")

    else:
        contador_v = contador_v + 1

        if prioridade == 1 or prioridade == 2:
            urgentes = urgentes + 1

        total_m = total_m + tempo

        if tempo > maior:
            maior = tempo

    contador = contador + 1

if contador_v > 0:
    media = total_m / contador_v
else:
    media = 0

if urgentes >= 5 or total_m > 600:
    classificacao = "CRÍTICA"

elif urgentes >= 3 or total_m > 480:
    classificacao = "ELEVADA"

else:
    classificacao = "NORMAL"

print("\n--- RESULTADOS ---")
print("Total de tickets:", contador)
print("Tickets válidos:", contador_v)
print("Tickets urgentes:", urgentes)
print("Total de minutos:", total_m)
print("Média de minutos:", media)
print("Maior tempo estimado:", maior)
print("Classificação:", classificacao)
