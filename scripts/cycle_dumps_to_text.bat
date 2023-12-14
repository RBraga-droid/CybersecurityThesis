@echo off
setlocal enabledelayedexpansion

rem Imposta il percorso della cartella di partenza
set "cartella_di_partenza=E:\scritturaTesiMagistrale\dump\windbg"



rem Itera attraverso tutti i file .txt nella cartella di partenza
for %%i in ("%cartella_di_partenza%\*.dmp") do (
	rem Imposta il comando da eseguire per ciascun file .txt
	
    rem Esegui il comando specifico per ciascun file
    C:\Users\braga\AppData\Local\Microsoft\WindowsApps\WinDbgX.exe -c ".scriptload E:\scritturaTesiMagistrale\scripts\RunCommand.js;dx Debugger.State.Scripts.RunCommand.Contents.RunCommands()" %%i

    rem Stampa un messaggio opzionale per indicare l'avanzamento
    echo Eseguito il comando per il file: %%i
)

echo Operazione completata.
pause
