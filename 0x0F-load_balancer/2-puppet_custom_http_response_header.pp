# Define a class to configure the custom HTTP response header
class custom_http_response_header {

  # Install package nginx
  package { 'nginx':
    ensure => installed,
  }

  # Define a custom fact to get the hostname of the server
  Facter.add('server_hostname') do
    setcode 'hostname'
  end

  # Define nginx configuration file
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    # Add custom HTTP response header
    add_header X-Served-By $::server_hostname;
}
",
    require => Package['nginx'],
  }

  # Restart nginx service
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

# Apply the class to configure the custom HTTP response header
include custom_http_response_header

