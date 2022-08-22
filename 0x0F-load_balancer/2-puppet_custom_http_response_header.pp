#Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'update':
    command  => 'sudo apt-get update',
    provider => shell,
}

exec { 'install nginx':
    command  => 'sudo apt-get -y install nginx',
    provider => shell,
    require  => Exec['update'],
}

exec { 'response header':
    command  => "sudo sed -i '/server_name _;/a add_header X-Served-By '$HOSTNAME';' /etc/nginx/sites-available/default",
    provider => shell,
    require  => Exec['install nginx'],
}

exec { 'restart nginx':
    command  => 'sudo service nginx restart',
    provider => shell,
}
