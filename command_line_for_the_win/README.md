COMMAND LINE FOR THE WIN

How I Used SFTP to Transfer Screenshots From my Local Machine to  the Sandbox Environment.


1. First, I cloned my repo in the sandbox environment and created the command_line_for_the_win directory, afterwards, I opened a terminal on my local machine and created a key pair using this command:

ssh-keygen

I got this output:

Generating public/private rsa key pair.
Enter file in which to save the key (/home/my_username/.ssh/id_rsa):

Then I entered this directory to save the key pair:

home/my_username/.ssh/id_rsa

This caused the prompt:

Enter passphrase (empty for no passphrase):

I entered a passphrase.


2. Next, I copied the public key to my local machine using SSH with this syntax:

cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && touch ~/.ssh/authorized_keys && chmod -R go= ~/.ssh && cat >> ~/.ssh/authorized_keys"


I entered yes to the output text that is similar to this:

The authenticity of host '203.0.113.1 (203.0.113.1)' can't be established.
ECDSA key fingerprint is fd:fd:d4:f9:77:fe:73:84:e1:55:00:ad:d6:6d:22:fe.
Are you sure you want to continue connecting (yes/no)?


Then, I entered the password in a prompt similar to this:

username@203.0.113.1's password:


3.  I entered the SSH of the sandbox environment which looked like this:  

ssh sandbox&username@remote_host(sandbox)


I was successfully logged into the sandbox environment.


4. Afterwards, I exited the SSH using:

exit

5. I copied the sandbox SFTP which looks similar to this syntax:

sftp username@remote_hostname 

6. Afterwards, I navigated to the command_line_for_the_win directory on the sandbox environment that is the directory where I wanted to transfer the file using these commands:

pwd
ls
cd /root/alx-system_engineering-devops/command_line_for_the_win/

7. Next, I navigated to the directory in my local machine using where the screenshot was saved using these commands:

lpwd
lls
lcd
/mnt/c/HP/Pictures/Screenshots

5. I uploaded each of the files from my local machine to the sandbox using this command:
   
   put 0-first_9_tasks.png
   put 1-next_9_tasks.png
   put 2-next_9_tasks.png
   

6. I verified the file transfer, by listing the contents of the command_line_for_the_win directory as thus:

ls

7. Finally, I exited the SFTP session:
   
exit


 Helpful Resources 

SFTP commands:
https://www.hostinger.com/tutorials/how-to-use-sftp-to-safely-transfer-files/

https://www.uppmax.uu.se/support/user-guides/basic-sftp-commands/

For SFTP connection:
https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server

For SSH connection:
https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-20-04
