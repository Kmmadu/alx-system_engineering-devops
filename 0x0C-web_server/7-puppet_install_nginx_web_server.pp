# Setup nginx server

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => '    location /redirect_me/ { return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4; }',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

