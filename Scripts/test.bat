set _path=%cd%
for %%a in ("%_path%") do set "p_dir=%%~dpa"
echo %p_dir%

set args=asd
set args=%1
set key=a
if defined args (if not "%args%" =="a" (echo no) ) else (echo no)

::if defined args (echo no)

::if defined args (if not %1 == a (echo noo) else (echo yea)) else (echo no)

::if "%1" =="a" (echo go)
echo exit
pause