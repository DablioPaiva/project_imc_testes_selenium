from django.shortcuts import HttpResponse, redirect, render


def index(request):
    return render(request=request, template_name='index.html')

def calcular_imc(request):

    if request.method.POST:
        # Exercicio

        #  Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
        #  mostre seu status, de acordo com a tabela abaixo:
        # - IMC abaixo de 18,5: Abaixo do Peso
        # - Entre 18,5 e 25: Peso Ideal
        # - 25 até 30: Sobrepeso
        # - 30 até 40: Obesidade
        # - Acima de 40: Obesidade Mórbida

        sexo_masculino = request.POST.get('masculino', None)
        sexo_feminino = request.POST.get('feminino', None)

        peso = float(request.POST.get('peso'))
        altura_metro = float(request.POST.get('altura'))
        calculo_imc = peso / (altura_metro ** 2)

        if calculo_imc < 18.5:
            print('Abaixo do Peso.\n'
                  'Seu IMC é de: {:.2f}'.format(calculo_imc))
        elif 18.5 < calculo_imc < 25:
            print('Peso Ideal!\n'
                  'Seu IMC é de: {:.2f}'.format(calculo_imc))
        elif 25 <= calculo_imc < 30:
            print('Sobrepeso.\n'
                  'Seu IMC é de: {:.2f}'.format(calculo_imc))
        elif 30 <= calculo_imc <= 40:
            print('Obesidade.\n'
                  'Seu IMC é de: {:.2f}'.format(calculo_imc))
        elif calculo_imc > 40:
            print('Obesidade Mórbida.\n'
                  'Seu IMC é de: {:.2f}'.format(calculo_imc))

        return render(request,'index.html')