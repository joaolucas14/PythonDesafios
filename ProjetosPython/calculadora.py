from tkinter import *
from tkinter import ttk

cor1 = "#000000" #preto
cor2 = "#ffffff" #branco
cor3 = "#3f415e" #azul
cor4 = "#ccc5c5" #cinza
cor5 = "#e59719" #laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310") #largura x altura
janela.config(bg=cor1)  #back ground

#criando frame
frame_tela = Frame(janela, width=235, height=50, bg=cor3)#janela(variável), largura, altura
frame_tela.grid(row=0, column=0)#(Fileira, coluna)
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#variavél todos valores
todos_valores=""

# criando função
def entrar_valores(num):
    global todos_valores

    todos_valores = todos_valores + str(num)

    #passando o valor para o leitor
    valor_texto.set(todos_valores)

#função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#função limpartela
def limpartela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

#criando o leitor
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
#padx = padding(margem) anchor="e"(ancorar no 'east' direita o label inteiro) justify =RIGHT(junta as letras a direita)
app_label.place(x=0,y=0)
#criando botões
b1 = Button(frame_corpo,command= limpartela, text="C", width=11, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)#indica aonde vai ficar, texto que aparece no botão
b1.place(x=0, y=0)#x = horizontal y = vertical
b2 = Button(frame_corpo, command= lambda: entrar_valores('%'),text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)#fonte(Estilo, tamanho, negrito) relief=Raised(Determina qual será o estilo da borda de um widget) overrelief=RIDGE(Efeito quando passa o mouse por cima)
b2.place(x=118, y=0)
b3 = Button(frame_corpo, command= lambda: entrar_valores('/'),text="/", width=5, height=2, bg=cor5, fg=cor2,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)#fg = cor da fonte
b3.place(x=177, y=0)

b4 = Button(frame_corpo, command= lambda: entrar_valores('7'),text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(frame_corpo, command= lambda: entrar_valores('8'),text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)
b6 = Button(frame_corpo, command= lambda: entrar_valores('9'),text="9", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=52)
b7 = Button(frame_corpo, command= lambda: entrar_valores('*'),text="*", width=5, height=2, bg=cor5, fg=cor2,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=177, y=52)

b8 = Button(frame_corpo, command= lambda: entrar_valores('4'),text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9 = Button(frame_corpo, command= lambda: entrar_valores('5'),text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=104)
b10 = Button(frame_corpo, command= lambda: entrar_valores('6'),text="6", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=104)
b11 = Button(frame_corpo, command= lambda: entrar_valores('-'),text="-", width=5, height=2, bg=cor5, fg=cor2,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=177, y=104)

b12 = Button(frame_corpo, command= lambda: entrar_valores('1'),text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13 = Button(frame_corpo, command= lambda: entrar_valores('2'),text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=156)
b14 = Button(frame_corpo, command= lambda: entrar_valores('3'),text="3", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=156)
b15 = Button(frame_corpo, command= lambda: entrar_valores('+'),text="+", width=5, height=2, bg=cor5, fg=cor2,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=177, y=156)

b16 = Button(frame_corpo, command= lambda: entrar_valores('0'),text="0", width=11, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)
b17 = Button(frame_corpo, command= lambda: entrar_valores('.'),text=".", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=208)
b18 = Button(frame_corpo, command= calcular,text="=", width=5, height=2, bg=cor5, fg=cor2,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=177, y=208)

janela.mainloop()