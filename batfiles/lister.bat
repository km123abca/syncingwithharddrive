echo off


cd ..
set /p foldder=<"files\folderloc.txt"
dir /b /A:-D %foldder% >"files\filles.txt"