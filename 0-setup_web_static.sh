#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

# Install Nginx if not already installed
apt-get update -y
apt-get install nginx -y

# Create directories if they don't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
cat << EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Remove existing symbolic link if it exists and create new one
rm -f /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to add hbnb_static location
# Use a more reliable method to add the location block
if ! grep -q "/hbnb_static" /etc/nginx/sites-available/default; then
    # Find the location / block and add our location before it
    sed -i '/location \/ {/i\
\
	location /hbnb_static {\
		alias /data/web_static/current/;\
	}\
' /etc/nginx/sites-available/default
fi

# Restart Nginx to apply configuration
service nginx restart

# Ensure script exits successfully
exit 0