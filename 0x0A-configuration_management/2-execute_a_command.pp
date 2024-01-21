#This script kills a process name killmenow using puppet

exec { 'pkill':
  command => '/bin/pkill killmenow',
}
