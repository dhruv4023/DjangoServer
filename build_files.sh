
echo "BUID START"
pip install -r requirements.txt
python3.9 manage.py collectstatic
echo "BUID END" 
