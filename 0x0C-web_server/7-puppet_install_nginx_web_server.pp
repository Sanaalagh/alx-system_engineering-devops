# Puppet script to install and configure Nginx on Ubuntu. It sets up Nginx to listen on port 80, serve a "Hello World!" page at the root, and redirect "/redirect_me" with a 301 to YouTube.

class nginx_setup {

  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    require    => Package['nginx'],
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => '<html><body><h1>Hello World!</h1></body></html>',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('modulename/nginx_default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/snippets/redirect_me.conf':
    ensure  => file,
    content => 'return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  exec { 'nginx_reload':
    command     => '/usr/sbin/nginx -s reload',
    refreshonly => true,
  }
}

include nginx_setup
