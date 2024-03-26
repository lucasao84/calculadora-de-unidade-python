from calculadoraUnidadeDemedidas import *


# ------------ configurando a funcionalidade -----------------

unidade = {'massa': [{'kg':1000}, {'hg':100}, {'dag':10}, {'g':1}, {'dg':0.1}, {'cg':0.01},{'mg':0.001}],
           'comprimento': [{'km':1000}, {'hm':100}, {'dam':10}, {'m':1}, {'dm':0.1}, {'cm':0.01},{'mm':0.001}]}

def mostrar_menu():

    unidade_de = []
    unidade_para = []
    unidade_valores =[]

    for j in unidade['massa']:
        for k, v in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            unidade_valores.append(v)

    c_como['value'] = unidade_de
    c_comop['value'] = unidade_para

mostrar_menu()