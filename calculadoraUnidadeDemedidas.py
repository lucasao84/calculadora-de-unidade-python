from tkinter import *
from tkinter import ttk
from funcao.unidade import *

# ------------ configurando a funcionalidade -----------------

unidade = {'massa': [{'kg':1000}, {'hg':100}, {'dag':10}, {'g':1}, {'dg':0.1}, {'cg':0.01},{'mg':0.001}],
           'comprimento': [{'km':1000}, {'hm':100}, {'dam':10}, {'m':1}, {'dm':0.1}, {'cm':0.01},{'mm':0.001}]}

def mostrar_menu(i):

    unidade_de = []
    unidade_para = []
    unidade_valores =[]

    for j in unidade[i]:
        for k, v in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            unidade_valores.append(v)

    

    c_como['value'] = unidade_de
    c_comop['value'] = unidade_para

    label_unidade['text'] = i

    # label digitar numero

    label_digite = Label(terceiro_frame, width=20, text='Digite um numero abaixo', bg=cor2, fg=cor1 , font=('Arial 10 bold'))
    label_digite.place(x=12, y=130)

    #entry

    l_entry = Entry(terceiro_frame, width=8, relief='solid',justify='center' ,font=('Ivy 14 bold'))
    l_entry.place(x=10, y=165)

    #botão calcular

    l_butao = Button(terceiro_frame,command=calcular ,width=10,text='CALCULAR', relief='raised', font=('Ivy 8 bold'), bg=cor3, fg=cor2)
    l_butao.place(x=108, y=165)
    

    #label

    global label_resultado

    label_resultado = Label(terceiro_frame,width=14,padx=3,height=1 ,text='---', bg=cor2, fg=cor1, font=('Ivy 14 bold'), relief='solid', anchor='center')
    label_resultado.place(x=10, y=205)


def calcular():

    #obtendo as unidades

    a = c_como.get()
    b = c_comop.get()

    #obtendo os numeros
    numero_para_converte = float(label_resultado.get())

    print(a, b , numero_para_converte)

# importanto pillow

from PIL import ImageTk, Image

# cores

cor1 = '#3b3b3b' # preta / black
cor2 = '#ffffff' # branca / white
cor3 = '#48b3e0' # azul / blue


# Configurando janela

janela = Tk()
janela.title("")
janela.geometry('650x260')
janela.config(bg='black')

# dividindo frames

primeiro_frame = Frame(janela, width=449.49, height=50, relief='flat', bg=cor2 , padx=0, pady=3)
primeiro_frame.place(x=2, y=2)

segundo_frame = Frame(janela, width=450, height=210, relief='flat', bg=cor2,  padx=0, pady=3)
segundo_frame.place(x=2, y=54)

terceiro_frame = Frame(janela, width=200, height=260, relief='solid', bg=cor2,  padx=0, pady=3) 
terceiro_frame.place(x=454, y=2)

#Label_titulo

titulo = Label(primeiro_frame, text='CALCULADORA DE UNIDADES DE MEDIDAS', bg=cor2, fg=cor3, font=('Ivy 13 bold'))
titulo.place(x=40, y=8)


# botoes segundo frame

#estilo para janela

estilo = ttk.Style(janela)
estilo.theme_use("clam")


img_0 = Image.open('img.png')
img_0 = img_0.resize((50,50))
img_0 = ImageTk.PhotoImage(img_0)

b_peso = Button(segundo_frame,command=lambda:mostrar_menu('massa'), text='Massa', width=129.5, height=50,overrelief='solid', compound=LEFT ,relief='flat', anchor='nw',font=('Ivy 9 bold'), bg=cor3, fg=cor2, image=img_0)
b_peso.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)

#Tempo

img_1 = Image.open('img1.png')
img_1 = img_1.resize((50,50))
img_1 = ImageTk.PhotoImage(img_1)

b_comprimento = Button(segundo_frame,text='Tempo', width=129.49, height=50,overrelief='solid', compound=LEFT ,relief='flat', anchor='nw',font=('Ivy 9 bold'), bg=cor3, fg=cor2, image=img_1)
b_comprimento.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5)


#Comprimento

img_2 = Image.open('img2.png')
img_2 = img_2.resize((50,50))
img_2 = ImageTk.PhotoImage(img_2)

