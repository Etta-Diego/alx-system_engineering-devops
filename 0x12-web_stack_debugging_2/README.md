0x12-web_stack_debugging_2/

The user root is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the root user, as if you fat finger a command and for example run rm -rf /, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the root user can do, just need to use a specific command that you need to discover.

The root user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as root. With this in mind, it’s a good practice not to run your web servers as root (which is the default for most configurations) and instead run the process as the less privileged nginx user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the nginx user.

Files
0-iamsomeoneelse
This file contains a Bash script that accepts one argument
The script runs the whoami command under the user passed as an argument

1-run_nginx_as_nginx
This file contains a bash script that configures nginx to run as nginx user
and also to listen to all active IPs on port 8080

100-fix_in_7_lines_or_less
This file does same as 1-run_nginx_as_nginx but this time with shorter lines of code.
