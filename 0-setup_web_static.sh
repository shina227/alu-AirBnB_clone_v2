#!/usr/bin/env bash
# Script that sets up web servers for deployment

# Install Nginx if not already installed
apt-get -y update
apt-get -y install nginx

# Create directories if they don't exist
mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file for testing
cat > /data/web_static/releases/test/index.html << EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Remove existing symbolic link if it exists and create new one
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group recursively
chown -hR ubuntu:ubuntu /data/

# Update Nginx configuration - add location block after server_name
if ! grep -q "location /hbnb_static" /etc/nginx/sites-available/default; then
    sed -i '/server_name _;/a\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
fi

# Restart Nginx to apply configuration
service nginx restart