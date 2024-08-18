# Puppet manifest to install and configure Nginx

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
}

# Create a custom index.html page with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure Nginx to listen on port 80 and set up redirection
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Template content (nginx/default.erb)
file_line { 'listen_80':
  path  => '/etc/nginx/sites-available/default',
  line  => 'listen 80;',
  match => '^listen',
}

file_line { 'redirect_me':
  path  => '/etc/nginx/sites-available/default',
  line  => '    location /redirect_me {\n        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n    }',
  match => 'location /redirect_me',
}

file_line { 'index_root':
  path  => '/etc/nginx/sites-available/default',
  line  => 'root /var/www/html;',
  match => '^root',
}

