# 1-install_a_package.pp
# This manifest installs Flask version 2.1.0 using pip3

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
}
