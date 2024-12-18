import time

places = ['la forêt', 'les mines', 'le château']

def intro(player):
    print(f"{player.nom} et ses amis s'endormaient paisiblement autour de leur précieux oeuf...")
    time.sleep(2.5)
    print(f"Soudain une horde de Picoos débarque et saccage tout. Alors que {player.nom} dort encore paisiblement, ses amis sont enlevés et l'oeuf est subtilisé...")
    time.sleep(3)
    print(f'{player.nom} se réveille seul...')
    time.sleep(1.5)
    print("Il se rend compte que l'oeuf et ses amis ont disparu. Mais il reconnaît les traces laissés par les vils Picoo...")
    time.sleep(4)
    print('Il décide de suivre ces traces et se met alors en quête du précieux oeuf.\n')
    time.sleep(2)

def get_mode(stage):
    mode = 0
    if stage <= 3:
        mode = 0
    elif stage <= 8:
        mode = 1
    elif stage == 9:
        mode = 2
    return mode

def get_place(stage):
    place = places[get_mode(stage)]
    return place

def introduce_level(stage):
    print(f'Vous entrez dans {get_place(stage)}.')
    time.sleep(3)

def final_battle():
    print('Vous entrez finalement dans la demeure de King Picoo.')
    time.sleep(3)
    print('Il vous attendait...')
    time.sleep(2)
    print('Vous engagez le combat sans plus attendre.')
