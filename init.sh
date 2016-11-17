sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default


sudo service nginx restart
sudo gunicorn -b 0.0.0.0:8080 hello.py:app &
