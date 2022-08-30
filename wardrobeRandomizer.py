import random

command = ""

shirts = ['akira tee', 'nike sb tee', 'pulp fiction tee', 'bape tee', 'supreme motion tee', 'assc blk logo tee',
          'supreme miles davis tee', 'assc x gallery tee', 'vintage - EC (red)', 'vintage - scat',
          'vintage - EC (blue)', 'supreme water pistol tee', 'vintage - kramer', 'mnml tee', 'frank ocean tee',
          'dgk noodle tee', 'rock steady tee', 'real love tee', 'mac miller tee', 'vintage - dodge tee', 'enjoi tee',
          'sovrn tee', 'politics tee', 'blk stussy tee', 'orange stussy tee', 'bulma tee', 'mike tyson tee',
          'grey coke tee', 'marine layer tee', 'red striped tee', 'george carlin tee', 'white pacsun skate tee',
          'hundreds tee', 'skate chick tee', 'l/s black jp tee', 'nike beast tee', 'dead inside tee',
          'thick as thieves tee', 'diamond tee', 'red nike jp tee']
pants = ['blk cargo pants', 'olive cargo pants', 'light blue jeans', 'brown joggers', 'grey joggers', 'blk joggers',
         'blk skinny jeans', 'dark blue jeans', 'chinos', 'blk b-ball shorts']
sneakers = ['infrared am90', "blk chucks", 'atmos dunks', 'nb 1010', 'chicago 1', 'mocha 1', 'game royal 1',
            'nyc to paris 1', 'taupe haze 4', 'am97', 'white af1', 'samba dunks', 'blazers', 'vans',
            'red chucks', 'white adidas']

alrightOutfit = [[sneakers[1] + " | " + shirts[2] + " | " + pants[2]],  # CHUCKS
                 [[sneakers[1] + " | " + shirts[5] + " | " + pants[2]]],
                 [[sneakers[1] + " | " + shirts[37] + " | " + pants[3]]],
                 [[sneakers[1] + " | " + shirts[12] + " | " + pants[3]]],
                 [[sneakers[1] + " | " + shirts[31] + " | " + pants[0]]],
                 [[sneakers[1] + " | " + shirts[25] + " | " + pants[5]]],
                 [[sneakers[3] + " | " + shirts[16] + " | " + pants[2]]],  # NB
                 [[sneakers[3] + " | " + shirts[18] + " | " + pants[2]]],
                 [[sneakers[3] + " | " + shirts[30] + " | " + pants[2]]],
                 [[sneakers[3] + " | " + shirts[32] + " | " + pants[2]]],
                 [[sneakers[13] + " | " + shirts[23] + " | " + pants[2]]],  # VANS
                 [[sneakers[12] + " | " + shirts[17] + " | " + pants[2]]],  # BLAZERS
                 [[sneakers[12] + " | " + shirts[23] + " | " + pants[2]]],
                 [[sneakers[12] + " | " + shirts[28] + " | " + pants[2]]],
                 [[sneakers[12] + " | " + shirts[34] + " | " + pants[2]]],
                 [[sneakers[15] + " | " + shirts[13] + " | " + pants[6]]],  # ADIDAS
                 [[sneakers[15] + " | " + shirts[2] + " | " + pants[2]]],
                 [[sneakers[14] + " | " + shirts[0] + " | " + pants[1]]]  # RED CHUCKS (16)
                 ]
mehOutfit = [[sneakers[13] + " | " + shirts[5] + " | " + pants[6]],  # VANS
             [[sneakers[13] + " | " + shirts[7] + " | " + pants[6]]],
             [[sneakers[13] + " | " + shirts[15] + " | " + pants[6]]],
             [[sneakers[13] + " | " + shirts[26] + " | " + pants[6]]],
             [[sneakers[1] + " | " + shirts[5] + " | " + pants[4]]],  # CHUCKS
             [[sneakers[1] + " | " + shirts[5] + " | " + pants[6]]],
             [[sneakers[1] + " | " + shirts[7] + " | " + pants[6]]],
             [[sneakers[1] + " | " + shirts[15] + " | " + pants[6]]],
             [[sneakers[1] + " | " + shirts[26] + " | " + pants[6]]]  # (9)
             ]
