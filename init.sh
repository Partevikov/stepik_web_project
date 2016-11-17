sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default

sudo ln -s -r /home/box/etc/hello.py /etc/gunicorn.d/hello.py

sudo service nginx restart
sudo gunicorn -b 0.0.0.0:8080 hello:app &
