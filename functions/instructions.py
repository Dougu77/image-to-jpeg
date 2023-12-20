def folder_instructions():
    print('\n' + f'{"-" * 33}' + ' CONVERSOR DE IMAGENS ' + f'{"-" * 33}' + '\n')
    print('>>> Converta imagens de diversos formatos diferentes para JPEG.')
    print('>>> Formatos suportados: PNG, JPG, JPEG e WEBP.')
    print('>>> Coloque as imagens que deseja converter na pasta "images/original".')
    print('>>> Não coloque pastas dentro de "images/original", e sim diretamente as imagens.')
    print('>>> Depois de colocar as imagens na pasta indicada, digite "OK".')
    print('\n' + f'{"-" * 36}' + ' IMAGE CONVERTER ' + f'{"-" * 35}' + '\n')
    print('>>> Convert images from different formats to JPEG.')
    print('>>> Suported formats: PNG, JPG, JPEG and WEBP.')
    print('>>> Put the images that you want to convert in the folder "images/original".')
    print('>>> Don\'t put folders in "images/original", just put directly the images.')
    print('>>> After putting the images in the right folder, type "OK".')

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
    print('\n' + f'{"-" * 88}')
