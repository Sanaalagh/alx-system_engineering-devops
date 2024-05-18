# This Puppet manifest increases the file descriptor limits for the 'holberton' user
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
