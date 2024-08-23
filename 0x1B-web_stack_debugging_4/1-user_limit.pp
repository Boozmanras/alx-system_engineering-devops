# This Puppet manifest adjusts the file limit settings for the 'holberton' user to ensure proper login and file access without issues.

exec { 'Enhance the hard file limit settings for holberton user':
  command => "sed -i '/^holberton.*hard.*nofile/s/[0-9]\+/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin:/usr/bin',
}

exec { 'Raise the soft file limit for holberton user':
  command => "sed -i '/^holberton.*soft.*nofile/s/[0-9]\+/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin:/usr/bin',
}
