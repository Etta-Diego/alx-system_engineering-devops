0x13-firewall

Concepts
For this project, we will look at this concept:

Web stack debugging

Files

0-block_all_incoming_traffic_but:
This file contains the ufw commands that is used to configure ufw so that it blocks all incoming traffic, except the following TCP ports:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)

100-port_forwarding
This file contains copy of the ufw configuration file that was used to configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.
