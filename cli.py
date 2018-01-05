from program import computer
from program import cpu
from program import memory
from program import tools
import sys

params = sys.argv

if len(sys.argv) > 1:
	if params[1] == "os" or params[1] == "system":
		print("Sistema Operacional: ", computer.os())
		print("Versão: ", computer.osVersion())
	elif params[1] == "name":
		print("Nome de rede: ", computer.name())
	elif params[1] == "arc":
		print("Arquitetura: ", computer.arc())
	elif params[1] ==  "processor" or params[1] == "-p":
		if len(params) == 4 and params[2] == "percentage" and int(params[3]) >= 1:
			for x in range(int(params[3])):
				consume = cpu.percentage()
				print("Consumindo: ", consume.user + consume.system, "%")
				print("Livre: ", consume.idle, "%")
				print("______________________________")
		elif len(params) == 4 and params[2] == "bench" and int(params[3]) >= 1:
			media = 0
			for x in range(int(params[3])):
				consume = cpu.percentage()
				print("Analisando o uso da CPU...")
				media += consume.user + consume.system
			media = media / int(params[3])
			print("Média de consumo da CPU durante", params[3], "segundos:", media, "%")
		else:
			print("Processador: ", computer.cpu())
			print("Velocidade: ", cpu.freq(), "GHz")
			print("Cores: ", cpu.cores())
			print("Cores Fisicos:", cpu.phyCores())
	elif params[1]  == "memory" or params[1] == "-m":
			if str(params).find("size") > 0:
				print("Tamanho da memória: ", memory.size(), "GB")
			if str(params).find("percentage") > 0:
				print("Consumo atual da memória: ", memory.percentage(), "%")
			if str(params).find("free") > 0:
				print("Memória livre: ", memory.free(), "GB")
			if str(params).find("used") > 0:
				print("Memória usada: ", memory.used(), "GB")
	elif str(params).find("shutdown") > 0:
		print("Desligando ...")
		tools.shutdown()
	elif str(params).find("reboot") > 0:
		print("Reiniciando o computador...")
		tools.reboot()
	else:
		print("Parametro desconhecido")