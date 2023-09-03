import socket
import time

def speedtest(server,port):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        try:
            s.connect((server,port))
        except:
            print('Failed')
            return None

        end_time=time.time()
        elapsed_time=end_time-start_time
    download_speed=(1/elapsed_time)*8
    return download_speed

start_time=time.time()
download_speed=speedtest('192.168.1.1',80)
if download_speed is not None:
    print(f"{download_speed} Mbps")