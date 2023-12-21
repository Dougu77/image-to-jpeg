def folder_instructions():
    print('\n' + f'{"-" * 36}' + ' CONVERSOR DE IMAGENS ' + f'{"-" * 35}' + '\n')
    print('>>> Converta imagens de diversos formatos diferentes para JPEG.')
    print('>>> Formatos suportados: PNG, JPG, JPEG e WEBP.')
    print('>>> Coloque as pastas com as imagens que deseja converter na pasta "images/original".')
    print('>>> Depois de colocar as pastas no local indicado, digite "OK".')
    print('\n' + f'{"-" * 38}' + ' IMAGE CONVERTER ' + f'{"-" * 38}' + '\n')
    print('>>> Convert images from different formats to JPEG.')
    print('>>> Suported formats: PNG, JPG, JPEG and WEBP.')
    print('>>> Put the folders with the images that you want to convert in the folder "images/original".')
    print('>>> After putting the folders in the right place, type "OK".')

def ask_ok():
    print('')
    ok = ''
    while ok != 'OK':
            ok = input('OK: ').strip().upper()

def convert_again():
    print('\nSUCESSO! Deseja fazer outra conversão? | SUCESS! Do you want to do another conversion?\n')
    again = ''
    answers = ['SIM', 'S', 'YES', 'Y', 'NAO', 'NO', 'N']
    while again not in answers:
        again = input('SIM / YES | NÃO / NO: ').strip().upper().replace('Ã', 'A')
    if again in answers[:4]: return True
    else: return False

def write_line():
    print('\n' + f'{"-" * 93}')
