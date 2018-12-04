"""Author: Richard Sherman
2018-12-04
make-change.py, makes change in various currencies based on user input"""

# note: this is revised from an assignment I tried & failed to write for Al's Intro to Programming course
# note: change in Old British Pounds is all wrong, but you get the idea (and they're out of circulation anyway)

# first make a dict of currencies by countries and coins / divisions

currencies = {'GBP': {
                    'country': 'Great Britain',
                    'currency': 'old pounds',
                    'div'	:	[
                                'shillings'	,
                                'pence' ,
                                'farthings'
                                ] ,
                    'vals'	:	[
                                20 ,
                                12 ,
                                0.25
                                ]
                    } ,
            'USD'	:	{
                    'country'	:	'United States' ,
                    'currency'	:	'dollars' ,
                    'div'	:	[
                                'quarters' ,
                                'dimes' ,
                                'nickels' ,
                                'pennies'
                                ] ,
                    'vals'	:	[
                                25 ,
                                10 ,
                                5 ,
                                1
                                ]
                        } ,
            'KRW'	:	{
                    'country'	:	'Korea' ,
                    'currency'	:	'won' ,
                    'div'	:	[
                                'man' ,
                                'cheon' ,
                                'baek' ,
                                'won'
                                ] ,
                    'vals'	:	[	1000000 ,
                                100000 ,
                                10000 ,
                                100
                                ]

                        } ,
            'Kwatloos' :	{
                    'country'	:	'Triskelion' ,
                    'currency'	:	'kwatloos' ,
                    'div'	:	[
                                'kwatwhirls' ,
                                'kwatcircs'	,
                                'kwatyus' ,
                                'kwatrights' ,
                                'kwangles'
                                ] ,
                    'vals'	:	[
                                760 ,
                                360 ,
                                180 ,
                                90 ,
                                45
                                ]
                                } ,
            "Guilders" :	{
                    'country'	:	'Netherlands' ,
                    'currency'	:	'guilders' ,
                    'div'	:	[
                                'vijfjes' ,
                                'rijksdaalders' ,
                                'gulden' ,
                                'kwartjes' ,
                                'dubbeltjes' ,
                                'stuivers'
                                ] ,
                    'vals'	:	[
                                500 ,
                                250 ,
                                100 ,
                                25 ,
                                10 ,
                                5
                                ]
        }
}

# now get input and make change
# there should be (but isn't) some checking here for valid input

print("\nI can make change for you. First, I need to know which currency you are using.")
print \
    ("\nYou can choose between: \n\t\tOld British pounds \n\t\tUS dollars \n\t\tKorean won \n\t\tTriskelionian kwatloos, or \n\t\tDutch guilders.")
print \
    ("\nBut my boss is very picky. He insists that you type either:\n\t\t'GBP' for pounds \n\t\t'USD' for dollars \n\t\t'KRW' for won \n\t\t'Kwatloos' for kwatloos, or \n\t\t'Guilders' for guilders.")
cur_choice = input( "\nWhich currency would you like to change? Please type it in without quotation marks: > " )
amt = input( f"\nHow many {cur_choice} would you like to change? \n\tPlease, remember that my boss is very picky. You need to enter the ammount in the form xx.xx, for example: 123.45, 123.00, etc. > ")
amt =  int(amt.replace('.', ''))
print("\nYour change is: \n" )
i = 0
while i <= len(currencies[cur_choice]['vals']) -1:
    q_i = amt // currencies[cur_choice]['vals'][i]
    amt = amt % currencies[cur_choice]['vals'][i]
    print(f"\t{q_i}\t{currencies[cur_choice]['div'][i]}")
    i = i + 1