dopeOutfit = [[sneakers[4] + " | " + shirts[0] + " | " + pants[0]],  # CHICAGO 1
              [[sneakers[4] + " | " + shirts[26] + " | " + pants[2]]],
              [[sneakers[4] + " | " + shirts[8] + " | " + pants[2]]],
              [[sneakers[5] + " | " + shirts[14] + " | " + pants[1]]],  # MOCHA 1
              [[sneakers[5] + " | " + shirts[35] + " | " + pants[0]]],
              [[sneakers[5] + " | " + shirts[14] + " | " + pants[2]]],
              [[sneakers[5] + " | " + shirts[11] + " | " + pants[0]]],
              [[sneakers[6] + " | " + shirts[10] + " | " + pants[0]]],  # GAME ROYAL 1
              [[sneakers[6] + " | " + shirts[36] + " | " + pants[0]]],
              [[sneakers[6] + " | " + shirts[25] + " | " + pants[0]]],
              [[sneakers[7] + " | " + shirts[37] + " | " + pants[3]]],  # NYC TO PARIS 1
              [[sneakers[8] + " | " + shirts[14] + " | " + pants[1]]],  # TAUPE HAZE 4
              [[sneakers[0] + " | " + shirts[0] + " | " + pants[8]]],  # AM90
              [[sneakers[0] + " | " + shirts[26] + " | " + pants[2]]],
              [[sneakers[9] + " | " + shirts[38] + " | " + pants[9]]],  # AM97
              [[sneakers[10] + " | " + shirts[10] + " | " + pants[9]]],  # AF1
              [[sneakers[10] + " | " + shirts[39] + " | " + pants[9]]],
              [[sneakers[2] + " | " + shirts[19] + " | " + pants[0]]],  # SB DUNK
              [[sneakers[2] + " | " + shirts[6] + " | " + pants[0]]],
              [[sneakers[2] + " | " + shirts[1] + " | " + pants[0]]],
              [[sneakers[11] + " | " + shirts[4] + " | " + pants[8]]],  # SAMBA DUNK
              [[sneakers[13] + " | " + shirts[33] + " | " + pants[6]]]  # VANS - (20)
              ]
