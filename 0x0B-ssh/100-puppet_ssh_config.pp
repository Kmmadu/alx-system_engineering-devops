# Your SSH client configuration must be configured
# to use the private key ~/.ssh/school

include stdlib

file_line { 'New private key holder':
  ensure             => present,
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^IdentityFile',
  append_on_no_match => true,
}

file_line { 'No password':
  ensure             => present,
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^PasswordAuthentication',
  append_on_no_match => true,
}

