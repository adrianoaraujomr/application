#!/usr/bin/python3

from data_sheet import *
from client  import *
from tkinter import *


#( )Pass workbook use to data_sheet
#(X)Deal with Empty list in the prev next of sessions e clients 
#(X)Improve naviagtion putting buttons to the home window
#( )Try as an exe in windows
#(X)Fix prev button for sessions (Can a client do more than one session on the same date ?)(Was calling next)
#( )Organize the buttons position

######################################################################################################

def clients_window():
	lbl_list = []
	edt_list = []
	ses_list = []

	window = Tk()
	window.title("Red Sam")
	window.geometry('320x200')

#	wb = load_workbook()
	cl = list_clients()

	lll = Label(window,text="              ")
	lll.grid(column=0,row=0)

	for i in range(5):
		try:
			lbl_list.append(Label(window,text=cl[i],font=("Arial Bold",10)))
			lbl_list[i].grid(column=1,row=i)
		except:
			lbl_list.append(Label(window,text=cl[i],font=("Arial Bold",10)))
			lbl_list[i].grid(column=1,row=i)

		edt_list.append(Button(window,text="Edit",command=lambda i=lbl_list[i],w=window: call_edit(i,w)))
		edt_list[i].grid(column=2,row=i)

		ses_list.append(Button(window,text="Sessions",command=lambda i=lbl_list[i],w=window: call_sessions(i,w)))
		ses_list[i].grid(column=3,row=i)
	
	nxt_btn = Button(window,text="Next",command=lambda cl=cl,lbl_list=lbl_list : next_page(cl,lbl_list))
	nxt_btn.grid(column=2,row=5)

	prv_btn = Button(window,text="Prev",command=lambda cl=cl,lbl_list=lbl_list : prev_page(cl,lbl_list))
	prv_btn.grid(column=1,row=5)

	add_btn = Button(window,text="Add Client",command=lambda w=window : call_new_client(w))
	add_btn.grid(column=3,row=5)

	window.mainloop()	

def next_page(cl,lbl_list):
	nro_elements = len(cl)
	if nro_elements > 0:
		last_cli = lbl_list[-1].cget("text")

		if((not last_cli == cl[-1]) and (not last_cli == "")):
			last_index = cl.index(last_cli)
	
			for i in range(5):
				try:
					aux = cl[i + last_index + 1]
					lbl_list[i].configure(text=aux)
				except:
					lbl_list[i].configure(text="")

def prev_page(cl,lbl_list):
	nro_elements = len(cl)
	if nro_elements > 0:
		first_cli = lbl_list[0].cget("text")

		if((not first_cli == cl[0]) and (not first_cli == "")):
			first_index = cl.index(first_cli)

			for i in range(5):
				try:
					aux = cl[first_index - i - 1]
					lbl_list[-(i + 1)].configure(text=aux)
				except:
					lbl_list[- ( i +1)].configure(text="")

def call_new_client(w):
	w.destroy()
	new_client_window()

def call_edit(i,w):
	aux = i.cget("text")
	if not aux == "":
		w.destroy()
		edit_client_window(aux)

def call_sessions(i,w):
	aux = i.cget("text")
	if not aux == "":
		w.destroy()
		sessions_window(aux)

def go_home(w):
	w.destroy()
	clients_window()

######################################################################################################
#Deal with no sessions
def sessions_window(name):
	lbl_list = []
	edt_list = []
	ses_list = []

#	ws = find_client(wb,name)
	ss = list_sessions_by_date(name)

	window = Tk()
	window.title("Stickin to the Floor")
	window.geometry('320x200')

	home_btn = Button(window,text="Home",command=lambda w=window : go_home(w))
	home_btn.grid(column=2,row=6)

	lll = Label(window,text="              ")
	lll.grid(column=0,row=0)

	for i in range(5):
		try :
			lbl_list.append(Label(window,text=ss[i],font=("Arial Bold",10)))
			lbl_list[i].grid(column=1,row=i)
		except:
			lbl_list.append(Label(window,text="",font=("Arial Bold",10)))
			lbl_list[i].grid(column=1,row=i)

		edt_list.append(Button(window,text="Edit",command=lambda w=window,name=name, lbl=lbl_list[i] : call_edit_session(w,name,lbl)))
		edt_list[i].grid(column=2,row=i)

		ses_list.append(Button(window,text="Show info",command=lambda i=lbl_list[i] : call_session(i)))
		ses_list[i].grid(column=3,row=i)

	nxt_btn = Button(window,text="Next",command=lambda cl=ss,lbl_list=lbl_list : next_page(cl,lbl_list))
	nxt_btn.grid(column=2,row=5)

	prv_btn = Button(window,text="Prev",command=lambda cl=ss,lbl_list=lbl_list : prev_page(cl,lbl_list))
	prv_btn.grid(column=1,row=5)

	add_btn = Button(window,text="Add Session",command=lambda w=window,name=name : call_new_session(w,name))
	add_btn.grid(column=3,row=5)

	window.mainloop()	

