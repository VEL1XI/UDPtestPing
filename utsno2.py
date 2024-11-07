import socket
import time


SERVER_IP = '127.0.0.1'  
SERVER_PORT = 12000          
PING_COUNT = 10               


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)  

for i in range(1, PING_COUNT + 1):
    message = f'Ping {i} {time.time()}'.encode()

    try:

        start_time = time.time()
        client_socket.sendto(message, (SERVER_IP, SERVER_PORT))
        response, addr = client_socket.recvfrom(1024)
        end_time = time.time()
        rtt = end_time - start_time
        print(f'Ping {i}: RTT = {rtt:.4f} seconds')
    except socket.timeout:
        print(f'Ping {i}: Request timed out')


client_socket.close()

# import socket
# import time

# # Detail server (sesuaikan jika diperlukan)
# SERVER_IP = '127.0.0.1'  # Alamat server
# SERVER_PORT = 12000      # Port yang digunakan server

# # Membuat socket UDP
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(1)  # Menetapkan waktu tunggu 1 detik

# i = 1  # Inisialisasi hitungan ping

# while True:
#     # Mempersiapkan pesan ping
#     message = f'Ping {i} {time.time()}'.encode()

#     try:
#         # Merekam waktu pengiriman ping 
#         start_time = time.time()
        
#         # Mengirim pesan ke server
#         client_socket.sendto(message, (SERVER_IP, SERVER_PORT))
        
#         # Menunggu balasan
#         response, addr = client_socket.recvfrom(1024)
        
#         # Merekam waktu penerimaan pong dan menghitung RTT
#         end_time = time.time()
#         rtt = end_time - start_time
        
#         # Mencetak hasil
#         print(f'Ping {i}: RTT = {rtt:.4f} seconds')
    
#     except socket.timeout:
#         # Jika tidak ada balasan dalam 1 detik, anggap paket hilang
#         print(f'Ping {i}: Request timed out')

#     # Increment ping count
#     i += 1
#     time.sleep(1)  # Optional delay between pings for readability

# # Menutup socket
# # client_socket.close()
