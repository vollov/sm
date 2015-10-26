
mkdir -p /opt/www/jennyli/mdeia
mkdir -p /opt/www/jennyli/static
mkdir -p /opt/www/jennyli/logs
chown -R dustin.dustin /opt/www/jennyli
cp deploy/jennyli.conf /etc/init/

cat deploy/lighttpd.conf >> /etc/lighttpd/lighttpd.conf
