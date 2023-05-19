import os
import subprocess
from tkinter import *
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Código da aplicação que requer permissões de administrador
    print("Permissão de administrador concedida!")
else:
    # Se o usuário não for um administrador, solicite permissões de administrador
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

subprocess.call('powercfg /h off', shell=True)


def check_updates():
    print("A verificar atualizações do Windows...")
    subprocess.call("wuauclt /detectnow", shell=True)
    print("O sistema encontra-se atualizado...")

def desativar_fastboot():
    print("A desativar o Windows Fastboot...")
    subprocess.call('powercfg /h off', shell=True)
    print("Fastboot desativado...")

def scan_virus():
    print("A procura de Virus...")
    subprocess.call("powershell.exe Get-MpComputerStatus", shell=True)
    print("Sistema seguro...")

def clean_temp_files():
    print("A limpar ficheiros temporarios...")
    subprocess.call("powershell.exe Clear-RecycleBin", shell=True)
    print("Ficheiros temporarios eliminados...")

def fix_windows_problems():
    print("Fixing Windows problems...")
    subprocess.call("sfc /scannow", shell=True)
    subprocess.call("DISM /online /cleanup-image /checkhealth", shell=True)
    subprocess.call("DISM /online /Cleanup-image /RestoreHealth", shell=True)
    print("Concluido...")

def add_user():
    subprocess.run(['net', 'user', 'Gestor', 'stop', '/add'])
    print("Gestor adicionado...")

def update_cuco():
    print("A remover CUCO")
    cuco_local = "F:\20210517101 (1).bat"
    os.system(cuco_local)
    os.system(cuco_local)
def remover_umbrella():
     print("A remover Umbrella")
     subprocess.run ('wmic Product where name="Umbrella Roaming Client" call uninstall', shell=True)
     print("Umbrella removido... Execute Desbloqueio CUCO")


def main():
    janela = Tk()
    janela.title("Manutenção do Windows")
    janela.geometry("500x500")
    janela.configure(background='#778899')
    janela.resizable(width=False, height=False)


    #janela, text= "Desenvolvido por João luz"
    botao_check_updates = Button(janela, text="Atualizar Windows", width=20, command=check_updates)
    botao_check_updates.place(x=180, y=50)

    botao_desativar_fastboot = Button(janela, text="Desativar Fastboot", width=20, command=desativar_fastboot)
    botao_desativar_fastboot.place(x=180, y=100)

    botao_scan_virus = Button(janela, text="Procurar Virus", width=20, command=scan_virus)
    botao_scan_virus.place(x=180, y=150)

    botao_clean_temp_files = Button(janela, text="Limpar Temp Files", width=20, command=clean_temp_files)
    botao_clean_temp_files.place(x=180, y=200)

    botao_fix_windows_problems = Button(janela, text="Corrigir problemas do Windows", width=30, command=fix_windows_problems)
    botao_fix_windows_problems.place(x=150, y=250)

    botao_add_gestor = Button(janela, text="Adicionar Gestor", width= 20,command=add_user)
    botao_add_gestor.place(x=180, y=300)

    botao_update_cuco = Button(janela, text="Desbloqueio Cuco", width= 20,command=update_cuco)
    botao_update_cuco.place(x=180, y= 350)

    botao_remover_umbrella = Button(janela, text="Remover Umbrella", width= 20,command=remover_umbrella)
    botao_remover_umbrella.place(x=180, y= 400)
    janela.mainloop()



if __name__ == "__main__":
    
    main()