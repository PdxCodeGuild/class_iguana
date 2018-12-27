
class Interaction:
    def __init__(self, coordinate, text):
        self.coord = coordinate
        self.text_list = text 


base = [['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],   
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n']
]

level_list = [
#          0  1   2     3     4     5     6     7     8     9     10    11  12  13
        [['','   ',' | ','   ','   ','   ','   ','   ','   ','   ',' | ',' U ','','\n'],
        ['','   ',' | ','  [',']  ',' []','   ','[] ','  [',']  ',' | ','   ','','\n'],
        ['','   ',' | ','   ','   ','   ','   ','   ','   ','   ',' | ','   ','','\n'],
        ['','   ',' | ','  [',']  ',' []','   ','[] ','  [',']  ',' | ','   ','','\n'],
        ['',' 0 ',' | ','   ','   ','   ','_ _','   ','   ','   ',' | ','   ','','\n'],
        ['','   ',' |_','__[',']__','__[','_|_',']__','__[',']__','_| ','   ','','\n'],   # Level 0
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n'],
        ['','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','','\n']
        ],

        [['-','---','---','---','---','---','===','---','---','---','---','---','-','\n'],
        ['|','|¯¯','ΞΞΞ','¯¯|','   ','   ','| |','   ','   ','ΞΞΞ','ΞΞΞ','¯¯|','|','\n'],
        ['|','| |','   ','|  ','ΞΞΞ','   ','| |','   ','|Ō|','   ','   ','| |','|','\n'],
        ['|','| |','   ','| |','   ','   ','| |','   ','|__','ΞΞΞ','¯ ¯','__|','|','\n'],
        ['|','| |','   ','|__','ΞΞΞ','ΞΞΞ','__|','   ','   ','   ','| |','   ','|','\n'],
        ['|','| |','   ','   ','   ','   ',' X ','ΞΞΞ','¯¯|','   ','|__','¯¯|','|','\n'],   # Level 1
        ['|','| |','   ','   ','|¯¯','ΞΞΞ','¯¯|','   ','| |','   ','   ','| |','|','\n'],
        ['|','|__','ΞΞΞ','ΞΞΞ','  |','   ','| |','   ','| |','   ','   ','| |','|','\n'],
        ['|','   ','   ','   ','| |','   ','|  ','ΞΞΞ','ΞΞΞ','ΞΞΞ','ΞΞΞ','  |','|','\n'],
        ['|','|Ō|','   ','   ','| |','   ','| |','   ','   ','   ','   ','| |','|','\n'],
        ['|','|__','ΞΞΞ','ΞΞΞ','__|','   ','| |','   ','ΞΞΞ','ΞΞΞ','ΞΞΞ','__|','|','\n'],
        ['|','   ','   ','   ','   ','   ','|_|','   ','   ','   ','   ','   ','|','\n']
        ],

        [['-','---','---','---','---','---','===','---','---','---','---','---','-','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],   # Level 2
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','---','---','---','---','---','___','---','---','---','---','---','|','\n']
        ],

        [['-','---','---','---','---','---','===','---','---','---','---','---','-','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],   # Level 3
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','---','---','---','---','---','___','---','---','---','---','---','|','\n']
        ],

        [['-','---','---','---','---','---','---','---','---','---','---','---','-','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ',' T ','   ',' T ','   ','   ','   ',' T ','   ',' T ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],   # Level 4
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ',' X ','   ','   ','   ','   ','   ',' X ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','|','\n'],
        ['|','---','---','---','---','---','___','---','---','---','---','---','|','\n']
        ]
]




npc1 = Interaction((1,4), 'Hello, World')
trash = Interaction((11,0), 'This is a trash can. There\'s trash in here...')

level_objects = [
    {'doors' : [(6,5),(6,4)],       # level 0
    'special' : [npc1, trash],
    },
    {'doors' : [(6,0)],      # level 1
    'special' : [(8,2),(1,9)],
    },
    {'doors' : [(6,0)],      # level 2
    'special' : [],
    },
    {'doors' : [(6,0)],      # level 3
    'special' : [],
    },
    {'doors' : [(6,0)],      # level 4
    'special' : [(2,2),(4,2),(8,2),(10,2),(3,8),(3,9)],
    }
]



