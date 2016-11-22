sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo service nginx restart

sudo rm -r /etc/gunicorn.d/test-wsgi
sudo rm -r /etc/gunicorn.d/test-django
sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test-wsgi
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
sudo /etc/init.d/gunicorn restart


#sudo gunicorn -с /etc/gunicorn.d/hello.py hello:app
#sudo gunicorn -b 0.0.0.0:8000 ask.qa:test &
