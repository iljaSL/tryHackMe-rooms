<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-24%20at%205.38.43%20PM.png" alt="Logo" width="1000" height="200">
</p>

# Table of contents

- [Task](#task)
- [Enumaration](#enumaration)

## Task

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-24%20at%205.39.27%20PM.png" alt="Logo" width="1100" height="300">
</p>

## Enumaration

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

The next step would be to check out the folder sturcture of the website with dirbuster, maybe we can find some usefull files as well.
After running successfully dirbuster, we get some interesting files listed inside the webstes folder structure. 

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-24%20at%205.24.37%20PM.png" alt="Logo" width="500" height="200">
</p>

It seems like the website has been set up with WordPress. We need to gain somehow access to Wordpress, let’s try something trivial.

`Username: admin` <br>
`Password: admin`

It did not work, but we got a clue from the error message, that the user admin does not exist, I tried it with root and we get the same result.

Coming back to our dirbuster result, we still have some text files that we need to check for some more clues or even a valid user that we can use to login into wordpress.


to be continued...


