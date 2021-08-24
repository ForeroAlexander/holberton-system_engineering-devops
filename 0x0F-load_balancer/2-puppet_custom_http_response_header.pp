# creating a custom HTTP header response, but with Puppet.
# -The name of the custom HTTP header must be X-Served-By
# -The value of the custom HTTP header must be the hostname
# of the server Nginx is running on
# -Write 2-puppet_custom_http_response-header.pp so that
# it configures a brand new Ubuntu machine to the requirements asked in this task

exec {'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

package {'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file_line {'response_header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => "add_header X-Served-By ${hostname};",
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => File_line['response_header'],
}
