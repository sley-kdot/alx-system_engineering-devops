# client-side configuration with puppet

file_line {'make use of private key':
  ensure => present,
  path   => '/etc/ssh/ssh-config',
  line   => 'IdentityFile ~/.ssh/school',
}

file_line {'refuse to authenticate using a passwd':
  ensure => present,
  path   => '/etc/ssh/ssh-config',
  line   => 'PasswordAuthentication',
}
