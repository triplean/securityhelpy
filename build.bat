md build
cd build
pyinstaller --noconfirm --onefile --windowed --icon "../logo.ico"  "../main.py"
ROBOCOPY "../" "./dist/" logo.ico /mt /z
cls
echo "Building complete. Exiting."