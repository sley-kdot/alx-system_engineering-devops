# install nginx web server with pupper

package { 'nginx':
    ensure => installed;
      name => 'nginx';
  provider => 'apt';
}

exec { 'listen on port 80':
  command => "sudo ufw allow 'Nginx HTTP'",
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}