while command != "quit".lower():
    command = input("""Select Option:
        - Shirt...      - I'm in a mood...
        - Pants...      - Random!!!
        - Sneakers...
        >""").lower()
    # SHIRT
    if command == 'shirt':
        print(*shirts, sep="\n")
        print(" ")  # SPACING
        selection = input('Select shirt:').lower()
        print("""
        Outfit ideas:
        -------------""")
        if selection == shirts[0].lower():
            print((alrightOutfit[17]))
            break
        elif selection == shirts[1].lower():
            print(dopeOutfit[19])
            break
        elif selection == shirts[2].lower():
            print(alrightOutfit[0])
            print(alrightOutfit[16])
            break
        elif selection == shirts[3].lower():
            print("unlisted")
        elif selection == shirts[4].lower():
            print(dopeOutfit[20])
        elif selection == shirts[5].lower():
            print(alrightOutfit[1])
            print(mehOutfit[0])
            print(mehOutfit[4])
            print(mehOutfit[5])
            break
        elif selection == shirts[6].lower():
            print(dopeOutfit[18])
        elif selection == shirts[7].lower():
            print(mehOutfit[1])
            print(mehOutfit[6])
        elif selection == shirts[8].lower():
            print(dopeOutfit[2])
            break
        elif selection == shirts[9].lower():
            print("unlisted")
        elif selection == shirts[10].lower():
            print(dopeOutfit[15])
            print(dopeOutfit[7])
            break
        elif selection == shirts[11].lower():
            print(dopeOutfit[6])
            break
        elif selection == shirts[12].lower():
            print(alrightOutfit[3])
            break
        elif selection == shirts[13].lower():
            print(alrightOutfit[15])
            break
        elif selection == shirts[14].lower():
            print(dopeOutfit[3])
            print(dopeOutfit[5])
            print(dopeOutfit[11])
            break
        elif selection == shirts[15].lower():
            print(mehOutfit[2])
            print(mehOutfit[7])
            break
        elif selection == shirts[16].lower():
            print(alrightOutfit[6])
            break
        elif selection == shirts[17].lower():
            print(alrightOutfit[11])
            break
        elif selection == shirts[18].lower():
            print(mehOutfit[7])
            break
        elif selection == shirts[19].lower():
            print(dopeOutfit[17])
            break
        elif selection == shirts[20].lower():
            print("unlisted")
        elif selection == shirts[21].lower():
            print("unlisted")
        elif selection == shirts[22].lower():
            print("unlisted")
        elif selection == shirts[23].lower():
            print(alrightOutfit[10])
            print(alrightOutfit[12])
            break
        elif selection == shirts[24].lower():
            print("unlisted")
        elif selection == shirts[25].lower():
            print(alrightOutfit[5])
            break
        elif selection == shirts[26].lower():
            print(mehOutfit[3])
            print(mehOutfit[8])
            print(dopeOutfit[1])
            print(dopeOutfit[13])
        elif selection == shirts[27].lower():
            print("unlisted")
        elif selection == shirts[28].lower():
            print(alrightOutfit[13])
            break
        elif selection == shirts[29].lower():
            print("unlisted")
        elif selection == shirts[30].lower():
            print(alrightOutfit[8])
            break
        elif selection == shirts[31].lower():
            print(alrightOutfit[4])
            break
        elif selection == shirts[32].lower():
            print(alrightOutfit[9])
            break
        elif selection == shirts[33].lower():
            print(dopeOutfit[21])
            break
        elif selection == shirts[34].lower():
            print(alrightOutfit[14])
            break
        elif selection == shirts[35].lower():
            print(dopeOutfit[4])
            break
        elif selection == shirts[36].lower():
            print(dopeOutfit[8])
            break
        elif selection == shirts[37].lower():
            print(alrightOutfit[2])
            break
        elif selection == shirts[38].lower():
            print(dopeOutfit[14])
            break
        elif selection == shirts[39].lower():
            print(dopeOutfit[16])
            break
    # PANTS
    elif command == 'pants':
        print(*pants, sep="\n")
        print(" ")  # SPACING
        selection = input('Select pants: ')
        print("""
                Outfit ideas:
                -------------""")
        if selection == pants[0].lower():
            print(alrightOutfit[4])
            print(dopeOutfit[0])
            print(dopeOutfit[4])
            print(dopeOutfit[6])
            print(dopeOutfit[7])
            print(dopeOutfit[8])
            print(dopeOutfit[9])
            print(dopeOutfit[17])
            print(dopeOutfit[18])
            print(dopeOutfit[19])
            break
        elif selection == pants[1].lower():
            print(alrightOutfit[17])
            print(dopeOutfit[3])
            print(dopeOutfit[11])
            break
        elif selection == pants[2].lower():
            print(alrightOutfit[0])
            print(alrightOutfit[1])
            print(alrightOutfit[6])
            print(alrightOutfit[7])
            print(alrightOutfit[8])
            print(alrightOutfit[9])
            print(alrightOutfit[10])
            print(alrightOutfit[11])
            print(alrightOutfit[12])
            print(alrightOutfit[13])
            print(alrightOutfit[14])
            print(alrightOutfit[16])
            print(dopeOutfit[1])
            print(dopeOutfit[2])
            print(dopeOutfit[5])
            print(dopeOutfit[13])
            break
        elif selection == pants[3].lower():
            print(alrightOutfit[2])
            print(alrightOutfit[3])
            print(dopeOutfit[10])
            break
        elif selection == pants[4].lower():
            print(mehOutfit[4])
            break
        elif selection == pants[5].lower():
            print(alrightOutfit[5])
            break
        elif selection == pants[6].lower():
            print(alrightOutfit[15])
            print(mehOutfit[0])
            print(mehOutfit[1])
            print(mehOutfit[2])
            print(mehOutfit[3])
            print(mehOutfit[5])
            print(mehOutfit[6])
            print(mehOutfit[7])
            print(mehOutfit[8])
            print(dopeOutfit[21])
            break
        elif selection == pants[7].lower():
            print('unlisted')
            break
        elif selection == pants[8].lower():
            print(dopeOutfit[12])
            print(dopeOutfit[20])
            break
    # SNEAKERS
    elif command == 'sneakers':
        print(*sneakers, sep="\n")
        print(" ")  # SPACING
        selection = input('Select sneakers: ')
        print("""
                Outfit ideas:
                -------------""")
        if selection == sneakers[0].lower():
            print(dopeOutfit[12])
            print(dopeOutfit[13])
            break
        elif selection == sneakers[1].lower():
            print(alrightOutfit[0])
            print(alrightOutfit[1])
            print(alrightOutfit[3])
            print(alrightOutfit[4])
            print(alrightOutfit[5])
            print(alrightOutfit[6])
            print(mehOutfit[4])
            print(mehOutfit[5])
            print(mehOutfit[6])
            print(mehOutfit[7])
            print(mehOutfit[8])
            break
        elif selection == sneakers[2].lower():
            print(sneakers[17])
            print(sneakers[18])
            print(sneakers[19])
            break
        elif selection == sneakers[3].lower():
            print(alrightOutfit[6])
            print(alrightOutfit[7])
            print(alrightOutfit[8])
            print(alrightOutfit[9])
            break
        elif selection == sneakers[4].lower():
            print(dopeOutfit[0])
            print(dopeOutfit[1])
            print(dopeOutfit[2])
            break
        elif selection == sneakers[5].lower():
            print(dopeOutfit[3])
            print(dopeOutfit[4])
            print(dopeOutfit[5])
            print(dopeOutfit[6])
            break
        elif selection == sneakers[6].lower():
            print(dopeOutfit[7])
            print(dopeOutfit[8])
            print(dopeOutfit[9])
            break
        elif selection == sneakers[7].lower():
            print(dopeOutfit[10])
            break
        elif selection == sneakers[8].lower():
            print(dopeOutfit[11])
            break
        elif selection == sneakers[9].lower():
            print(dopeOutfit[14])
            break
        elif selection == sneakers[10].lower():
            print(dopeOutfit[15])
            print(dopeOutfit[16])
            break
        elif selection == sneakers[11].lower():
            print(dopeOutfit[20])
            break
        elif selection == sneakers[12].lower():
            print(alrightOutfit[11])
            print(alrightOutfit[12])
            print(alrightOutfit[13])
            print(alrightOutfit[14])
            break
        elif selection == sneakers[13].lower():
            print(mehOutfit[0])
            print(mehOutfit[1])
            print(mehOutfit[2])
            print(mehOutfit[3])
            break
        elif selection == sneakers[14].lower():
            print(alrightOutfit[17])
            break
        elif selection == sneakers[15].lower():
            print(alrightOutfit[15])
            print(alrightOutfit[16])
            break
    # MOOD
    elif command == "mood".lower():
        # blah blah blah
        selection = input("""What kind of mood are you in?
        -Feelin' alright!
        -Meh...
        -Dope!!
        >""")
        if selection == 'alright'.lower():
            print("""
            Here's a random outfit idea:
            ----------------------------
            """)
            print(random.choice(alrightOutfit))
            break
        elif selection == 'meh'.lower():
            print("""
             Here's a random outfit idea:
            -----------------------------
            """)
            print(random.choice(mehOutfit))
            break
        elif selection == 'dope'.lower():
            print("""
             Here's a random outfit idea:
            -----------------------------
            """)
            print(random.choice(dopeOutfit))
            break
        else:
            "I don't know...?"
    # RANDOM
    elif command == 'random':
        print('--------------------------')
        print("Here's your outfit!")
        print('Shirt: ' + random.choice(shirts))
        print('Pants: ' + random.choice(pants))
        print('Sneakers: ' + random.choice(sneakers))
        print('--------------------------')
        break
    elif command == 'quit':
        print('Exiting.')
        break
    else:
        print("Sorry, I don't understand that...")

    # Wardrobe app
    # Choose article of clothing (i.e. shirt, pants, sneaker)
    # Asks user clothes, mood, or random
    # build outfit using pre-made designs
    # -possibly add a build mode
    # -possibly add feature to be able to store new outfits/add clothes
