<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-24%20at%205.38.43%20PM.png" alt="Logo" width="1000" height="200">
</p>

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-24%20at%205.39.27%20PM.png" alt="Logo" width="1100" height="300">
</p>

Let's begin with the enumaration! First I will check with nmap, which ports are open and what kind of OS I'm dealing with. 

`npm -A -p- <machine ip>`

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-24%20at%203.35.56%20PM.png" alt="Logo" width="550" height="250">
</p>

2 ports are open, 1 closed and it look likes the OS of the target machine is Linux, usually the reason a port will appear as closed is that there is no service listening on it and the firewall is not filtering access to the port.
The Linux machine is running an Apache server on Port 80. Let's check out the <MachineIP:Port> inside the web browser.

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-24%20at%203.38.52%20PM.png" alt="Logo" width="550" height="250">
</p>

It seems like the website is having a built in terminal. It's not possible though to use any known unix commands inside the terminal expect the one listed under 'commands'.
Using those commands will triger some videos.

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-30%20at%201.09.22%20PM.png" alt="Logo" width="550" height="450">
</p>

The next step would be to check out the folder sturcture of the website with dirbuster, maybe we can find some usefull files as well.
After running successfully dirbuster, we get some interesting files listed inside the webstes folder structure. 

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-24%20at%205.24.37%20PM.png" alt="Logo" width="500" height="200">
</p>

It seems like the website has been set up with WordPress. We need to gain somehow access to Wordpress, let’s try something trivial.

`Username: admin` <br>
`Password: admin`

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-30%20at%201.55.10%20PM.png" alt="Logo" width="250" height="250">
</p>

It did not work, but we got a clue from the error message, that the user admin does not exist, I tried it with root and we get the same result.

Coming back to our dirbuster result, we still have some text files that we need to check for some more clues or even a valid user that we can use to login into wordpress. 
We can't reach the text files inside the wp-login directorie yet, license.txt does not have any new clues either, but robots.txt looks really promising!

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-24%20at%204.00.51%20PM.png" alt="Logo" width="600" height="250">
</p>

Let's get those two files on our system with wget. Bingo! There is the first key!

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-30%20at%201.14.32%20PM.png" alt="Logo" width="250" height="60">
</p>

The content of fsocity.dic (dictionary file) includes random data, to be more specific it looks like it is a wordlist wiht over 85000 words. 
Which can maybe include a user and password for the Wordpress site, let's brute force it with Hydra.

The command: `hydra -L fsocity.dic -p test 10.10.36.214 http-post-form "/wp-login.php:log=^USER^&pwd=^PWD:Invalid username" -t 30`

and we got the password! `ER28–****`

Let's try and log in into wordpress.

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-11-22%20at%207.01.25%20PM.png" width="800" height="400">
</p>

It worked!

Unfortunately there is not much valuable information inside the wordpress panel, but we have access to the appearances and with the admin rights we can actually update them and with the help of the listed tutorial we can get a reverse shell to the server! <br>

[Reverse-shell-tutorial](https://www.hackingarticles.in/wordpress-reverse-shell/) <br>
[Pentestmonkey-tutorial](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php
) <br>
[Pentestmoneky-PHP-sources-code](http://pentestmonkey.net/tools/web-shells/php-reverse-shell) <br>

Now I include the code from pentestmonkey inside the 404.php appearance site, set up the `nc` command and listen to the port I include inside the code, go to `<target-ip>/404.php` and the reverse shell was a success!

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-11-22%20at%207.45.17%20PM.png" width="800" height="300">
</p>

We can upgrade now the simple shell with this great tutorial found here [Ropnop Blog](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/).

We are at the momemt inside the machine with the user daeamon, but there is another user called robot and by checking his home directorie we finnaly found the second flag!
BUT we don't have the permission to read the file, it's nice that robot provides us his hashed password inside a file though. 

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-11-22%20at%207.49.31%20PM.png" width="800" height="200">
</p>

Let's crack the md5 hashed password, we can do that with Hashcat or an online cracker.

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-11-22%20at%207.53.31%20PM.png" width="1400" height="200">
</p>

We cracked the password! And the way is cleared in order to get the second flag.

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-11-22%20at%208.00.20%20PM.png" width="800" height="500">
</p>

After going through the directories with the user robot without any promising weakness, we can try out to spot any possibilities to gain root access, which would be as well the next logical step. There are many possibilities to  check for privilege escalation. I'm gonna try it out first with LinEnum. We can download it to the target machine by creating a simple python http server and using wget.

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/linenum-Download.png" width="1400" height="200">
</p>

After running LinEnum.sh, we get a huge log printed with lots of information.
