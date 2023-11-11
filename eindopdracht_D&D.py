#append gebruiken voor queue


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
#print(type(kamers["11"][0]))

pending = [1]
queue = [1]

def best_path():
    control = True
#    while 0 == 0:
    #if 12 in queue:
        #print(queue)
    #else: 
    while control == True:
       #for buur in queue:   #bij een for loop gebruiken gaat elke keer naar de volgende plaats in de queue, en als je elke keer 1 waarde toevoegt blijft er dus telkens hetzelfde uitkomen.
        for element in kamers[queue[0]]:
        #if element in queue:
        #   print("element is al in de queue")
        #else:
            queue.insert(0, element)
        #queue.append(kamers[buur[]])
        # for andere_buur in queue:
        #     if andere_buur not in queue:
        #         queue.append(andere_buur)
        print(queue)
        pending.insert(0, queue[0])
        print("Pending list:" , pending)
        
        #teruglopen van de pending list totdat een andere buur gevonden die nog niet bekeken is
        # if queue[0] == 12:
        #     while queue[0] == pending[0]:
        #         queue.pop(0)
        #         pending.pop(0)
        
        
        #eerste keer bij het einde gekomen hier
        if pending[0] == 12:
            control = False
            while queue[0] == pending[0]:
                queue.pop(0)
                pending.pop(0)
                print("Queue:", queue)
                print("Pending", pending)
            #control = True
            
         
    
best_path()


#dit is nog steeds breadth first search, alle nieuwe elementen moeten als eerst geplaatst worden zodat het depth first search wordt