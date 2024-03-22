# 1-install_a_package.pp
# This manifest installs Flask version 2.1.0 using pip3

package { 'Flask':
  ensure   => '3.0.2',
  provider => 'pip3',
}
