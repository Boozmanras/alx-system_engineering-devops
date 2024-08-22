#Adjust the operating system settings so that the 'holberton' user can log in and access files without any errors

exec { 'Enhance the file limit settings for the 'holberton' user':

  command => 'sed -i "/holberton hard/s/4/50000/" /etc/security/limits.conf',

  path    => '/usr/local/bin/:/bin/'

}


exec { 'Raise the soft file limit for the 'holberton' user':

  command => 'sed -i "/holberton soft/s/5/50000/" /etc/security/limits.conf',

  path    => '/usr/local/bin/:/bin/'

}
