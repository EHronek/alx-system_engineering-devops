# script o fix an error in afile in my server

exec { 'fix an error in my file':
  command => 'test -f /var/www/html/wp-settings.php && sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin:/bin',
}
