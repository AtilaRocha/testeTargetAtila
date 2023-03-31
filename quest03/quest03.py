import json
with open('G:/Atila_Rocha/Programacao/testeTarget/quest03/dados.json') as f:
    data = json.load(f)
menor_valor = sorted(data, key=lambda x: x['valor'])[0]['valor']
maior_valor = sorted(data, key=lambda x: x['valor'], reverse=True)[0]['valor']
total_faturamento = sum([dia["valor"] for dia in data])
media_mensal = total_faturamento / len(data)
dias_acima_media = 0
for dia in data:
    if dia["valor"] > media_mensal:
        dias_acima_media += 1
print(f"Menor valor de faturamento ocorrido em um dia do mês: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento ocorrido em um dia do mês: R$ {maior_valor:.2f}")
print(f"O total de dias acima da Média Mensal ({media_mensal:.2f}): {dias_acima_media} dias")