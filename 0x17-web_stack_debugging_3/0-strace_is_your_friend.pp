# 0-strace_is_your_friend.pp
# This Puppet manifest fixes missing configuration file issue for Apache on WordPress
file { '/path/to/missing/config.file':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => "Configuration content goes here\n",
}

exec { 'restart-apache':
  command     => '/etc/init.d/apache2 restart',
  refreshonly => true,
  subscribe   => File['/path/to/missing/config.file'],
}
