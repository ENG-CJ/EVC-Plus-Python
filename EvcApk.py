postal=2244
balance=200

categories="""
1: Itus Haraaga
2: Kaarka Hadalka
3: Bixi Biil
4: Uwareeji
5: Warbixin Kooban
6: Salaam Bank
7: Mareeynta
8: Xawilaad
0: Kabax
"""

def display():
    print('[EVC PLUS]')
    print('-HORMUUD SERVICE-')
    return

def TypeError(err,display):
    print(f'Sida aad Isticmashay {err}'
          f' Waa Khalad\nFadlan Isticmaal'
          f' {display}'
          )
    return
def display2():
    print(categories)

def incorrect():
    print('Number-ka Sirta Waa Khalad')
def itus_haraaga(haraaga):
    print(f'Haraagagu Waa ${haraaga}'
)
def sub_field():
    print('1: Kushubo Airtime\n2: Ugushub Airtime')

def kushubo(pin,lacag,number): # Function And Its Validation
    if pin==postal:
        if lacag<=balance:
            print('[EVC-PLUS] waxaad'
                  f' ${lacag} Ugushubtay {number}'
                  f' \nHaragagu Waa ${balance-lacag}')
        else:
            print('Haraagagu Kuguma Filna')
    else:
        print('Number-ka Sirta Waa KHALAD')

def Biil():
    print('1: Ogoow Biilka')
    print('2: Ku Iibso')

def  Validation_transfer(pin,transfer_money,business_,business_no):
    if pin==postal:
        if transfer_money<=balance:
            print(f'[EVC-PLUS]\nWaxaad ${transfer_money} Udirtay'
                  f' Ganacsade {business_} ({business_no}'
                  f' \nHaragagu waa ${balance-transfer_money})')
        else:
            print('Haraagagu Kuguma Filna')
    else:
        print('Number-ka Sirta Waa khalad')

def valid_transfer(pin,money,No):
    if pin==postal:
        if money<=balance:
            print(f'[EVC-PLUS] Waxaa ${money} Uwareejisay {No}'
                  f'\nHaraagagu waa ${balance-money}')
        else:
            print('Haragagu Kuguma Filna')
    else:
        print('Number-ka Sirta Waa Khalad')