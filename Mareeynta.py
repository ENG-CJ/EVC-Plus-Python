
pin=2244
new=0
def maareeynta_file():
    print('''
Maareynta
1: Badel lambarka sirta ah
2: Badel Luuqadda
3: Wargelin Mobile Lumay
    ''')
    Input_choice=input('')
    if Input_choice=='1':
        new_pin=int(input('Fadlan Geli Pin-kaaga Cusub: '))
        valid=int(input('Hubi Pin-kaaga Cusub: '))
        if valid==new_pin:
            print('Waad Ku Guulaysatay Inaad Badasho Pin-kaaga')
        else:
            print(f'{new_pin} != {valid}')
    elif Input_choice=='2':
        print('1: English\n2: Arabic')
        valid=input('')
        if valid=='1':
            print('Waad Ku Guulaysatay Inaad Badasho Luuqadda')

        elif valid == '2':
            print('Waad Ku Guulaysatay Inaad Badasho Luuqadda')
        else:
            print('Invalid Choice')
    elif Input_choice=='3':
        mobile=int(input('Fadlan Geli Mobile-ka Lumay: '))
        if len(str(mobile))<=10:
            number = int(input('fadlan Gelu Number-kisa Sirta: '))
            print(f'Mahubtaa Inaad Udiwan geliso Lumid Number-kaan ({mobile}) \n1: Haa\n2: Maya')
            valid2=input('')
            if valid2=='1':
                print(f'Waad Ku Guulaysatay Inaad Udiwan geliso Number-kaan {mobile} Inuu Lumay')
            else:
                print('Macsalaama!')
        else:
            print('Number-ka Aad Gelisay Majiro')
    else:
        print('Invalid Choice')