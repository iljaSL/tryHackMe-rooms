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

First I check with nmap which ports are open and what kind of OS I'm dealing with. 

`npm -A -p- <machine ip>`

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-24%20at%203.35.56%20PM.png" alt="Logo" width="1100" height="500">
</p>

2 ports are open and 1 closed, usually the reason a port will appear as closed is that there is no service listening on it and the firewall is not filtering access to the port.
The machine is running a Apache server on Port 80. So lets check out the Machine IP with the port inside a web browser out.

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-24%20at%203.38.52%20PM.png" alt="Logo" width="1100" height="500">
</p>

It seems like the website is having a built in terminal. It's not possible though to use any known unix commands inside the terminal expect the one listed under 'commands'.
Using those commands will triger some videos.

Let's check out the dir sturcture of the website out with dirbuster. Maybe we can find some usefull files as well.
After running dirbuster, we get some interesting files listed in the folder structure. 

<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/MrRobotCTF/images/Screen%20Shot%202020-10-24%20at%205.24.37%20PM.png" alt="Logo" width="1000" height="600">
</p>

The first obvious hint we have is that the website is set up with WordPress. We will come back to that later...

to be continued...


