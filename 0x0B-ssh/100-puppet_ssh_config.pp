#!/usr/bin/env bash
#4. Client configuration file (w/ Puppet)

file_line { 'Identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
}

file_line { 'No Password needed':
  path    => '/etc/ssh/ssh_config',
  line    => 'No PasswordAuthentication',
}
