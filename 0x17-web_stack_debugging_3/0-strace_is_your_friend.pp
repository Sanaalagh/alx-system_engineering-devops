# Puppet manifest to ensure the php5-mysql package is installed
# This fixes a common issue where PHP cannot communicate with MySQL,
# leading to a 500 error on Wordpress sites.

class wordpress_fix {
  package { 'php5-mysql':
    ensure => installed,
  }

  service { 'apache2':
    ensure     => running,
    enable     => true,
    subscribe  => Package['php5-mysql'],
    require    => Package['php5-mysql'],
  }
}

include wordpress_fix
