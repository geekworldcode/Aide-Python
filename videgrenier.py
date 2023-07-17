import random
from tkinter import *

jeux_video = {
    'NES': [
        {'nom': 'Super Mario Bros.', 'prix': 20.00, 'image': 'super_mario_bros.png'},
        {'nom': 'The Legend of Zelda', 'prix': 30.00, 'image': 'the_legend_of_zelda.png'},
        {'nom': 'Metroid', 'prix': 25.00, 'image': 'metroid.png'},
        {'nom': 'Mega Man 2', 'prix': 40.00, 'image': 'mega_man_2.png'},
        {'nom': 'Castlevania', 'prix': 35.00, 'image': 'castlevania.png'},
        {'nom': 'Final Fantasy', 'prix': 50.00, 'image': 'final_fantasy.png'},
        {'nom': 'Punch-Out!!', 'prix': 30.00, 'image': 'punch_out.png'},
        {'nom': 'Contra', 'prix': 45.00, 'image': 'contra.png'},
        {'nom': 'Excitebike', 'prix': 25.00, 'image': 'excitebike.png'},
        {'nom': 'Super Mario Bros. 3', 'prix': 35.00, 'image': 'super_mario_bros_3.png'}
    ],
    'SNES': [
        {'nom': 'Super Mario World', 'prix': 30.00, 'image': 'super_mario_world.png'},
        {'nom': 'The Legend of Zelda: A Link to the Past', 'prix': 40.00, 'image': 'zelda_a_link_to_the_past.png'},
        {'nom': 'Super Metroid', 'prix': 50.00, 'image': 'super_metroid.png'},
        {'nom': 'Chrono Trigger', 'prix': 60.00, 'image': 'chrono_trigger.png'},
        {'nom': 'Super Mario Kart', 'prix': 30.00, 'image': 'super_mario_kart.png'},
        {'nom': 'Donkey Kong Country', 'prix': 35.00, 'image': 'donkey_kong_country.png'},
        {'nom': 'Final Fantasy VI', 'prix': 70.00, 'image': 'final_fantasy_VI.png'},
        {'nom': 'Super Mario RPG', 'prix': 50.00, 'image': 'super_mario_rpg.png'},
        {'nom': 'Street Fighter II', 'prix': 30.00, 'image': 'street_fighter_II.png'},
        {'nom': 'Mega Man X', 'prix': 40.00, 'image': 'mega_man_X.png'}
    ],
    'N64': [
        {'nom': 'Super Mario 64', 'prix': 50.00, 'image': 'super_mario_64.png'},
        {'nom': 'The Legend of Zelda: Ocarina of Time', 'prix': 60.00, 'image': 'zelda_ocarina_of_time.png'},
        {'nom': 'GoldenEye 007', 'prix': 40.00, 'image': 'goldeneye_007.png'},
        {'nom': 'Mario Kart 64', 'prix': 35.00, 'image': 'mario_kart_64.png'},
        {'nom': 'Super Smash Bros.', 'prix': 50.00, 'image': 'super_smash_bros.png'},
        {'nom': 'Banjo-Kazooie', 'prix': 45.00, 'image': 'banjo_kazooie.png'},
        {'nom': 'Perfect Dark', 'prix': 40.00, 'image': 'perfect_dark.png'},
        {'nom': 'Star Fox 64', 'prix': 30.00, 'image': 'star_fox_64.png'},
        {'nom': 'Mario Party', 'prix': 35.00, 'image': 'mario_party.png'},
        {'nom': 'Pokemon Stadium', 'prix': 40.00, 'image': 'pokemon_stadium.png'}
    ],
    'GameCube': [
        {'nom': 'Super Smash Bros. Melee', 'prix': 40.00, 'image': 'super_smash_bros_melee.png'},
        {'nom': 'The Legend of Zelda: The Wind Waker', 'prix': 45.00, 'image': 'zelda_the_wind_waker.png'},
        {'nom': 'Metroid Prime', 'prix': 35.00, 'image': 'metroid_prime.png'},
        {'nom': "Eternal Darkness: Sanity's Requiem", 'prix': 50.00, 'image': 'eternal_darkness.png'},
        {'nom': 'Resident Evil 4', 'prix': 40.00, 'image': 'resident_evil_4.png'},
        {'nom': 'Super Mario Sunshine', 'prix': 30.00, 'image': 'super_mario_sunshine.png'},
        {'nom': 'Paper Mario: The Thousand-Year Door', 'prix': 40.00, 'image': 'paper_mario.png'},
        {'nom': 'Animal Crossing', 'prix': 35.00, 'image': 'animal_crossing.png'},
        {'nom': 'Pikmin', 'prix': 30.00, 'image': 'pikmin.png'},
        {'nom': 'F-Zero GX', 'prix': 45.00, 'image': 'f_zero_gx.png'}
    ],
    'Game Boy': [
        {'nom': 'Tetris', 'prix': 20.00, 'image': 'tetris.png'},
        {'nom': 'Pokémon Rouge', 'prix': 25.00, 'image': 'pokemon_redpng'},
        {'nom': "The Legend of Zelda: Link's Awakening", 'prix': 30.00, 'image': 'zelda_links_awakening.png'},
        {'nom': 'Super Mario Land', 'prix': 20.00, 'image': 'super_mario_land.png'},
        {'nom': 'Metroid II: Return of Samus', 'prix': 35.00, 'image': 'metroid_II.png'},
        {'nom': "Kirby's Dream Land", 'prix': 20.00, 'image': 'kirbys_dream_land.png'},
        {'nom': 'Pokemon Gold', 'prix': 30.00, 'image': 'pokemon_gold.png'},
        {'nom': 'Donkey Kong', 'prix': 25.00, 'image': 'donkey_kong.png'},
        {'nom': 'Wario Land: Super Mario Land 3', 'prix': 30.00, 'image': 'wario_land.png'},
        {'nom': 'Final Fantasy Adventure', 'prix': 35.00, 'image': 'final_fantasy_adventure.png'}
    ],
    'Nintendo DS': [
        {'nom': 'New Super Mario Bros.', 'prix': 25.00, 'image': 'new_super_mario_bros.png'},
        {'nom': 'Mario Kart DS', 'prix': 30.00, 'image': 'mario_kart_ds.png'},
        {'nom': 'Pokemon Diamond', 'prix': 35.00, 'image': 'pokemon_diamond.png'},
        {'nom': 'The Legend of Zelda: Phantom Hourglass', 'prix': 40.00, 'image': 'zelda_phantom_hourglass.png'},
        {'nom': 'Animal Crossing: Wild World', 'prix': 25.00, 'image': 'animal_crossing_wild_world.png'},
        {'nom': "Mario & Luigi: Bowser's Inside Story", 'prix': 30.00, 'image': 'mario_luigi_bowsers_inside_story.png'},
        {'nom': 'Pokémon Blacke', 'prix': 35.00, 'image': 'pokemon_black.png'},
        {'nom': 'Brain Age', 'prix': 20.00, 'image': 'brain_age.png'},
        {'nom': 'Dragon Quest IX: Sentinels of the Starry Skies', 'prix': 40.00, 'image': 'dragon_quest_ix.png'},
        {'nom': 'Luigi Mansin 2', 'prix': 60.00, 'image': 'luigi_mansion_2.png'}
    ],
    'Nintendo Switch': [
        {'nom': 'The Legend of Zelda: Breath of the Wild', 'prix': 60.00, 'image': 'zelda_breath_of_the_wild.png'},
        {'nom': 'Super Mario Odyssey', 'prix': 55.00, 'image': 'super_mario_odyssey.png'},
        {'nom': 'Pokémon Sword', 'prix': 45.00, 'image': 'pokemon_sword_shield.png'},
        {'nom': 'Splatoon 2', 'prix': 40.00, 'image': 'splatoon_2.png'},
        {'nom': 'Mario Kart 8 Deluxe', 'prix': 45.00, 'image': 'mario_kart_8_deluxe.png'},
        {'nom': 'Super Smash Bros. Ultimate', 'prix': 50.00, 'image': 'super_smash_bros_ultimate.png'},
        {'nom': 'Luigi Mansion 3', 'prix': 35.00, 'image': 'luigi_mansion_3'},
    ],
    'PlayStation': [
        {'nom': 'Final Fantasy VII', 'prix': 40.00, 'image': 'final_fantasy_VII.png'},
        {'nom': 'Metal Gear Solid', 'prix': 30.00, 'image': 'metal_gear_solid.png'},
        {'nom': 'Gran Turismo', 'prix': 25.00, 'image': 'gran_turismo.png'},
        {'nom': 'Resident Evil', 'prix': 30.00, 'image': 'resident_evil.png'},
        {'nom': 'Crash Bandicoot', 'prix': 25.00, 'image': 'crash_bandicoot.png'},
        {'nom': 'Tomb Raider', 'prix': 20.00, 'image': 'tomb_raider.png'},
        {'nom': 'Spyro the Dragon', 'prix': 30.00, 'image': 'spyro_the_dragon.png'},
        {'nom': 'Castlevania: Symphony of the Night', 'prix': 35.00, 'image': 'castlevania_symphony_of_the_night.png'},
        {'nom': 'Tekken 3', 'prix': 20.00, 'image': 'tekken_3.png'},
        {'nom': 'Silent Hill', 'prix': 40.00, 'image': 'silent_hill.png'}
    ],
    'PS2': [
        {'nom': 'Grand Theft Auto: San Andreas', 'prix': 30.00, 'image': 'gta_san_andreas.png'},
        {'nom': 'God of War', 'prix': 25.00, 'image': 'god_of_war.png'},
        {'nom': 'Shadow of the Colossus', 'prix': 35.00, 'image': 'shadow_of_the_colossus.png'},
        {'nom': 'Metal Gear Solid 3: Snake Eater', 'prix': 30.00, 'image': 'metal_gear_solid_3.png'},
        {'nom': 'Final Fantasy X', 'prix': 35.00, 'image': 'final_fantasy_X.png'},
        {'nom': 'Resident Evil 4', 'prix': 30.00, 'image': 'resident_evil_4_ps2.png'},
        {'nom': 'Kingdom Hearts', 'prix': 25.00, 'image': 'kingdom_hearts.png'},
        {'nom': 'Jak and Daxter: The Precursor Legacy', 'prix': 30.00, 'image': 'jak_and_daxter.png'},
        {'nom': 'Ratchet & Clank', 'prix': 25.00, 'image': 'ratchet_and_clank.png'},
        {'nom': 'Devil May Cry', 'prix': 20.00, 'image': 'devil_may_cry.png'}
    ],
    'PS3': [
        {'nom': 'The Last of Us', 'prix': 35.00, 'image': 'the_last_of_us.png'},
        {'nom': 'Red Dead Redemption', 'prix': 25.00, 'image': 'red_dead_redemption.png'},
        {'nom': 'Batman: Arkham City', 'prix': 30.00, 'image': 'batman_arkham_city.png'},
        {'nom': 'Fallout 3', 'prix': 30.00, 'image': 'fallout_3.png'},
        {'nom': 'Assassins Creed II', 'prix': 25.00, 'image': 'assassins_creed_2.png'}
    ],
    'Xbox': [
        {'nom': 'Halo: Combat Evolved', 'prix': 30.00, 'image': 'halo_combat_evolved.png'},
        {'nom': 'Star Wars: Knights of the Old Republic', 'prix': 35.00, 'image': 'kotor.png'},
        {'nom': 'Splinter Cell', 'prix': 25.00, 'image': 'splinter_cell.png'},
        {'nom': 'Grand Theft Auto: Vice City', 'prix': 30.00, 'image': 'gta_vice_city.png'},
        {'nom': 'Burnout 3: Takedown', 'prix': 25.00, 'image': 'burnout_3.png'},
    ],
    'Sega Mega Drive': [
        {'nom': 'Sonic the Hedgehog', 'prix': 20.00, 'image': 'sonic_the_hedgehog.png'},
        {'nom': 'Streets of Rage 2', 'prix': 25.00, 'image': 'streets_of_rage_2.png'},
        {'nom': 'Mortal Kombat', 'prix': 25.00, 'image': 'mortal_kombat.png'},
        {'nom': 'Street Fighter II', 'prix': 30.00, 'image': 'street_fighter_2.png'},
    ],
    'Philips CD-i': [
        {'nom': 'Link: The Faces of Evil', 'prix': 50.00, 'image': 'link_the_faces_of_evil.png'},
        {'nom': 'Hotel Mario', 'prix': 40.00, 'image': 'hotel_mario.png'},
        {'nom': "Zelda's Adventure", 'prix': 60.00, 'image': 'zeldas_adventure.png'},
    ],
}

