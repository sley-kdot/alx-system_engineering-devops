# install nginx web server with pupper

package { 'nginx':
    ensure => installed,
    name   => 'nginx',
}

exec { 'installer':
  command   => 'sudo apt -y update; sudo apt -y install nginx',
  provider  => shell,
}

exec { 'page':
  command  => "echo 'Hello World!' | sudo tee /var/www/html/index.html > /dev/null",
  provider => shell,
}
