# kill a program called killmenow
exec { 'conejo':
  path     => ['/usr/bin'],
  command  => 'pkill -f killmenow',
  provider => 'shell'
}
