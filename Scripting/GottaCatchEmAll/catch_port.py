import socket
import time
import re
import sys

def Main():
    host = sys.argv[1]
    port = 1337
    start_number = 0

    while port != 9765:
        try:
            s = socket.socket()
            s.connect((host,port))
            request = f"GET / HTTP/1.0\r\nHost: {host}:{port}\r\n\r\n"
            s.send(request.encode())

            while True:
                response = s.recv(1024)
                if (len(response) < 1):
                    break
                data = response.decode()

            operator, new_number, next_port = assign_data(data)
            start_number = do_operation(operator, start_number, new_number)
            print(f"Current number: {start_number}, next port: {next_port}")
            port = next_port

            s.close()

        except:
            s.close()
            time.sleep(3)
            pass

    print(f"The final answer is {round(start_number,2)}")

def do_operation(operator, start_number, new_number):
    if operator == 'add':
        return start_number + new_number
    elif operator == 'minus':
        return start_number - new_number
    elif operator == 'divide':
        return start_number / new_number
    elif operator == 'multiply':
        return start_number * new_number
    else:
        return None

def assign_data(data):
    data_array = re.split(' |\*|\n', data)
    data_array = list(filter(None, data_array))
    operator = data_array[-3]
    new_number = float(data_array[-2])
    next_port = int(data_array[-1])

    return operator, new_number, next_port

if __name__ == '__main__':
    Main()