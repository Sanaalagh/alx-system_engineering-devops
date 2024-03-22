#!/usr/bin/pup
# 1-install_a_package.pp
# This manifest installs Flask version 2.1.0 using pip3
package { 'python3-pip':
  ensure => 'installed',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
