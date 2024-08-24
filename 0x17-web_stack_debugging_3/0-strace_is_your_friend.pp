# This manifest fixes the Apache 500 error by ensuring the correct PHP module is enabled and Apache is correctly configured.

exec { 'enable-php5-module':
  command => '/usr/sbin/a2enmod php5',
  path    => ['/usr/bin', '/usr/sbin'],
  onlyif  => 'test ! -f /etc/apache2/mods-enabled/php5.load',
  notify  => Exec['restart-apache'],
}

exec { 'restart-apache':
  command     => '/usr/sbin/service apache2 restart',
  path        => ['/usr/bin', '/usr/sbin'],
  refreshonly => true,
}

exec { 'check-apache-status':
  command => 'curl -o /dev/null -s -w "%{http_code}" http://localhost/index.php | grep -q "^200$"',
  path    => ['/usr/bin', '/usr/sbin'],
  require => Exec['restart-apache'],
}
