sudo apt-get install python3
rm data/output.txt
python3 ./sort.py
curl -XPOST -F file=@/home/liz/Documents/Sortable/data/output.txt https://challenge-check.sortable.com/validate
