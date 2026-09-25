def listar_veiculos():
   if len(carros) == 0:
      print("Nenhum veiculo encontrado ")
   else:
      for carro in carros:
         print("placa", carro["placa"])
         print("horas", carro["horas"])
         print(f"pagar R$ {carro['pagar']:.2f}")
def buscar_veiculos():
   placa_busca = input("informe a placa que deseja buscar ").upper()
   encontrado = False
   for carro in carros:
      if carro["placa"] == placa_busca:
         print("Veiculo encontrado: ", carro["placa"])
         encontrado = True
   if encontrado == False:
      print("Veiculo não encontrado ")
def registrar_saida(caixa, saidas):
   placa_saida = input("Informe a placa que vai sair ").upper()
   encontrado = False
   for carro in carros:
      if carro["placa"] == placa_saida:
         print("Veiculo encontrado", carro["placa"])
         print(f"Valor a pagar R$  {carro["pagar"]:.2f}")
         carros.remove(carro) 
         caixa += carro["pagar"]
         saidas += 1
         encontrado = True
         print("Saida registrada com sucesso !")
         break
   if encontrado == False:
      print("Veiculo não encontrado ")
   return caixa, saidas
def mostrar_relatorio(caixa, saidas):
   print(f"Total em caixa R$ {caixa:.2f}")
   print("Veiculos estacionados", len(carros))
   print("Veiculos que sairam", saidas)
def registrar_entrada():
   placa = input("Informe a placa do veiculo ").upper()
   for carro in carros:
      if carro["placa"] == placa:
         print("Veiculo ja está estacionado ")
         return
   try:
      horas = int(input("Informe Quantas horas irá ficar "))
   except ValueError:
      print("Digite apenas números ")
      return
   if horas <= 0:
      print("Numero de horas invalido ")
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
   print("Veiculo registrado com sucesso ! ")



carros = []
caixa = 0
saidas = 0
while True:

    print(f"{'='*10}ESTACIONAMENTO{'='*10}")
    print("1 - Registrar entrada")
    print("2 - Listar veículos ")
    print("3 - Buscar veículo ")
    print("4 - Registar saida")
    print("5 - Relatório")
    print("0 - Encerrar")
    try:
         opcao=int(input("Escolha uma opção "))
    except ValueError:
       print("Digite apenas números ")
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

   





                
             


          