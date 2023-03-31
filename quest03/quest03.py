import xml.etree.ElementTree as ET
tree = ET.parse('G:/Atila_Rocha/Programacao/testeTarget/quest03/faturamento.xml')
root = tree.getroot()
menor_valor = float('inf')
maior_valor = 0
total_faturamento = 0
total_dias = 0
for mes in root.findall('mes'):
    faturamento_mes = 0
    dias_mes = 0
    for dia in mes.findall('dia'):
        valor = float(dia.get('valor'))
        if valor < menor_valor:
            menor_valor = valor
        if valor > maior_valor:
            maior_valor = valor
        faturamento_mes += valor
        dias_mes += 1
    media_mes = faturamento_mes / dias_mes
    for dia in mes.findall('dia'):
        valor = float(dia.get('valor'))
        if valor > media_mes:
            total_dias += 1
    total_faturamento += faturamento_mes
    total_dias += dias_mes
media_geral = total_faturamento / total_dias
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {total_dias}")