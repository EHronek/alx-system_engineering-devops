 # Fixes bug in my wordpress file

 exec { 'wordpress_fix':
   command => 'sed -i s/phpp/php/g /var/www/html/wp-setting.php',
   path    => '/usr/local/bin:/bin'
}
