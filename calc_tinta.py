l = float(input('Digite a largura de sua parede: '))
a = float(input('Digite a altura de sua parede: '))
area = l * a 
tinta = area / 2

print('Sua parede tem {}x{} e sua área é de {}m².'.format(l, a, area))

print('Para pintar sua parede, você precisa de {}l de tinta.' .format(tinta))