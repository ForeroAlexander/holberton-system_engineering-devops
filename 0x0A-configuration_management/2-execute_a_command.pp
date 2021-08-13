#pkill
exec { 'killmenow':
    command => '/usr/bin/pkill killmenow',
}
