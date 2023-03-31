import xml.etree.ElementTree as ET
import random
from datetime import date, timedelta
data_inicial = date(2023, 3, 1)
num_meses = 2
root = ET.Element("faturamento")
for i in range(num_meses):
    mes_element = ET.SubElement(root, "mes", data=data_inicial.strftime("%m/%Y"))
    num_dias_mes = (date(data_inicial.year, data_inicial.month+1, 1) - data_inicial).days
    for j in range(num_dias_mes):
        dia = data_inicial + timedelta(days=j)
        valor = random.randint(2000, 150000)
        dia_element = ET.SubElement(mes_element, "dia", data=dia.strftime("%d/%m/%Y"), valor=str(valor))
    faturamento_mensal = sum([int(dia_element.attrib["valor"]) for dia_element in mes_element])
    ET.SubElement(mes_element, "faturamento_mensal", valor=str(faturamento_mensal))
    data_inicial = date(data_inicial.year, data_inicial.month+1, 1)
tree = ET.ElementTree(root)
tree.write("G:/Atila_Rocha/Programacao/testeTarget/quest03/faturamento.xml", encoding="utf-8", xml_declaration=True)
