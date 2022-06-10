logout
sudo ls -la /root
logout
apt list --upgradable
logout
sudo ls -a
cat .sudo_as_admin_successful 
sudo ls -a
sudo apt-get update
sudo apt-get install python-pip ython-dev
sudo apt-get install python-pip python-dev
sudo apt-get install python3-pip python3-virtualenv
sudo apt-get install mysql-server
mysql
sudo mysql
sudo mysql_secure_installation
sudo mysql
mysql -u epleadmanager
mysql -u epleadmanager -p
sudo mysql
systemctl status mysql.service
ls
ls -a
ls .ssh
cat ~/.ssh/id_rsa.pub | pbcopy
ssh-keygen
cat ~/.ssh/id_rsa.pub | pbcopy
cat ~/.ssh/id_rsa.pu
cat ~/.ssh/id_rsa.pub
git clone git@bitbucket.org:jacobbothaws/ep-lead-manager.git
ls
cd ep-lead-manager/
ls
cd ~
mv ep-lead-manager/ epleads/
ls
cd epleads/
git status
git branch
git checkout feature/production
git fetch
git branch
git checkout release/production
ls
virtualenv venv
ls
source venv/bin/activate
pip install django mysqlclient
pip list
sudo apt-get install python-dev default-libmysqlclient-dev
pip install django mysqlclient
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
pip install gunicorn
python manage.py collectstatic
python manage.py createsuperuser
sudo ufw allow 8000
python manage.py runserver 0.0.0.0:8000
vim epleads/settings.py 
python manage.py runserver 0.0.0.0:8000
vim epleads/settings.py 
python manage.py runserver 0.0.0.0:8000
gunicorn --bind 0.0.0.0:8000 epleads.wsgi
N
deactivate
sudo vim /etc/systemd/system/gunicorn.socket
sudo vim /etc/systemd/system/gunicorn.service
sudo systemctl status gunicorn.socket
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket
file /run/gunicorn.sock
ls
cd ~
sudo systemctl status gunicorn
curl --unix-socket /run/gunicorn.sock localhost
vim epleads/settings.py 
vim epleads/epleads/settings.py 
curl --unix-socket /run/gunicorn.sock localhost
sudo journalctl -u gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
curl --unix-socket /run/gunicorn.sock localhost
curl --unix-socket /run/gunicorn.sock localhost\leads_admin
sudo nano /etc/nginx/sites-available/epleads
sudo vim /etc/nginx/sites-available/epleads
sudo nano /etc/nginx/sites-available/epleads
sudo apt-get install nginx
sudo vim /etc/nginx/sites-available/epleads
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
curl --unix-socket /run/gunicorn.sock
curl --unix-socket /run/gunicorn.sock localhost\leads_admin
curl --unix-socket /run/gunicorn.sock localhost
curl --unix-socket /run/gunicorn.sock localhost/leads_admin
curl --unix-socket /run/gunicorn.sock localhost
curl --unix-socket /run/gunicorn.sock localhost/leads_admin/
ls epleads/
ls/run/
ls /run/
sudo nginx -t
sudo vim /etc/nginx/sites-available/epleads
sudo vim /etc/systemd/system/gunicorn.service 
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket
file /run/gunicorn.sock 
sudp jouralctl -u gunicorn.socket
sudo journalctl -u gunicorn.socket
sudo systemctly status gunicorn
sudo systemctl status gunicorn
sudo vim /etc/nginx/sites-available/epleads
sudo ln -s /etc/nginx/sites-available/epleads /etc/nginx/sites-enabled/
sudo nginx -t
sudo stemctl restart nginx
sudo systemctl restart nginx
sudo journalctl -xe
sudo tail -F /var/log/nginx/error.log
ls /etc/nginx/sites-enabled/
rm /etc/nginx/sites-enabled/myproject 
sudo rm /etc/nginx/sites-enabled/myproject 
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
cd ~
openssl req -newkey rsa:2048 -nodes -keyout epdata.com.au.key -out epdata.com.csr
cat epdata.csr
ls -a
openssl req -newkey rsa:2048 -nodes -keyout epdata.com.au.key -out epdata.com.au.csr
cat epdata.com.au
cat epdata.com.au.csr
ls -A
rm epdata.com.csr 
ls
logout
apt list --upgradable
ls
cat example.com.crt intermediate.crt > example.com.chained.crt
cat epdata.com.au.crt intermediate.crt > example.com.chained.crt
cd /etc/nginx/sites-enabled
ls
sudo vim default 
sudo service nginx restart
sudo ufw allow 443
sudo service nginx restart
sudo nginx -t && sudo systemctl restart nginx
ls
ls ~/
mv ~/example.com.chained.crt ~/epdata.com.au.chained.crt
ls ~/
sudo nginx -t && sudo systemctl restart nginx
sudo ufw status
sudo ufw remove 443
sudo ufw delete 443
sudo ufw delete allow 443
sudo all 'Nginx Full'
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'
sudo nginx -t && sudo systemctl restart nginx
sudo vim default 
sudo nginx -t && sudo systemctl restart nginx
sudo vim default 
sudo nginx -t && sudo systemctl restart nginx
sudo vim default 
cat epleads 
sudo vim default 
sudo nginx -t && sudo systemctl restart nginx
sudo vim epleads 
sudo nginx -t && sudo systemctl restart nginx
ls
cd epleads/
ls
git staus
git status
git fetch
git status
git pull
ls
ls leads
git pull
git diff epleads/settings.py
git stash
git pull
sudo systemctl restart gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service
sudo nginx -t && sudo systemctl restart nginx
sudo tail -F /var/log/nginx/error.log
sudo journalctl -u gunicorn
sudo journalctl -u gunicorn.socket
sudo systemctl status mysql
sudo systemctl restart gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service
sudo nginx -t && sudo systemctl restart nginx
git status
git pop
cat epleads/settings.py 
git unstash
git stash --help
git stash pop
sudo nginx -t && sudo systemctl restart nginx
sudo systemctl restart gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service
sudo nginx -t && sudo systemctl restart nginx
git status
sudo systemctl status gunicorn.socket
sudo journalctl -u gunicorn.socket
sudo journalctl -u gunicorn
curl --unix-socket /run/gunicorn.sock localhost
file /run/gunicorn.sock
cat /etc/systemd/system/gunicorn.service
ls
cat epleads.wsgi
ls epleads/
sudo systemctl reset-failed gunicorn.service
sudo systemctl status gunicorn.socket[
ls
ls venv
ls venv/bin/
sudo systemctl reset-failed gunicorn.socket
sudo systemctl status gunicorn.socket
sudo systemctl status gunicorn
sudo systemctl restart gunicorn.socket gunicorn.service
sudo systemctl status gunicorn
sudo journalctl -u gunicorn.socket
ls /var/logs
ls /var/log
ls /var/log/nginx/
cat /var/log/nginx/error.log
sudo vim /var/log/nginx/error.log
git stash
git pull
pip list
pip instal
pip install
pip install requirements.txt
pip install -r requirements.txt
pip list
pip install django-import-export
pip install django-phonenumber-field
pip install -r requirements.txt
pip install scrapy
pip list
python manage.py makemigrations
source venv/bin/activate
pip install -r requirements.txt
pip list
pip install django-import-export
pip install django-phonenumber-field
pip install scrapy
python manage.py migrate
pip list
python manage.py migrate
cat epleads/settings.py 
pip list
pip -r requirements.txt 
pip install -r requirements.txt 
pip install django-phonenumber-field[phonenumberslite]
python manage.py migrate
sudo systemctl restart gunicorn
sudo systemctl status gunicorn
q
ls
cat import_export.log 
sudo journalctl -u gunicorn
git pull master
git pull
cd epleads/
git pull
python manage.py import -h
ls
source venv/bin/activate
python manage.py import -h
logout
ls
ls ~
mkdir importdata
ls
logout
ls
cd epleads/
source venv/bin/activate
python manage.py import centre ~/importdata/EnglandChildcaresFinal.csv 
systemctl status mysql
python manage.py import centre ~/importdata/EnglandChildcaresFinal.csv 
mysql -u epleadmanager -p
vim epleads/settings.py 
python manage.py import centre ~/importdata/EnglandChildcaresFinal.csv 
sudo systemctl restart gunicorn
ls
python manage.py import centre ~/importdata/EnglandChildcaresFinal.csv 
mysql.server start
mysql
mysql -h localhost -u leadmanager -p
mysql -h localhost -u root -p
systemctl status mysql
mysql -u epleadmanager -p
mysql -h localhost -epu leadmanager -p
mysql -h localhost -u epleadmanager -p
vim epleads/settings.py 
mysql -h localhost -u epleadmanager -p
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
systemctl status mysql
ls /tmp/
mysql restart
systemctl restart mysql
sudo systemctl restart mysql
python manage.py import centre ~/importdata/EnglandChildcaresFinal.csv 
cd epleads/
source venv/bin/activate
python manage.py import centre ~/importdata/EnglandChildcaresFinal.csv 
ls /var/run/mysqld/
mysql -u root -p
mysql -u root
sudo find / -type s
vim epleads/settings.py 
python manage.py import centre ~/importdata/EnglandChildcaresFinal.csv 
vim epleads/settings.py 
python manage.py import centre ~/importdata/EnglandChildcaresFinal.csv 
sudo service mysql statys
sudo service mysql status
sudo service mysql stop
sudo service mysql start
sudo service mysql stop
sudo service mysql start
sudo service mysql status
python manage.py import centre ~/importdata/EnglandChildcaresFinal.csv 
vim epleads/settings.py 
python manage.py import centre ~/importdata/EnglandChildcaresFinal.csv 
mysql -u leadmanager -p -h localhost
mysql -u leadmanager -p
mysql -u epleadmanager -p
logout
ls importdata/
logout
ls importdata/
cd importdata/epleadsdata/
mysql -u epleadmanager -p 
mysql -u epleadmanager -p -h localhost epleads
ls
mysql -u epleadmanager -p -h localhost epleads < ep_lead_manager_leads_centre.sql
mysql -u epleadmanager -p 
mysql -u epleadmanager -p -h localhost epleads < ep_lead_manager_leads_phone.sql
cd epleads/
git status
git stash
git stash pop
git pull
sudo systemctl restart gunicorn
git pull
sudo systemctl restart gunicorn
mysql -u epleadmanager -p
mysql -u epleadmanager
mysql -u epleadmanager -p
cd epleads/
source venv/bin/activate
python manage.py shell
