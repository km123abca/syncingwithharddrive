echo off
:l

set /p fil=Enter file choice




if %fil% equ q (
goto :q

)


pause
cls
goto :l
:q