b_comprimento = Button(segundo_frame,command=lambda:mostrar_menu('comprimento'),  text='Comprimento', width=129.49, height=50,overrelief='solid', compound=LEFT ,relief='flat', anchor='nw',font=('Ivy 9 bold'), bg=cor3, fg=cor2, image=img_2)
b_comprimento.grid(row=0, column=2, sticky=NSEW, padx=5, pady=5)

#area

img_3 = Image.open('img3.png')
img_3 = img_3.resize((50,50))
img_3 = ImageTk.PhotoImage(img_3)

b_area = Button(segundo_frame, text='Area',padx=5, width=129.49, height=50,overrelief='solid', compound=LEFT ,relief='flat', anchor='nw',font=('Ivy 9 bold'), bg=cor3, fg=cor2, image=img_3)
b_area.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)


#quantidade

img_4 = Image.open('img4.png')
img_4 = img_4.resize((50,50))
img_4 = ImageTk.PhotoImage(img_4)

b_quantidade = Button(segundo_frame, text='Quantidade', width=129.49, height=50,overrelief='solid', compound=LEFT ,relief='flat', anchor='nw',font=('Ivy 9 bold'), bg=cor3, fg=cor2, image=img_4)
b_quantidade.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5)

#Velocidade

img_5 = Image.open('img5.png')
img_5 = img_5.resize((50,50))
img_5 = ImageTk.PhotoImage(img_5)

b_velocidade = Button(segundo_frame, text='Velocidade', width=129.49, height=50,overrelief='solid', compound=LEFT ,relief='flat', anchor='nw',font=('Ivy 9 bold'), bg=cor3, fg=cor2, image=img_5)
b_velocidade.grid(row=1, column=2, sticky=NSEW, padx=5, pady=5)

#temperatura

img_6 = Image.open('img6.png')
img_6 = img_6.resize((50,50))
img_6 = ImageTk.PhotoImage(img_6)

b_temperatura = Button(segundo_frame, text='Temperatura', width=129.5, height=50,overrelief='solid', compound=LEFT ,relief='flat', anchor='nw',font=('Ivy 9 bold'), bg=cor3, fg=cor2, image=img_6)
b_temperatura.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)

#energia

img_7 = Image.open('img7.png')
img_7 = img_7.resize((50,50))
img_7 = ImageTk.PhotoImage(img_7)

b_energia = Button(segundo_frame, text='Energia', width=129.49, height=50,overrelief='solid', compound=LEFT ,relief='flat', anchor='nw',font=('Ivy 9 bold'), bg=cor3, fg=cor2, image=img_7)
b_energia.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)

#pressão

img_8 = Image.open('img8.png')
img_8 = img_8.resize((50,50))
img_8 = ImageTk.PhotoImage(img_8)

b_energia = Button(segundo_frame, text='Pressão', width=129.49, height=50,overrelief='solid', compound=LEFT ,relief='flat', anchor='nw',font=('Ivy 9 bold'), bg=cor3, fg=cor2, image=img_8)
b_energia.grid(row=2, column=2, sticky=NSEW, padx=5, pady=5)

#Label unidade

label_unidade = Label(terceiro_frame,width=16,height=2 ,text='UNIDADE', bg=cor2, fg=cor1, font=('Ivy 14 bold'), relief='groove', anchor='center')
label_unidade.place(x=0, y=0)

#label_De terceiro_frame

label_de = Label(terceiro_frame,height=1 ,text='De',padx=3, bg=cor2, fg=cor1, font=('Ivy 10 bold'), relief='groove', anchor='center')
label_de.place(x=10, y=70)

#label_para terceiro_fame

label_de = Label(terceiro_frame,height=1 ,text='Para',padx=3, bg=cor2, fg=cor1, font=('Ivy 10 bold'), relief='groove', anchor='center')
label_de.place(x=97, y=70)

#como box terceiro_frame

c_como = ttk.Combobox(terceiro_frame, width=5, justify='center', font=('Ivy 8 bold '))
c_como.place(x=38, y=70)

c_comop = ttk.Combobox(terceiro_frame, width=5, justify='center', font=('Ivy 8 bold '))
c_comop.place(x=138, y=70)




janela.mainloop()