def generer_jeux_aleatoires():
    jeux_aleatoires = []
    jeux_utilises = set()  # Jeux déjà sélectionnés
    while len(jeux_aleatoires) < 6 and len(jeux_utilises) < len(jeux_video):
        console = random.choice(list(jeux_video.keys()))
        jeux_console = jeux_video[console]
        jeu = random.choice(jeux_console)
        nom = jeu['nom']
        if nom not in jeux_utilises:
            prix = jeu['prix']
            jeux_aleatoires.append({'nom': nom, 'console': console, 'prix': prix})
            jeux_utilises.add(nom)  # Ajouter le jeu à la liste des jeux utilisés
    return jeux_aleatoires

def afficher_jeux_aleatoires(jeux):
    print("Jeux vidéo générés aléatoirement :\n")
    for i, jeu in enumerate(jeux, 1):
        nom = jeu['nom']
        console = jeu['console']
        prix = jeu['prix']
        print(f"{i}. {nom} ({console}) - Prix : {prix} €")
    print()

# Génération des jeux aléatoires
jeux_aleatoires = generer_jeux_aleatoires()

# Affichage des jeux aléatoires
afficher_jeux_aleatoires(jeux_aleatoires)

# Création de la fenêtre Tkinter
window = Tk()
window.title("RetroHunter")
window.geometry("800x600")
window.minsize(800,600)
window.maxsize(800,600)

# Création du canevas pour afficher les jeux
canv = Canvas(window, width=800, height=600, bg='white')
canv.pack()

# Chargement des images des jeux
images = {}
for jeu in jeux_aleatoires:
    image_path = jeu['image']
    image = PhotoImage(file=image_path)
    images[jeu['nom']] = image

# Affichage des jeux avec leurs prix et images dans le canevas
for i, jeu in enumerate(jeux_aleatoires):
    nom = jeu['nom']
    console = jeu['console']
    prix = jeu['prix']
    image = images[nom]

    # Affichage de l'image
    canv.create_image(100, (i + 1) * 100, anchor=NW, image=image)

    # Affichage du nom du jeu et du prix
    text = f"{nom} ({console}) - Prix : {prix} €"
    canv.create_text(250, (i + 1) * 100 + 50, text=text, font=("Arial", 14), fill="black")

    # Création du bouton "Acheter"
    bouton_acheter = Button(text="Acheter", font=("Arial", 14), width=10)
    bouton_acheter.place(x=450, y=(i + 1) * 100 + 35)

# Lancement de la boucle principale Tkinter
window.mainloop()