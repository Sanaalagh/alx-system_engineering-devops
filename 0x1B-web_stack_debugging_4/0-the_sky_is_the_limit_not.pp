# This Puppet manifest optimizes Nginx to handle more concurrent connections

exec { 'optimize-nginx-config':
  command => "/bin/sed -i 's/worker_connections 1024;/worker_connections 2048;/' /etc/nginx/nginx.conf",
  path    => ['/bin', '/usr/bin'],
  onlyif  => "/bin/grep -q 'worker_connections 1024;' /etc/nginx/nginx.conf",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Exec['optimize-nginx-config'],
}
