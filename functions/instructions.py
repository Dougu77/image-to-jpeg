def choose_language():
    language = ''
    print('Escolha o idioma | Choose the language')
    while(language != 'PT' and language != 'EN'):
        language = input('[PT | EN]: ').strip().upper()
    return language

def folder_instructions(language):
    ok = ''
    if language == 'PT':
        print('\n' + f'{"-" * 15}' + ' CONVERSOR DE IMAGENS ' + f'{"-" * 15}')
        print('\n>>> Converta imagens de diversos formatos diferentes para JPEG.')
        print('>>> Formatos suportados: PNG, JPG, JPEG e WEBP')
        print('>>> Coloque as imagens que deseja converter na pasta "images/original".')
        print('>>> Depois de colocar as imagens na pasta indicada, digite "OK".')
    elif language == 'EN':
        print('\n' + f'{"-" * 15}' + ' IMAGE CONVERTER ' + f'{"-" * 15}')
        print('\n>>> Convert images from different formats to JPEG.')
        print('>>> Suported format: PNG, JPG, JPEG and WEBP')
        print('>>> Put the images that you wish to convert in the folder "images/original".')
        print('>>> After putting the images in the right folder, type "OK".')
    while(ok != 'OK'):
            ok = input('OK: ').strip().upper()

def ending(language):
    if language == 'PT':
        input('\nSUCESSO! Pressione qualquer tecla para sair... ')
    elif language == 'EN':
        input('\nSUCESS! Press any key to exit... ')
