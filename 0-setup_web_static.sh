#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static

apt-get update
apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<h1>Wakhi-Ken</h1>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist).
# This should be recursive; everything inside should be created/owned by this user/group.
chown -hR ubuntu:ubuntu /data

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
# (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
# Use alias inside your Nginx configuration
bash -c "echo -e '$SERVER_CONFIG' > /etc/nginx/sites-available/default"
ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

if [ "$(pgrep -c nginx)" -le 0 ]; then
	service nginx start
else
	service nginx restart
    service nginx reload
fi