import py7zr
import time
import os
import zipfile
import py7zr
#coding=utf-8
def estrai_archivi(directory, estensione, directory_destinazione, password):
    for filename in os.listdir(directory):
        if filename.endswith(estensione):
            full_path = os.path.join(directory, filename)
            if estensione == '.zip':
                with zipfile.ZipFile(full_path, 'r') as zip_ref:
                    try:
                        zip_ref.extractall(directory_destinazione)
                        print(f"File ZIP '{filename}' estratto con successo.")
                    except Exception as e:
                        print("Errore sconosciuto: " + str(e))
            elif estensione == '.7z':
                with py7zr.SevenZipFile(full_path, 'r', password=password) as zip_ref:
                    try:
                        zip_ref.extractall(directory_destinazione)
                        print(f"File 7z '{filename}' estratto con successo.")
                    except Exception as e:
                        print("Errore sconosciuto: " + str(e))
            else:
                print(f"Estensione non supportata per il file '{filename}'.")
    return filename



# Esempio di utilizzo
cartella_di_lavoro = 'Z:\\samples'
estensione_da_cercare = '.7z'  # o '.7z' a seconda del tipo di archivio
password_archivio = 'infected'  # lascia None se non c'e' una password
directory_destinazione = "C:\\Users\\student\\Desktop\\sample"

file_cancellare = estrai_archivi(cartella_di_lavoro, estensione_da_cercare, directory_destinazione, password_archivio)
# esegue il comando procdump con percorso berasaglio per il dump e nome del processo da lanciare.

import subprocess
# coding=utf-8
program_path = 'C:\\Users\\student\\Desktop\\procdump\\procdump.exe'  # Sostituisci 'NomeDelProgramma.exe' con il nome effettivo del tuo programma
arg1 = '-accepteula'
arg2 = '-ma'
arg3 = '-t'
arg4 = '-x'
arg5 = 'Z:\\dumps'
directory_sample = 'C:\\Users\\student\\Desktop\\sample'

def cancella_file(percorso_file):
    try:
        os.remove(percorso_file)
        print(f"Il file {percorso_file} e' stato cancellato con successo.")
    except FileNotFoundError:
        print(f"Il file {percorso_file} non e' presente.")
    except Exception as e:
        print(f"Si e' verificato un errore durante la cancellazione del file: {str(e)}")
		


		
killerfilename = "provuis"	
def find_arg6(directory):
	for cartella_corrente, sottocartelle, files in os.walk(directory):
		for file in files:
			if file.endswith(".exe"):
				global killerfilename
				killerfilename = file
				print("trovato filename "+killerfilename)
				return os.path.join(cartella_corrente, file)

			
arg6 = find_arg6(directory_sample)
try:
    process = subprocess.Popen([program_path, arg1, arg2, arg3, arg4, arg5, arg6])
except FileNotFoundError:
    print(f"Errore: Il programma '{program_path}' non e' stato trovato.")
except Exception as e:
    print(f"Errore sconosciuto: {e}")
time.sleep(5)
	
	
print("Cercando di terminare "+killerfilename)
try:
    process = subprocess.Popen(['taskkill', '/F', '/IM', killerfilename])
except FileNotFoundError:
    print("Errore: Il programma +"+program_path+" non e' stato trovato.")
except Exception as e:
    print("Errore sconosciuto per la terminazione: {e}")
time.sleep(5)	
try:
    process = subprocess.Popen(['taskkill', '/F', '/IM', 'procdump.exe'])
except FileNotFoundError:
    print("Errore: Il programma '{program_path}' non e' stato trovato.")
except Exception as e:
    print("Errore sconosciuto: {e}")

# Esempio di utilizzo
percorso_del_file = cartella_di_lavoro + "\\"+file_cancellare # Inserisci il percorso del file che desideri cancellare
#process.wait()
cancella_file(percorso_del_file)