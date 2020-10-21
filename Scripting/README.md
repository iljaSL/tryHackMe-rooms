<p align="center">
    <img src="https://github.com/iljaSL/tryHackMe-rooms/blob/main/Scripting/images/room_picture.png" alt="Logo" width="600" height="150">
</p>

## Task 1: [Base64](https://github.com/iljaSL/tryHackMe-rooms/tree/main/Scripting/Base64)

#### The file b64.txt has been base64 encoded 50 times - write a script to retrieve the flag. Try do this in both Bash and Python!

I wrote both the [python](https://github.com/iljaSL/tryHackMe-rooms/blob/main/Scripting/Base64/decoder.py) and the [bash](https://github.com/iljaSL/tryHackMe-rooms/blob/main/Scripting/Base64/decoder.sh) script. Excuting the scripts result in the following answer <br>

Task 1 Flag: `HackBack2019`

#### How to run the scripts
Python: `python3 decoder.py b64.txt`<br>
Bash: `./decoder.sh`

## Task 2: [Gotta Catch em All](https://github.com/iljaSL/tryHackMe-rooms/tree/main/Scripting/GottaCatchEmAll)

#### You need to write a script that connects to this webserver on the correct port, do an operation on a number and then move onto the next port. Start your original number at 0. The format is: operation, number, next port. For example the website might display, add 900 3212 which would be: add 900 and move onto port 3212. Then if it was minus 212 3499, you'd minus 212 (from the previous number which was 900) and move onto the next port 3499. Do this until you the page response is STOP (or you hit port 9765). Each port is also only live for 4 seconds. After that it goes to the next port. You might have to wait until port 1337 becomes live again... Go to: http://<machines_ip>:3010 to start...

1. Inside the while loop in the main function, I try to connect until port 1337 is available.

2. If it becomes available, I use the python socket librarie to connect to the server.

3. Sending a GET request to the server ip with the server port.

4. Retrieve the data from the request inside a while loop.

5. Assign the data from the HEADER inside the assign_data function into usable variables.

6. Do the calcualtion request by the task.

7. Output the current number and moving on to the next port.

8. The port will be updated every 4 seconds.

9. This will be done until the script hits the port 9765 OR until the page response is STOP, which will trigger the answer/

And the answer is: `344769.12`


## Task 3: [Encrypted Server Chit Chat](https://github.com/iljaSL/tryHackMe-rooms/blob/main/Scripting/encrypted_server_chit_chat/decrypt_chat.py)

#### The VM you have to connect to has a UDP server running on port 4000. Once connected to this UDP server, send a UDP message with the payload "hello" to receive more information. You will find some sort of encryption(using the AES-GCM cipher). Using the information from the server, write a script to retrieve the flag. Here are some useful thingsto keep in mind:

#### * sending and receiving data over a network is done in bytes.
#### * the PyCA encryption library and functions takes its inputs as bytes.
#### * AES GCM sends both encrypted plaintext and tag, and the server sends these values sequentially in the form of the encrypted plaintext followed by the tag.

1. Connect to the server ip (deployed on tryhackme) via UDP and send a message to get further instructions
this is what we get `You've connected to the super secret server, send a packet with the payload ready to receive more information`

2. After sending another message with the payload 'ready' we get the following response back
`to decrypt and find the flag that has a SHA256 checksum of ]w\xf0\x18\xd2\xbfwx`T\x86U\xd8Ms\x82\xdc'\xd6\xce\x81n\xdeh\xf6]rb\x14c\xd9\xda send final in the next payload to receive all the encrypted flags`

3. the checksum will be converted to hex to make the comparison easier.

4. Entering the loop until we get a checksum match, decryption happens with the AES GCM decryptor.

After a successful run, we get the following flag from the server:

`THM{eW-sCrIpTiNg-AnD-cRyPtO}`

### Resources

[All about the Python sockets library](https://realpython.com/python-sockets/) <br>
[Python f-strings](https://realpython.com/python-f-strings/)  <br>
[Symmetric encryption](https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/)  <br>
[Pythons hashlib library](https://docs.python.org/3/library/hashlib.html)  <br>
[Python b-string](https://www.studytonight.com/post/significance-of-prefix-b-in-a-string-in-python)  <br>
[AES GCM](https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/symmetric-key-ciphers/aes-encrypt-decrypt-examples.html)
