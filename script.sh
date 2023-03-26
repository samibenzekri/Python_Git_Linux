curl https://www.google.com/finance/quote/ENX:EPA?hl=fr > CodeSource.txt
price=$(cat CodeSource.txt | grep -oP '(?<="YMlKec fxKbKc">)[^<]+' | tr ',' '.'|tr -d '€')
echo "$(date),$price" >> prix.csv
sudo fuser -k 8050/tcp
/usr/bin/python3 /home/ec2-user/app.py

