###0x1A. Application server

*This project adds an application server to a web stack infrastructure, it plugs it to the Nginx and make it to serve the Airbnb clone project.*

- First, I set up the development environment  with Python, which is used for testing and debugging the code before deploying it to production.

This I did by installing the net-tools package on the server: sudo apt install -y net-tools

Then, I configured the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.


- Next, I set up the production application server with Gunicorn, port 5000. 

This I did by installing Gunicorn and any other libraries required by your application.

Then, I bind the Gunicorn instance to localhost listening on port 5000 with the application object as the entry point.


- Next, I configured Nginx to serve the page fromreboot your server (by using the command $ sudo reboot) to have Nginx publicly accessible the route /airbnb-onepage/ with the following requirements:

	- Nginx must serve this page both locally and on its public IP on port 80.
	
	- Nginx should proxy requests to the process listening on port 5000.

	- Include your Nginx config file as 2-app_server-nginx_config.


I tested this by spining up the production application server (listening on port 5000)

I rebooted the server (by using the command $ sudo reboot) to have Nginx publicly accessible
