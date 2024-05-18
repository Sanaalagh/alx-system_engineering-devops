# This Puppet manifest optimizes Nginx to handle more concurrent connections
exec { '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
