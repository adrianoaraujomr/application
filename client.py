#!/usr/bin/python

class Sessao:
#Atributos :
#	data  : data da sessao
#	rt    : regiao tratada
#	vp    : valor pago
#	fq    :
#       obs   : observacao
#	saved : booleano se a sessao ja esta na planinlha
	def __init__(self,data,rt,vp,fq,obs,saved):
		self.data = data
		self.rt = rt
		self.vp = vp
		self.fq = fq
		self.obs = obs
		self.saved = saved


class Cliente:
#Atributos :
#	nome
#	telefone
#	sessoes : lista de sessoes realizadas
	def __init__(self,nome,telefone,sessoes):
		self.nome = nome
		self.telefone = telefone
#		if sessoes is None:
#			self.sessoes
#		else:
		self.sessoes = sessoes

	def add_sessao(self,sessao):
		self.sessoes.append(sessao)

	def rm_sessao(self,sessao):
		self.sessoes.remove(sessao)
