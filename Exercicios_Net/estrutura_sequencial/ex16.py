# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
# cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input("Qual o tamanho da área a ser pintada em m²?"))
litros_necessarios = (area / 3)
qnt_latas = litros_necessarios / 18
preco_total = qnt_latas.__ceil__() * 80
print(f"Você irá precisar de {qnt_latas.__ceil__()} latas e irá custar R${preco_total:.2f}")
