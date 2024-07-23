# 100-puppet_ssh_config.pp

file { 'ssh_config':
    ensure  => 'file',
    path    => '/root/.ssh/config',
    content => template('ssh/client_config.erb'),
    mode    => '0600',
}

file { 'Turn off passwd auth':
    ensure  => 'present',
    path    => '/root/.ssh/config',
    line    => '    PasswordAuthentication no',
    match   => '^.*PasswordAuthentication.*$',
}

file { 'Declare identity file':
    ensure  => 'present',
    path    => '/root/.ssh/config',
    line    => '    IdentityFile ~/.ssh/school',
    match   => '^.*IdentityFile.*$',
}

file { 'Set user':
    ensure  => 'present',
    path    => '/root/.ssh/config',
    line    => '    User ubuntu',
    match   => '^.*User.*$',
}

