# installs flask from pip3 using Puppet

package { 'Flask':
 ensure   => '2.1.1',
 provider => 'pip3',
}
