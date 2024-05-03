# -*- coding: utf-8 -*-
"""listas.D2.victor.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ib9PrCCCh1rbUSRK-s5tpT14BPf7_yfW

Aula de Listas e operações aritméticas com Python ⏰
"""

#len permite saber o cumprimento de uma lista

jogo=["online", "nivel", 5, "genero", 100.00, "plataforma", "developer", "nome"]
len(jogo)

jogo1=["online", "rankeado", 1, "ps", 0.00, "pc", "riot", "valorant"]
jogo2=["online", "rankeado", 1, "mobfa", 0.00, "pc", "riot", "league of legends"]
jogo3=["sigle_multi_player", "sandbox", 10, "sandbox", 160.00, "pc_console", "mojang", "minecraft"]
jogo1+jogo2+jogo3

#list.append(x)
#Adiciona um item ao fim da lista. Equivalente a a[len(a):] = [x].
jogo1=["online", "rankeado", 1, "fps", 0.00, "pc", "riot", "valorant"]
jogo1[len(jogo1):] = ["victor"]
print(jogo1)

#list.remove(x)
#Remove o primeiro item encontrado na lista cujo valor é igual a x.
#Se não existir valor igual, uma exceção ValueError é levantada.
jogo2=["online", "rankeado", 1, "moba", 0.00, "pc", "riot", "league of legends"]
jogo2.remove("riot")
print(jogo2)

#list.pop([i])
#Remove o item na posição fornecida na lista e retorna. Se nenhum índice for especificado, a.pop() remove e retorna o último item da lista.
#Levanta um IndexError se a lista estiver vazia ou o índice estiver fora do intervalo da lista.
jogo3=["sigle_multi_player", "sandbox", 10, "sandbox", 160.00, "pc_console", "mojang", "minecraft"]
jogo3.pop(0)

#list.clear()
#Remove todos os itens de uma lista. Equivalente a del a[:].
jogo3=["sigle_multi_player", "sandbox", 10, "sandbox", 160.00, "pc_console", "mojang", "minecraft"]
jogo3.clear()
print(jogo3)