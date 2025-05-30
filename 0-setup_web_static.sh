#!/usr/bin/env bash

# Define servers
servers=("3.92.214.122" "3.88.21.35")

for server in "${servers[@]}"
do
    echo "Setting up server: $server"

    ssh -o StrictHostKeyChecking=no ubuntu@"$server" << 'ENDSSH'
        sudo apt-get -y update
        sudo apt-get -y upgrade
        sudo apt-get -y install nginx

        sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
        echo "This is a test" | sudo tee /data/web_static/releases/test/index.html

        sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

        sudo chown -hR ubuntu:ubuntu /data/

        sudo sed -i '/location \/ {/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

        sudo service nginx restart
ENDSSH

done

exit 0
