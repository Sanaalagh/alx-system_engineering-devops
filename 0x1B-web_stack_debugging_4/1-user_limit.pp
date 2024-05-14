# This Puppet manifest increases the file descriptor limits for the 'holberton' user

file_line { 'increase-fd-limits':
  path  => '/etc/security/limits.conf',
  line  => 'holberton soft nofile 4096\nholberton hard nofile 10000',
  match => '^holberton.*',
}

exec { 'apply-sysctl-fs-file-max':
  command => "/sbin/sysctl -w fs.file-max=100000",
  unless  => "/sbin/sysctl -n fs.file-max | /bin/grep -q 100000",
}
