# Ensure the SSH config directory exists
file { '/home/vagrant/.ssh':
  ensure => directory,
  owner  => 'vagrant',
  group  => 'vagrant',
  mode   => '0700',
}

# Ensure the SSH client configuration file exists
file { '/home/vagrant/.ssh/config':
  ensure => file,
  owner  => 'vagrant',
  group  => 'vagrant',
  mode   => '0600',
}

# Configure SSH to use the private key for authentication
file_line { 'Declare identity file':
  ensure => present,
  path   => '/home/vagrant/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile',
  replace => true,
}

# Turn off password authentication
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/home/vagrant/.ssh/config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
  replace => true,
}
