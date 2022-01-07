balance=200
pin=2244

def bank():
    print('1: Kawareeji EVCPLUS')
    Input=input('')
    if Input=='1':
        print('1: SALAAM SOMALI BANK')
        print('2: Salaam Bank')
        choice=input('')
        if choice=='1':
            koonto=int(input('Fadlan Geli Koontada: '))
            macluumad=input('Geli Faafahin: ')
            money=int(input('Geli Lacagta: '))
            if koonto==30050005:
                print(f'Mahubtaa Inaad ${money} Kudirto'
                      f' Koontada (JAMHUURIYA UNIVERSITY OF '
                      f' SCIENCE AND TECHNOLOGY [JUST])'
                      f'\n1: Haa\n2: Maya')
                validation=input('')
                if validation=='1':
                    Pin=int(input('Geli Pin-kaaga: '))
                    if Pin==pin:
                        if money<=balance:
                            print(f'[SALAM BANK] Waxaad ${money}'
                                  f' Udirtay koontada {koonto}'
                                  f'\nHaragagu Waa ${balance-money}')
                        else:
                            print('Haragagu Kuguma Filna')
                    else:
                        print('Number-ka Sirta Waa khalad')
                else:
                    print('Macsalama!')
            else:
                print(f'Mahubtaa Inaad ${money} Kudirto Koontada {koonto}'
                      f'\n1: Haa\n2: Maya')
                validation = input('')
                if validation == '1':
                    Pin = int(input('Geli Pin-kaaga: '))
                    if Pin == pin:
                        if money <= balance:
                            print(f'[SALAM BANK] Waxaad ${money}'
                                  f' Udirtay koontada {koonto}'
                                  f'\nHaragagu Waa ${balance - money}')
                        else:
                            print('Haragagu Kuguma Filna')
                    else:
                        print('Number-ka Sirta Waa khalad')
                else:
                    print('Macsalama!')
        elif choice=='2':
            koonto = int(input('Fadlan Geli Koontada: '))
            macluumad = input('Geli Faafahin: ')
            money = int(input('Geli Lacagta: '))
            if koonto == 30050005:
                print(f'Mahubtaa Inaad ${money} Kudirto'
                      f' Koontada (JAMHUURIYA UNIVERSITY OF '
                      f' SCIENCE AND TECHNOLOGY [JUST])'
                      f'\n1: Haa\n2: Maya')
                validation = input('')
                if validation == '1':
                    Pin = int(input('Geli Pin-kaaga: '))
                    if Pin == pin:
                        if money <= balance:
                            print(f'[SALAM BANK] Waxaad ${money}'
                                  f' Udirtay koontada {koonto}'
                                  f'\nHaragagu Waa ${balance - money}')
                        else:
                            print('Haragagu Kuguma Filna')
                    else:
                        print('Number-ka Sirta Waa khalad')
                else:
                    print('Macsalama!')
            else:
                print(f'Mahubtaa Inaad ${money} Kudirto Koontada {koonto}'
                      f'\n1: Haa\n2: Maya')
                validation = input('')
                if validation == '1':
                    Pin = int(input('Geli Pin-kaaga: '))
                    if Pin == pin:
                        if money <= balance:
                            print(f'[SALAM BANK] Waxaad ${money}'
                                  f' Udirtay koontada {koonto}'
                                  f'\nHaragagu Waa ${balance - money}')
                        else:
                            print('Haragagu Kuguma Filna')
                    else:
                        print('Number-ka Sirta Waa khalad')
                else:
                    print('Macsalama!')