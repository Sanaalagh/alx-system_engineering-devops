# 0-create_a_file.pp
# This manifest creates a file at /tmp/school with specified content, owner, group, and permissions

file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
