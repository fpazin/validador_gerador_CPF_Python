
V = True
while V == True:
    try:
        CPF = input("Digite um CPF: ")
        Lista9 = []
        Contador = 0
        for i in CPF: 					#Adiciona os primeiros 9 digitos em uma lista
            if Contador <= 8:
                Lista9.append(int(i))
            Contador += 1

        Soma = 0
        Multplicador = 1 
        for i in Lista9: #1º Digito
            Soma = Soma + (i*Multplicador)
            Multplicador += 1

        M = Soma % 11 					#Obtendo o primeiro digito e adicionando na lista
        if M == 10:
            M = 0
        Lista9.append(M)

        Soma1 = 0
        Multplicador = 0
        for i in Lista9: 				#2º Digito
            Soma1 = Soma1 + (i*Multplicador)
            Multplicador += 1

        M = Soma1 % 11
        if M == 10: 					#Obtendo o segundo digito e adicionando na Lista 
            M = 0
        Lista9.append(M)

        vCPF = "" 
        for i in Lista9: 				#Transformando a lista em uma String para comparacao ao CPF Digitado
            vCPF += str(i)

        if CPF  == vCPF: 				#Validacao do CPF
            print("É um CPF valido")
        else:
            print("Não é um CPF válido!")
        Q = input("Digite sair, para encerrar. Enter para continuar validando CPF's: ").lower()
        if Q == "sair":
            V = False
            print("Programa encerrado!")
    except:
        print("Parece que você não digitou numero de CPF. Tente novamente...")
        