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


jogador_1 = 'X'
jogador_2 = 'O'

score_1= 0
score_2= 0

tabela = [[1,2,3],[4,5,6],[7,8,9]]

jogando = 'X'
contador = 0
jogar = ''

def inicia_jogo():

    #controlar o jogo
    def controlar_jogo(i):
        global jogando
        global contador
        global jogar

        #comparando o valor do botao com o valor da tabela
        if i == '1':
            #verificar se o botao ja foi clicado
            if botao1['text'] == '':
                #verificar quem esta jogando
                if jogando == 'X':
                    cor = co6
                if jogando == 'O':
                    cor = co7
                #alterar o texto do botao
                botao1['fg'] = cor
                botao1['text'] = jogando
                tabela[0][0] = jogando
                #verificar quem esta jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'player1'
                else:
                    jogando = 'X'
                    jogar = 'player2'
                #contar quantas jogadas foram feitas
                contador += 1
                #se o contador for maior ou igual a 5, verificar se alguem ganhou
                if contador >= 5:
                    #linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!="":
                        verifica_vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!="":
                        verifica_vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!="":
                        verifica_vencedor(jogando)
                    #colunas
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0]!="":
                        verifica_vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!="":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!="":
                        verifica_vencedor(jogando)
                    #diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2]!="":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!="":
                        verifica_vencedor(jogando)

                    #se o contador for maior ou igual a 9, significa que deu velha
                if contador >= 9:
                    verifica_vencedor('velha')
        if i == '2':
            # verificar se o botao ja foi clicado
            if botao2['text'] == '':
                # verificar quem esta jogando
                if jogando == 'X':
                    cor = co6
                if jogando == 'O':
                    cor = co7
                # alterar o texto do botao
                botao2['fg'] = cor
                botao2['text'] = jogando
                tabela[0][1] = jogando
                # verificar quem esta jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'player1'
                else:
                    jogando = 'X'
                    jogar = 'player2'
                # contar quantas jogadas foram feitas
                contador += 1
                # se o contador for maior ou igual a 5, verificar se alguem ganhou
                if contador >= 5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # colunas
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        verifica_vencedor(jogando)

                # se o contador for maior ou igual a 9, significa que deu velha
                if contador >= 9:
                    verifica_vencedor('velha')
        if i == '3':
            # verificar se o botao ja foi clicado
            if botao3['text'] == '':
                # verificar quem esta jogando
                if jogando == 'X':
                    cor = co6
                if jogando == 'O':
                    cor = co7
                # alterar o texto do botao
                botao3['fg'] = cor
                botao3['text'] = jogando
                tabela[0][2] = jogando
                # verificar quem esta jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'player1'
                else:
                    jogando = 'X'
                    jogar = 'player2'
                # contar quantas jogadas foram feitas
                contador += 1
                # se o contador for maior ou igual a 5, verificar se alguem ganhou
                if contador >= 5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # colunas
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        verifica_vencedor(jogando)

                    # se o contador for maior ou igual a 9, significa que deu velha
                if contador >= 9:
                    verifica_vencedor('velha')
        if i == '4':
            # verificar se o botao ja foi clicado
            if botao4['text'] == '':
                # verificar quem esta jogando
                if jogando == 'X':
                    cor = co6
                if jogando == 'O':
                    cor = co7
                # alterar o texto do botao
                botao4['fg'] = cor
                botao4['text'] = jogando
                tabela[1][0] = jogando
                # verificar quem esta jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'player1'
                else:
                    jogando = 'X'
                    jogar = 'player2'
                # contar quantas jogadas foram feitas
                contador += 1
                # se o contador for maior ou igual a 5, verificar se alguem ganhou
                if contador >= 5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # colunas
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        verifica_vencedor(jogando)

                    # se o contador for maior ou igual a 9, significa que deu velha
                if contador >= 9:
                    verifica_vencedor('velha')
        if i == '5':
            # verificar se o botao ja foi clicado
            if botao5['text'] == '':
                # verificar quem esta jogando
                if jogando == 'X':
                    cor = co6
                if jogando == 'O':
                    cor = co7
                # alterar o texto do botao
                botao5['fg'] = cor
                botao5['text'] = jogando
                tabela[1][1] = jogando
                # verificar quem esta jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'player1'
                else:
                    jogando = 'X'
                    jogar = 'player2'
                # contar quantas jogadas foram feitas
                contador += 1
                # se o contador for maior ou igual a 5, verificar se alguem ganhou
                if contador >= 5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # colunas
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        verifica_vencedor(jogando)

                    # se o contador for maior ou igual a 9, significa que deu velha
                if contador >= 9:
                    verifica_vencedor('velha')
        if i == '6':
            # verificar se o botao ja foi clicado
            if botao6['text'] == '':
                # verificar quem esta jogando
                if jogando == 'X':
                    cor = co6
                if jogando == 'O':
                    cor = co7
                # alterar o texto do botao
                botao6['fg'] = cor
                botao6['text'] = jogando
                tabela[1][2] = jogando
                # verificar quem esta jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'player1'
                else:
                    jogando = 'X'
                    jogar = 'player2'
                # contar quantas jogadas foram feitas
                contador += 1
                # se o contador for maior ou igual a 5, verificar se alguem ganhou
                if contador >= 5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # colunas
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        verifica_vencedor(jogando)

                    # se o contador for maior ou igual a 9, significa que deu velha
                    if contador >= 9:
                        verifica_vencedor('velha')
        if i == '7':
            # verificar se o botao ja foi clicado
            if botao7['text'] == '':
                # verificar quem esta jogando
                if jogando == 'X':
                    cor = co6
                if jogando == 'O':
                    cor = co7
                # alterar o texto do botao
                botao7['fg'] = cor
                botao7['text'] = jogando
                tabela[2][0] = jogando
                # verificar quem esta jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'player1'
                else:
                    jogando = 'X'
                    jogar = 'player2'
                # contar quantas jogadas foram feitas
                contador += 1
                # se o contador for maior ou igual a 5, verificar se alguem ganhou
                if contador >= 5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # colunas
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        verifica_vencedor(jogando)

                    # se o contador for maior ou igual a 9, significa que deu velha
                if contador >= 9:
                    verifica_vencedor('velha')
        if i == '8':
            # verificar se o botao ja foi clicado
            if botao8['text'] == '':
                # verificar quem esta jogando
                if jogando == 'X':
                    cor = co6
                if jogando == 'O':
                    cor = co7
                # alterar o texto do botao
                botao8['fg'] = cor
                botao8['text'] = jogando
                tabela[2][1] = jogando
                # verificar quem esta jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'player1'
                else:
                    jogando = 'X'
                    jogar = 'player2'
                # contar quantas jogadas foram feitas
                contador += 1
                # se o contador for maior ou igual a 5, verificar se alguem ganhou
                if contador >= 5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # colunas
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        verifica_vencedor(jogando)

                    # se o contador for maior ou igual a 9, significa que deu velha
                if contador >= 9:
                    verifica_vencedor('velha')
        if i == '9':
            # verificar se o botao ja foi clicado
            if botao9['text'] == '':
                # verificar quem esta jogando
                if jogando == 'X':
                    cor = co6
                if jogando == 'O':
                    cor = co7
                # alterar o texto do botao
                botao9['fg'] = cor
                botao9['text'] = jogando
                tabela[2][2] = jogando
                # verificar quem esta jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'player1'
                else:
                    jogando = 'X'
                    jogar = 'player2'
                # contar quantas jogadas foram feitas
                contador += 1
                # se o contador for maior ou igual a 5, verificar se alguem ganhou
                if contador >= 5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # colunas
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    # diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        verifica_vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        verifica_vencedor(jogando)

                    # se o contador for maior ou igual a 9, significa que deu velha
                if contador >= 9:
                    verifica_vencedor('velha')

    #verificar quem ganhou
    def verifica_vencedor(i):
        pass


    #terminar o jogo
    def finaliza_jogo():
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
    botao1 = Button(frame_baixo, text="",command=lambda: controlar_jogo('1'),width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao1.place(x=20, y=15)
    botao2 = Button(frame_baixo, text="",command=lambda: controlar_jogo('2'),width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao2.place(x=86, y=15)
    botao3 = Button(frame_baixo, text="",command=lambda: controlar_jogo('3'),width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao3.place(x=152, y=15)
    # botões da segunda linha
    botao4 = Button(frame_baixo, text="",command=lambda: controlar_jogo('4'),width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao4.place(x=20, y=75)
    botao5 = Button(frame_baixo, text="",command=lambda: controlar_jogo('5'),width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao5.place(x=86, y=75)
    botao6 = Button(frame_baixo, text="",command=lambda: controlar_jogo('6'),width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao6.place(x=152, y=75)
    # botões da 3 linha
    botao7 = Button(frame_baixo, text="",command=lambda: controlar_jogo('7'),width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao7.place(x=20, y=135)
    botao8 = Button(frame_baixo, text="",command=lambda: controlar_jogo('8'),width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao8.place(x=86, y=135)
    botao9 = Button(frame_baixo, text="",command=lambda: controlar_jogo('9'),width=3, font=("Ivy 20 bold"), overrelief=RIDGE, bg=fundo, fg=co0)
    botao9.place(x=152, y=135)
#botão inicia jogo
botao_inicia = Button(frame_baixo,command=inicia_jogo,text="Iniciar", width=10 ,font=("Ivy 10 bold"),overrelief=RIDGE, bg=fundo, fg=co0)
botao_inicia.place(x=75, y=210)








janela.mainloop()