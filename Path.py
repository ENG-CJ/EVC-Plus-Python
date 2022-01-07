import EvcApk as e
import Warbixin_kooban as wr
import  Salam_bank as bank
import  Mareeynta as mr
# Variables
pin=2244
balance=200
zipCode='*770#'
app=e.display()
code=input('')
# Validations
if code=='*770#':
    Pin=int(input('Fadlan Geli Pin-kaaga: '))
    if Pin==pin:
        e.display2()
        chose=input('')
        if chose=='1':
            e.itus_haraaga(balance)
        elif chose=='2':
            e.sub_field()
            # Components 2
            field_ch=input('')
            if field_ch=='1':
                telephone=int(input('Geli Number-ka: '))
                if len(str(telephone))<=10:
                    money=int(input('Geli Lacagta: '))
                    print(f'[Evc-Plus] Mahubtaa Inaad '
                          f' ${money} Ugu Shubto {telephone}'
                          f' \n1: Haa\n2: Maya')
                    valid=input('')
                    if valid=='1':
                        valid_pin=int(input('Geli Pin-kaaga: '))
                        e.kushubo(valid_pin,money,telephone)
                    else:
                        print('Macsalaama!')

                else:
                    print('Number-ka aad gelisay majiro')
            elif field_ch=='2':
                telephone = int(input('Geli Number-ka: '))
                if len(str(telephone)) <= 10:
                    money = int(input('Geli Lacagta: '))
                    print(f'[Evc-Plus] Mahubtaa Inaad '
                          f' ${money} Ugu Shubto {telephone}'
                          f' \n1: Haa\n2: Maya')
                    valid = input('')
                    if valid == '1':
                        valid_pin = int(input('Geli Pin-kaaga: '))
                        e.kushubo(valid_pin, money, telephone)
                    else:
                        print('Macsalaama!')

                else:
                    print('Number-ka aad gelisay majiro')
            else:
                print('Invalid Choice')

            # End Comp2---
        elif chose=='3':
            # Component 3
            e.Biil()
            Input_data=input('')
            if Input_data=='1':
                print('Fadlan Isticmaal Adeega Caawiye *140#')
            elif Input_data=='2':
                Business_man=input('Geli Aqoonsiga Ganacsiga: ')
                Business_number=int(input('Geli Number-ka Ganacsadaha: '))
                if len(str(Business_number))<=6:
                    Money=int(input('Geli Lacgata: '))
                    print(f'Mahubtaa Inaad ${Money} Udirtid Ganacade {Business_man} ({Business_number})'
                          f' \n1: Haa\n2: Maya')
                    valid_input=input('')
                    if valid_input=='1':
                        Valid_Pin=int(input('Geli Pin-kaaga: '))
                        e.Validation_transfer(Valid_Pin,Money,Business_man,Business_number)
                    else:
                        print('Macsalaama!')
                else:
                    print('Number-ka Aad Gelisay Majiro')
            else:
                print('Invalid Choice')
        elif chose=='4':
            # Component 4
            number=int(input('Fadlan Geli Mobile-ka: '))
            if len(str(number))<=10:
                money=int(input('Geli Lacagta: '))
                print(f'Mahubtaa Inaad ${money} Uwareejisid {number}'
                      f'\n1: Haa\n2: Maya')
                valid_input=input('')
                if valid_input=='1':
                    Pin_number=int(input('Geli Pin-kaaga: '))
                    e.valid_transfer(Pin_number,money,number)
                else:
                    print('Macsalaama!')
            else:
                print('Number-ka Aad Gelisay Majiro')
        elif chose=='5':
            wr.Incomplete_information()
        elif chose=='6':
            bank.bank()
        elif chose=='7':
            mr.maareeynta_file()


    else:
        e.incorrect()
else:
    e.TypeError(code,zipCode)

