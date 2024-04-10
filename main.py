import PySimpleGUI as sg


def verificar_emprestimo(values):
  nome_limpo = values['nome_limpo']
  carteira_assinada = values['carteira_assinada']
  casa_propria = values['casa_propria']

  if nome_limpo and carteira_assinada and casa_propria:
    sg.popup("Qualificação para Empréstimo",
             "Parabéns! Você está qualificado para um empréstimo.")
    # Adicione aqui a lógica para calcular o valor do empréstimo ou outras ações
  else:
    sg.popup("Qualificação para Empréstimo",
             "Desculpe, você não está qualificado para um empréstimo.")


# Layout da janela
layout = [[sg.Text("Seu nome está limpo?"),
           sg.Checkbox("", key='nome_limpo')],
          [
              sg.Text("Você possui carteira assinada?"),
              sg.Checkbox("", key='carteira_assinada')
          ],
          [
              sg.Text("Você possui casa própria?"),
              sg.Checkbox("", key='casa_propria')
          ], [sg.Button("Verificar")]]

# Criação da janela
window = sg.Window("Verificação de Empréstimo", layout)

# Loop de eventos
while True:
  event, values = window.read()
  if event == sg.WINDOW_CLOSED:
    break
  elif event == "Verificar":
    verificar_emprestimo(values)

# Fechamento da janela
window.close()
