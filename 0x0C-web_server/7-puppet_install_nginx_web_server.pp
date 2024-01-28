# install nginx web server with pupper

package { 'nginx':
    ensure => installed,
      name => 'nginx',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}
