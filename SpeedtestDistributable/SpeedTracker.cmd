@echo off
:start
echo %DATE% >>testspeed.txt
echo %TIME% >>testspeed.txt
speedtest_cli.py >>testspeed.txt
timeout /t 900 /nobreak >nul
if 1 equ 1 goto :start
