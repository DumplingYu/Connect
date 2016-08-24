## Define Fundamental Color Values
BLACK = '#000000'
WHITE = '#FFFFFF'
RED = '#FF0000'
GREEN = '#00FF00'
BLUE = '#0000FF'
YELLOW = '#FFFF00'
PURPLE = '#FF00FF'
AQUA = '#00FFFF'

skins = ['Hacker','Night']
choice = 'Night'

#appearances = {i:j for i,j in zip(skins, ({} for j in range(len(skins))))}

for skin in skins:
    if skin == 'Hacker': # Hacker skin
        # Colors
        mainBgColor = BLACK
        logBgColor = BLACK
        logFgColor = GREEN
        logHlColor = BLACK
        boxBgColor = BLACK
        boxFgColor = GREEN
        boxHlColor = GREEN
        # Others
        logCursor = 'arrow'
        
    if skin == 'Night': # Hacker skin
        # Colors
        mainBgColor = BLACK
        logBgColor = BLACK
        logFgColor = GREEN
        logHlColor = BLACK
        boxBgColor = BLACK
        boxFgColor = GREEN
        boxHlColor = GREEN
        # Others
        logCursor = 'arrow'
