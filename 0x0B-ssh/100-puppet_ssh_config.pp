#set up coniguration file so that you can connect to a server
# without typing a password
exec { 'echo':
  path    => 'usr/bin:/bin',
  command => 'echo " IdentityFile ~/.ssh/schoo\n PasswordAuthentication no" >> /etc/ssh/ssh_config',
  returns => [0, 1],
}
