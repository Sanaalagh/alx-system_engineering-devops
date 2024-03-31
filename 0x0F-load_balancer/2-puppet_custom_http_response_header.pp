# Define class for Nginx installation and configuration
class nginx_custom_header {
    package { 'nginx':
        ensure => 'installed',
    }

    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => "server {
            ...
            add_header X-Served-By $hostname;
            ...
        }",
        require => Package['nginx'],
    }

    service { 'nginx':
        ensure => 'running',
        enable => true,
        require => File['/etc/nginx/sites-available/default'],
    }
}

# Apply the class to the servers
node 'web-01', 'web-02' {
    include nginx_custom_header
}
