
mkdir -p /opt/www/sm/mdeia
mkdir -p /opt/www/sm/static
mkdir -p /opt/www/sm/logs
chown -R dustin.dustin /opt/www/sm
cp deploy/sm.conf /etc/init/

cat deploy/lighttp.conf >> /etc/lightppd/lighttpd.conf