def call_new_session(w,name):
	w.destroy()
	new_session_window(name)

def call_edit_session(w,name,lbl):
	data = lbl.cget("text")
	if not data == "":
		line = find_session(name,data)
		w.destroy()
		edit_session_window(name,line)

######################################################################################################

def edit_session_window(nome,line):
	window = Tk()
	window.title("In The Fade")
	window.geometry('320x200')

#	wb = load_workbook()
	ws = find_client(nome)

	home_btn = Button(window,text="Home",command=lambda w=window : go_home(w))
	home_btn.grid(column=2,row=6)

	lbl_data = Label(window,text="Data",font=("Arial Bold",10))
	lbl_data.grid(column=0,row=0)
	txt_data = Entry(window,width=15)
	txt_data.insert(0,ws.cell(row=line,column=1).value)
	txt_data.grid(column=1,row=0)

	lbl_rt =   Label(window,text="Regiao Tratada",font=("Arial Bold",10))
	lbl_rt.grid(column=0,row=1)
	txt_rt = Entry(window,width=15)
	txt_rt.insert(0,ws.cell(row=line,column=2).value)
	txt_rt.grid(column=1,row=1)

	lbl_vp =   Label(window,text="Valor Pago",font=("Arial Bold",10))
	lbl_vp.grid(column=0,row=2)
	txt_vp = Entry(window,width=15)
	txt_vp.insert(0,ws.cell(row=line,column=3).value)
	txt_vp.grid(column=1,row=2)

	lbl_fq =   Label(window,text="FQ",font=("Arial Bold",10))
	lbl_fq.grid(column=0,row=3)
	txt_fq = Entry(window,width=15)
	txt_fq.insert(0,ws.cell(row=line,column=4).value)
	txt_fq.grid(column=1,row=3)

	lbl_obs =  Label(window,text="Observacao",font=("Arial Bold",10))
	lbl_obs.grid(column=0,row=4)
	txt_obs = Text(window,width=17,height=4)
	txt_obs.insert(END,ws.cell(row=line,column=5).value)
	txt_obs.grid(column=1,row=4)

	btn_save = Button(window,text="Save",command=lambda w=window,nome=nome,line=line,dt=txt_data,rt=txt_rt,vp=txt_vp,fq=txt_fq,obs=txt_obs : save_session(w,nome,line,dt,rt,vp,fq,obs))
	btn_save.grid(column=1,row=5)

	window.mainloop()

def save_session(w,nome,line,dt,rt,vp,fq,obs):
	edit_session(nome,line,dt.get(),rt.get(),vp.get(),fq.get(),obs.get("1.0",END))
	w.destroy()
	clients_window()


######################################################################################################

def new_session_window(nome):
	window = Tk()
	window.title("Them Bones")
	window.geometry('320x200')

	home_btn = Button(window,text="Home",command=lambda w=window : go_home(w))
	home_btn.grid(column=2,row=6)

	lbl_data = Label(window,text="Data",font=("Arial Bold",10))
	lbl_data.grid(column=0,row=0)
	txt_data = Entry(window,width=15)
	txt_data.grid(column=1,row=0)

	lbl_rt = Label(window,text="Regiao Tratada",font=("Arial Bold",10))
	lbl_rt.grid(column=0,row=1)
	txt_rt = Entry(window,width=15)
	txt_rt.grid(column=1,row=1)

	lbl_vp = Label(window,text="Valor Pago",font=("Arial Bold",10))
	lbl_vp.grid(column=0,row=2)
	txt_vp = Entry(window,width=15)
	txt_vp.grid(column=1,row=2)

	lbl_fq = Label(window,text="FQ",font=("Arial Bold",10))
	lbl_fq.grid(column=0,row=3)
	txt_fq = Entry(window,width=15)
	txt_fq.grid(column=1,row=3)

	lbl_obs = Label(window,text="Observacao",font=("Arial Bold",10))
	lbl_obs.grid(column=0,row=4)
	txt_obs = Text(window,width=17,height=4)
	txt_obs.grid(column=1,row=4)

	btn_save = Button(window,text="Save",command=lambda w=window,nome=nome,dt=txt_data,rt=txt_rt,vp=txt_vp,fq=txt_fq,obs=txt_obs:add_new_session(w,nome,dt,rt,vp,fq,obs))
	btn_save.grid(column=1,row=5)

	window.mainloop()

