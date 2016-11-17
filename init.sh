sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default

sudo ln -s -r /home/box/etc/hello.py /etc/gunicorn.d/hello.py

sudo service nginx restart
sudo service gunicorn restart
