import psutil
import time
import os
import shutil

def format_bytes(bytes_num):
    """Convert bytes to a readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_num < 1024.0:
            return f"{bytes_num:.2f} {unit}"
        bytes_num /= 1024.0
    return f"{bytes_num:.2f} PB"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text, width):
    """Center the text within the given width"""
    return text.center(width)

def monitor_network():
    print("Starting real-time network monitor (press Ctrl+C to stop)...")
    
    # Get terminal width
    terminal_width = shutil.get_terminal_size().columns

    old_stats = psutil.net_io_counters()
    while True:
        time.sleep(1)
        new_stats = psutil.net_io_counters()

        bytes_sent = new_stats.bytes_sent
        bytes_recv = new_stats.bytes_recv
        packets_sent = new_stats.packets_sent
        packets_recv = new_stats.packets_recv

        sent_per_sec = bytes_sent - old_stats.bytes_sent
        recv_per_sec = bytes_recv - old_stats.bytes_recv
        psent_per_sec = packets_sent - old_stats.packets_sent
        precv_per_sec = packets_recv - old_stats.packets_recv

        clear()
        # Print the header centered
        print(center_text("=== Real-Time Network Usage ===", terminal_width))
        print(center_text(f"Total Bytes Sent:     {format_bytes(bytes_sent)}", terminal_width))
        print(center_text(f"Total Bytes Received: {format_bytes(bytes_recv)}", terminal_width))
        print(center_text(f"Packets Sent:         {packets_sent}", terminal_width))
        print(center_text(f"Packets Received:     {packets_recv}", terminal_width))
        print()
        print(center_text(f"Sent/sec:     {format_bytes(sent_per_sec)}", terminal_width))
        print(center_text(f"Received/sec: {format_bytes(recv_per_sec)}", terminal_width))
        print(center_text(f"Packets Sent/sec:     {psent_per_sec}", terminal_width))
        print(center_text(f"Packets Received/sec: {precv_per_sec}", terminal_width))

        old_stats = new_stats

if __name__ == "__main__":
    try:
        monitor_network()
    except KeyboardInterrupt:
        print("\nStopped network monitor.")
