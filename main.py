from tkinter import *
from tkinter import ttk

# cores ---------------------------------------
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

#janela principal

janela = Tk()
janela.title("")
janela.geometry('260x370')
janela.configure(bg=fundo)



#dividir a tela em 2 frames
frame_cima = Frame(janela, width=240, height=100, bg=co1 , relief="raised")
frame_cima.pack(side=TOP)

frame_baixo = Frame(janela , width=240, height=300 , bg=fundo , relief="flat")
frame_baixo.pack(side=BOTTOM)

#configurar o frame de cima
app_x = Label(frame_cima, text="X", font=("Arial", 40), bg=co1, fg=co6)
app_x.place(x=20, y=10)
app_x = Label(frame_cima,text='player1',font=("Arial", 10), bg=co1, fg=co10 )
app_x.place(x=20, y=65)

app_separador = Label(frame_cima, text=":", font=("Arial", 40), bg=co1, fg=co10)
app_separador.place(x=110   , y=10)


app_O = Label(frame_cima,text='O',font=("Arial", 40), bg=co1, fg=co7 )
app_O.place(x=175, y=10)
app_O = Label(frame_cima,text='player2',font=("Arial", 10), bg=co1, fg=co10 )
app_O.place(x=175, y=65)

pontuacao_x = Label(frame_cima,text='0',font=("Arial", 30), bg=co1, fg=co10 )
pontuacao_x.place(x=80, y=20)
pontuacao_o = Label(frame_cima,text='0',font=("Arial", 30), bg=co1, fg=co10 )
pontuacao_o.place(x=135, y=20)

#configurar o frame de baixo



def inicia_jogo():
    pass
    # linhas verticais
    app_linha1 = Label(frame_baixo, text="", height=23, pady=5, relief='flat', font=("Ivy 5 bold"), bg=co0, fg=co0)
    app_linha1.place(x=80, y=15)
    app_linha2 = Label(frame_baixo, text="", height=23, pady=5, relief='flat', font=("Ivy 5 bold"), bg=co0, fg=co0)
    app_linha2.place(x=147, y=15)

    # linhas horizontais
    app_linha3 = Label(frame_baixo, text="", width=61, padx=2, relief='flat', font=("Ivy 4 bold"), bg=co0, fg=co0)
    app_linha3.place(x=20, y=63)
    app_linha4 = Label(frame_baixo, text="", width=61, padx=2, relief='flat', font=("Ivy 4 bold"), bg=co0, fg=co0)
    app_linha4.place(x=20, y=123)

    # botoões da primeira linha
    botao1 = Button(frame_baixo, text="", width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao1.place(x=20, y=15)
    botao2 = Button(frame_baixo, text="", width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao2.place(x=86, y=15)
    botao3 = Button(frame_baixo, text="", width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao3.place(x=152, y=15)
    # botões da segunda linha
    botao4 = Button(frame_baixo, text="", width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao4.place(x=20, y=75)
    bota5 = Button(frame_baixo, text="", width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    bota5.place(x=86, y=75)
    botao6 = Button(frame_baixo, text="", width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao6.place(x=152, y=75)
    # botões da 3 linha
    botao7 = Button(frame_baixo, text="", width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao7.place(x=20, y=135)
    botao8 = Button(frame_baixo, text="", width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao8.place(x=86, y=135)
    botao9 = Button(frame_baixo, text="", width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao9.place(x=152, y=135)



    def verifica_vencedor():
        pass

    def finaliza_jogo():
        pass

#botão inicia jogo
botao_inicia = Button(frame_baixo,command=inicia_jogo,text="Iniciar", width=10 ,font=("Ivy 10 bold"),overrelief=RIDGE, bg=fundo, fg=co0)
botao_inicia.place(x=75, y=210)








janela.mainloop()