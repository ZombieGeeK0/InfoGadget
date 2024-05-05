import os, sys, platform, datetime, socket
from colorama import Fore, Back

BLUE = '\033[34m'
MAGENTA = '\033[35m'
WHITE = '\033[37m'
RESET = '\033[39m'

def clear():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

date = hora = datetime.datetime.now() 
hostname = socket.gethostname()
IPv4 = socket.gethostbyname(hostname)

def menu():
  clear()
  print(Fore.MAGENTA + Back.RESET)

  title = '''
  ╔═══                                                                                                            ═══╗ 
    ::::::::::: ::::    ::: :::::::::: ::::::::   ::::::::      :::     :::::::::   ::::::::  :::::::::: ::::::::::: 
        :+:     :+:+:   :+: :+:       :+:    :+: :+:    :+:   :+: :+:   :+:    :+: :+:    :+: :+:            :+:     
        +:+     :+:+:+  +:+ +:+       +:+    +:+ +:+         +:+   +:+  +:+    +:+ +:+        +:+            +:+     
  ║     +#+     +#+ +:+ +#+ :#::+::#  +#+    +:+ :#:        +#++:++#++: +#+    +:+ :#:        +#++:++#       +#+     ║ 
        +#+     +#+  +#+#+# +#+       +#+    +#+ +#+   +#+# +#+     +#+ +#+    +#+ +#+   +#+# +#+            +#+     
        #+#     #+#   #+#+# #+#       #+#    #+# #+#    #+# #+#     #+# #+#    #+# #+#    #+# #+#            #+#     
    ########### ###    #### ###        ########   ########  ###     ### #########   ########  ##########     ### 
  ╚═══                                                                                                            ═══╝
  '''
  print(Fore.MAGENTA + Back.RESET + title)

  information = '''
  [!] ©2023 by Phoenix
  [!] Github: https://github.com/3xpl017/InfoGadget
  [!] Presiona enter despues de ver el resultado de tu comando para volver al menú.
  '''

  print(Fore.BLUE + Back.RESET + information)

  options = '''
  [!] Para detener en cualquier momento, presiona CONTROL + C.
  [+] help: Show every commands.
  [+] os: Display the information obtained with the os module.
  [+] sys: display the information obtained with the sys module.
  [+] platform: display the information obtained with the platform module.
  [+] socket: display the information obtained with the socket module.
  [+] datetime: display the information obtained with the datetime module.
  '''
  print(Fore.BLUE + Back.RESET + options)

  answer = input(Fore.WHITE + Back.MAGENTA + 'InfoGadget:~$ ')

  if answer.lower() == 'help':
    print(Fore.BLUE + Back.RESET + options)
    print('\n')
    answer = input(Fore.WHITE + Back.MAGENTA + 'InfoGadget:~$ ')
    menu()

  elif answer.lower() == 'os':
    print(Fore.BLUE + Back.RESET)
    print('[+] Ruta de la ubicación actual: ' + str(os.getcwd()))
    print('\n[+] Carpetas que hay en tu directorio actual: ' + str(os.listdir()))
    print('\n')
    answer = input(Fore.WHITE + Back.MAGENTA + 'InfoGadget:~$ ')
    menu() 

  elif answer.lower() == 'sys':
    print(Fore.BLUE + Back.RESET)
    print('[+] Nombre del sistema operativo según el módulo sys: ' + sys.platform)
    print('\n[+] Información extra: ')
    sys1 = sys.getwindowsversion()
    sys2 = sys.version_info
    print('\n[+] ' + str(sys1))
    print('[+] ' + str(sys2))
    print('\n')
    answer = input(Fore.WHITE + Back.MAGENTA + 'InfoGadget:~$ ')
    menu() 

  elif answer.lower() == 'platform':
    print(Fore.BLUE + Back.RESET)
    print('[+] Información del sistema operativo: ' + str(platform.architecture()))
    print('[+] Modelo del procesador: ' + str(platform.machine()))
    print('[+] Información específica del procesador: ' + str(platform.processor()))   
    print('[+] Información sobre la plataforma del sistema operativo: ' + str(platform.platform()))  
    print('[+] Nombre del sistema operativo: ' + str(platform.system()))
    print('[+] Información extra del sistema operativo a trvés de uname: ' + str(platform.uname())) 
    print('\n')
    answer = input(Fore.WHITE + Back.MAGENTA + 'InfoGadget:~$ ')
    menu() 

  elif answer.lower() == 'socket':
    print(Fore.BLUE + Back.RESET)
    print('[+] IPv4: ' + IPv4)
    print('[+] Nombre del equipo: ' + hostname + '\n')
    answer = input(Fore.WHITE + Back.MAGENTA + 'InfoGadget:~$ ')
    menu() 

  elif answer.lower() == 'datetime':
    print(Fore.BLUE + Back.RESET)
    print('[+] Fecha y hora actual: ' + str(date))
    print('\n')
    answer = input(Fore.WHITE + Back.MAGENTA + 'InfoGadget:~$ ')
    menu() 

  else:
    print(Fore.BLUE + Back.RESET)
    print('[!] Error: Command not found :(\n')
    answer = input(Fore.WHITE + Back.MAGENTA + 'InfoGadget:~$ ')
    menu() 

menu()