def add_new_session(w,nome,dt,rt,vp,fq,obs):
	add_session(nome,dt.get(),rt.get(),vp.get(),fq.get(),obs.get("1.0",END))
	w.destroy()
	clients_window()

######################################################################################################
#For now approved
def edit_client_window(name):
	ws = find_client(name)
	ori_name = ws.cell(row=1,column=1).value

	window = Tk()
	window.title("Better off")
	window.geometry('320x200')

	home_btn = Button(window,text="Home",command=lambda w=window : go_home(w))
	home_btn.grid(column=2,row=6)

	lbl_nome = Label(window,text="Nome : ",font=("Arial Bold",10))
	lbl_nome.grid(column=0,row=0)

	txt_nome = Entry(window,width=15)
	txt_nome.insert(0,ori_name)
	txt_nome.grid(column=1,row=0)

	lbl_nome = Label(window,text="Telefone : ",font=("Arial Bold",10))
	lbl_nome.grid(column=0,row=1)

	txt_telf = Entry(window,width=15)
	txt_telf.insert(0,ws.cell(row=1,column=3).value)
	txt_telf.grid(column=1,row=1)

	btn_save = Button(window,text="Save",command=lambda w=window,original_name=ori_name,new_name=txt_nome,new_telf=txt_telf : save_client(w,original_name,new_name,new_telf))
	btn_save.grid(column=1,row=2)

	window.mainloop()

def save_client(w,original_name,new_name,new_telf):
	edit_cliente(original_name,new_name.get(),new_telf.get())
	w.destroy()
	clients_window()

######################################################################################################
#For now approved
def new_client_window():
	window = Tk()
	window.title("Out of the Black")
	window.geometry('320x200')

	home_btn = Button(window,text="Home",command=lambda w=window: go_home(w))
	home_btn.grid(column=2,row=6)

	lbl_nome = Label(window,text="Nome : ",font=("Arial Bold",10))
	lbl_nome.grid(column=0,row=0)

	txt_nome = Entry(window,width=15)
	txt_nome.grid(column=1,row=0)

	lbl_nome = Label(window,text="Telefone : ",font=("Arial Bold",10))
	lbl_nome.grid(column=0,row=1)

	txt_telf = Entry(window,width=15)
	txt_telf.grid(column=1,row=1)

	btn_save = Button(window,text="Save",command=lambda w=window,original_name=void_client,new_name=txt_nome,new_telf=txt_telf : save_client(w,original_name,new_name,new_telf))
	btn_save.grid(column=1,row=2)

	window.mainloop()

######################################################################################################

#def clicked():
#	aux = "Fuck " + txt.get()
#	lbl.configure(text=aux)

#window = Tk()
#window.title("Hello World")
#window.geometry('350x200')

#lbl = Label(window,text="Linux",font=("Arial Bold",50))
#lbl.grid(column=0,row=0)

#btn = Button(window,text="Don't Click",bg="red",fg="black",command=clicked)
#btn.grid(column=1,row=1)

#txt = Entry(window,width=10)
#txt.grid(column=1,row=0)

#window.mainloop()

#def main_window():
#	window = Tk()
#	window.title("Main Window")
#	window.geometry('320x200')

#	btn01 = Button(window,text="Buscar sessoes")
#	btn01.place(relx=0.5,rely=0.5,anchor=CENTER)
#	btn02 = Button(window,text="Adicionar sesao")
#	btn02.place(relx=0.5,rely=0.3,anchor=CENTER)
#	btn03 = Button(window,text="Listar Clientes")
#	btn03.place(relx=0.5,rely=0.7,anchor=CENTER)

#	window.mainloop()

#def busca_sessoes():
#	window = Tk()
#	window.title("Google")
#	window.geometry('320x200')

#	btn02 = Button(window,text="Adicionar sessao")
#	btn02.grid(column=0,row=0)
#	btn03 = Button(window,text="Listar Clientes")
#	btn03.grid(column=2,row=0)

#	txt = Entry(window,width=50)
#	txt.grid(column=1,row=1)

#	btn04 = Button(window,text="Busca")
#	btn04.grid(column=1,row=2)

#	window.mainloop()
