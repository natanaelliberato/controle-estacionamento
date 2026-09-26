def listar_veiculos():
   print("="*35)
   print("VEÍCULOS ESTACIONADOS")
   print("="*35)
   if len(carros) == 0:
      print("Nenhum veículo encontrado")
   else:
      for carro in carros:
         print("Placa", carro["placa"])
         print("Horas", carro["horas"])
         print(f"Valor a pagar R$ {carro['pagar']:.2f}")
def buscar_veiculos():
   print("="*35)
   print("BUSCAR VEÍCULO")
   print("="*35)
   placa_busca = input("Informe a placa que deseja buscar: ").upper()
   encontrado = False
   for carro in carros:
      if carro["placa"] == placa_busca:
         print("Veículo encontrado: ", carro["placa"])
         encontrado = True
   if encontrado == False:
      print("Veículo não encontrado")
def registrar_saida(caixa, saidas):
   print("="*35)
   print("REGISTRAR SAÍDA")
   print("="*35)
   placa_saida = input("Informe a placa do veículo que vai sair: ").upper()
   encontrado = False
   for carro in carros:
      if carro["placa"] == placa_saida:
         print("Veículo encontrado", carro["placa"])
         print(f"Valor a pagar R$  {carro["pagar"]:.2f}")
         carros.remove(carro) 
         caixa += carro["pagar"]
         saidas += 1
         encontrado = True
         print("Saída registrada com sucesso !")
         break
   if encontrado == False:
      print("Veículo não encontrado")
   return caixa, saidas
def mostrar_relatorio(caixa, saidas):
   print("="*35)
   print("RELATÓRIO")
   print("="*35)
   print(f"Total em caixa R$ {caixa:.2f}")
   print("Veículos estacionados", len(carros))
   print("Veículos que saíram", saidas)
def registrar_entrada():
   print("="*35)
   print("REGISTRAR ENTRADA")
   print("="*35)
   placa = input("Informe a placa do veículo ").upper()
   for carro in carros:
      if carro["placa"] == placa:
         print("Veículo já está estacionado")
         return
   try:
      horas = int(input("Informe quantas horas o veículo ficará: "))
   except ValueError:
      print("Digite apenas números: ")
      return
   if horas <= 0:
      print("Número de horas inválido!")
      return
   if horas <= 2:
      pagar = horas * 8
   elif horas <= 5:
      pagar = horas * 6
   else:
      pagar = horas * 5
   carro = {
      "placa": placa,
      "horas": horas,
      "pagar": pagar,
   }
   carros.append(carro)
   print("Veículo registrado com sucesso !")



carros = []
caixa = 0
saidas = 0
while True:

    print(f"\n{'='*10}ESTACIONAMENTO{'='*10}")
    print("1 - Registrar entrada")
    print("2 - Listar veículos")
    print("3 - Buscar veículo")
    print("4 - Registrar saída")
    print("5 - Relatório")
    print("0 - Encerrar")
    try:
         opcao=int(input("Escolha uma opção: "))
    except ValueError:
       print("Digite apenas números")
       continue
    if opcao == 0:
        break
    elif opcao ==1:
       registrar_entrada()
    elif opcao == 2:
       listar_veiculos()
    elif opcao == 3:
       buscar_veiculos()
    elif opcao == 4:
       caixa, saidas = registrar_saida(caixa, saidas)
    elif opcao == 5:
       mostrar_relatorio(caixa, saidas)


   





                
             


          