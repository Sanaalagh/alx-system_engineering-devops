# 2-execute_a_command.pp
# This manifest uses pkill to terminate any process named killmenow

exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/bin/', '/usr/bin/', '/sbin/', '/usr/sbin/'],
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
