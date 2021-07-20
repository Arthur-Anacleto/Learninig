altura = float(input('Digite a altura da parede a ser pintada. '))
largura = float(input('Digite a largura da parede a ser pintada'))
print('Sendo a área da parede {:.2f}m², você vai precisar de {:.2f} litros de tinta.'
      .format((altura*largura), (altura * largura) / 2))
