# pseudocode

# dictionary maken met elke kamer en de buren, en of de kamer een monster/loot heeft
# eerst buren checken en eerste buur checken
# huidige punt op pending zetten
# doorgaan naar buur
# +1 op teller voor loot en monster verslagen en status van loot veranderen
# het hele riedeltje opnieuw

# als je bij een punt komt dat op pending staat, ga je naar een andere buur
# als er geen buren zijn, maar het is niet het einde, dan route niet opslaan en neerzetten als done
# als je een route helemaal gelopen hebt, teruggaan naar de laatste die wel een buur had
# als er een onbekende buur is en een pending buur, ga je voor de onbekende



#betere pseudocode?

# while not at the end:
#     ga elke keer een buur verder
# if wel bij het eind:
#     teruglopen tot de vorige tegel met een buur
# Met een pending list en queue bijhouden welk pad je nu loopt, en welke nog moeten.
# afstanden bijhouden dmv de lists en de langste afstand is de beste route





# kamers = { #kamer : [buren]
#     1 : [2, 5],
#     2 : [3],
#     3 : [4],
#     4 : [3, 1],
#     5 : [6, 7],
#     6 : [8],
#     7 : [9],
#     8 : [12],
#     9 : [7, 10, 11],
#     10 : [7, 8],
#     11 : [],
#     12 : []
# }

kamers = { #kamer : [buren]
    1 : [2, 5],
    2 : [3],
    3 : [4],
    4 : [6],
    5 : [6],
    6 : [7, 8],
    7 : [11],
    8 : [9],
    9 : [10],
    10 : [11],
    11 : [12],
    12 : []
}

monsterloot = { #kamer : [monster, loot]
    1 : [False, False],
    2 : [True, True],
    3 : [True, True],
    4 : [True, True],
    5 : [True, True],
    6 : [False, False],
    7 : [True, True],
    8 : [True, True],
    9 : [True, True],
    10 : [True, True],
    11 : [True, True],
    12 : [False, False]
}

pending = [1]
queue = [1]

def best_path():
    control = True
    while control == True:
        for element in kamers[queue[0]]:
            queue.insert(0, element)
        print(queue)
        pending.insert(0, queue[0])
        print("Pending list:" , pending)
             
        #eerste keer bij het einde gekomen hier
        if pending[0] == 12:
            control = False
            while queue[0] == pending[0]:
                queue.pop(0)
                pending.pop(0)
                print("Queue:", queue)
                print("Pending", pending)
            
         
    
best_path()

