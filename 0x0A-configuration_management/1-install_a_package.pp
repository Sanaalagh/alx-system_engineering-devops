# 1-install_a_package.pp
# This manifest installs Flask version 2.1.0 using pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.1.1',  # Make sure Werkzeug is installed with the compatible version
  provider => 'pip3',
}
