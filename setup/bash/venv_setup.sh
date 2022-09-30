#windows
mainDir=$PWD
cd ..;
python -m venv venv;
echo "venv creado";
mv venv/ $mainDir/venv/;
echo "venv puesto en " $mainDir;
cd $mainDir;
. venv/Scripts/activate; 
echo "Corriendo venv";
pip install -r paquetes.txt;
echo "Script concluido";