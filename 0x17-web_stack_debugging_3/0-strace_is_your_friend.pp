# Corrects phpp extension for php
exec {'phppFix':
    path    => '/bin',
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
