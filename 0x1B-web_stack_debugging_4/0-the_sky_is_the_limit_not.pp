#Configuring NGiX to accept more traffic

exec('configure maximum open files allowance': command ='sed-i"s/15/4096"/etc/default/nginx/restart',
path => 'usr/local/sbin:/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
} 
