#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# Only add the location block if it doesn't already exist
if ! grep -q "location /hbnb_static" /etc/nginx/sites-enabled/default; then
    sudo sed -i '/listen 80 default_server/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
fi

sudo nginx -t && sudo systemctl restart nginx