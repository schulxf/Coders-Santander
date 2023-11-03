print('Olá, sejá bem vindo à sua mais nova calculadora de IMC masculino.')
print('Você deve logar para continuar!')
login = input('Digite seu login: ')
senha = input('Digite sua senha: ')

login_permitido = 'teste'
senha_permitida = 'teste'

while login != login_permitido and senha != senha_permitida:
    print('Você digitou alguma coisa errada...')

else:
    print('Você está conectado!')
    
    
while True:
    nome = input('Qual o seu nome? ')
    peso = int(input('Qual o seu peso? '))
    altura = float(input('Qual a sua altura? '))
    imc = peso / (altura * altura)
    imc_f = (f'{imc:.2f}')


    muito_abaixo = imc <= 16.9
    abaixo_peso = imc >= 17 and imc <= 18.4
    peso_normal = imc >= 18.5 and imc <= 24.9
    acima_peso = imc >= 25 and imc <= 29.9
    obes_grau1 = imc >= 30 and imc <= 34.9
    obes_grau2 = imc >= 35 and imc <= 39.99
    obes_grau3 = imc >= 40

    if muito_abaixo:
        print(f'Seu IMC é', imc_f, 'e você está muito abaixo do peso!')
    elif abaixo_peso:
        print(f'Seu IMC é', imc_f, 'e você está abaixo do peso!')
    elif peso_normal:
        print(f'Seu IMC é', imc_f, 'e você está no peso normal!')
    elif acima_peso:
        print(f'Seu IMC é', imc_f, 'e você está acima do peso!')
    elif obes_grau1:
        print(f'Seu IMC é', imc_f, 'e você está com obesidade de grau 1!')
    elif obes_grau2:
        print(f'Seu IMC é', imc_f, 'e você está com obesidade de grau 2!')
    else:
        print(f'Seu IMC é', imc_f, ' e você está OBESO NO GRAU 3!' )

 

    sair = input('Você deseja finalizar? Para sair digite "sim", caso contrário digite não! ;) ').lower().startswith('s')

    if sair is True:
        print('Você saiu do programa.')
        break
    else:
        print('Muito bem.')