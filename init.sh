sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default

#sudo rm -r /etc/gunicorn.d/hello.py
#sudo ln -s /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py

sudo service nginx restart
#sudo gunicorn -с /etc/gunicorn.d/hello.py hello:app
sudo gunicorn -b 0.0.0.0:8000 ask.qa:test &
