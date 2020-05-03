def get_input(text):
    return input(text)
def data_extenso():
    data_testada = get_input("Digite data no formato dd/mm/aaaa")
    meses = ["janeiro",
             "fevereiro",
             "março",
             "abril",
             "maio",
             "junho",
             "julho",
             "agosto",
             "setembro",
             "outubro",
             "novembro",
             "dezembro",
             ]
    dia, mes, ano = data_testada.split("/")
    mes_extenso = meses[int(mes)-1]
    return f"{dia} de {mes_extenso} de {ano}"