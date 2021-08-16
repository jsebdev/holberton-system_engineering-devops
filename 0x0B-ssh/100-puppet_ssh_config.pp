#set ssh key
include stdlib
file_line { 'replace a line':
  ensure  => present,
  path    => 'cosas raras',
  match   => '^incredible'
}
