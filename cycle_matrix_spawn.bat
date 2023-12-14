@echo off
setlocal enabledelayedexpansion



rem Cicla su ogni file nella cartella
for %%I in (E:\scritturaTesiMagistrale\dump\text\*) do (
    rem Esegui il comando per ogni file
    matrix_spawn.py %%I
)

endlocal
