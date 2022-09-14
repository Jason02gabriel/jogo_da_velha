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
app_x = Label(frame_cima, text="X", font=("Arial", 40), bg=co1, fg=co10)
app_x.place(x=20, y=10)
app_x = Label(frame_cima,text='player1',font=("Arial", 10), bg=co1, fg=co10 )
app_x.place(x=20, y=65)

app_O = Label(frame_cima,text='O',font=("Arial", 40), bg=co1, fg=co10 )
app_O.place(x=175, y=10)
app_O = Label(frame_cima,text='player2',font=("Arial", 10), bg=co1, fg=co10 )
app_O.place(x=175, y=65)





janela.mainloop()