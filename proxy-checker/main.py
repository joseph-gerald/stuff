from colorama import init, Fore, Style
from rgbprint import gradient_print, Color
from concurrent.futures import ThreadPoolExecutor
import threading
import tester
import time
import os

init(autoreset=True)

proxies_checked = 0
working_proxies = 0
dead_proxies = 0
start_time = time.time()
proxies_list = []

print_lock = threading.Lock()

def set_title(title):
    os.system(f"title {title}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_colored_timestamp():
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    timestamp_parts = timestamp.split(':')
    return (
        Fore.LIGHTBLACK_EX + timestamp_parts[0] + ':' +
        Fore.LIGHTBLACK_EX + timestamp_parts[1] + ':' +
        Fore.LIGHTBLACK_EX + timestamp_parts[2] + Fore.RESET
    )

def update_stats():
    global proxies_checked, working_proxies, dead_proxies, proxies_list, start_time
    elapsed_time = time.time() - start_time
    cpm = int((proxies_checked / elapsed_time) * 60) if elapsed_time > 0 else 0
    percentage_working = (working_proxies / proxies_checked) * 100 if proxies_checked > 0 else 0
    with print_lock:
        set_title(f"Hacker Tool - Checked: {proxies_checked}/{len(proxies_list)} - WORKING: {working_proxies} - DEAD: {dead_proxies} - {percentage_working:.2f}% - CPM: {cpm}")

clear_screen()

gradient_print(
    """
         __    __   ______    ______   __    __        ________  ______    ______   __       
        /  |  /  | /      \  /      \ /  |  /  |      /        |/      \  /      \ /  |      
        $$ |  $$ |/$$$$$$  |/$$$$$$  |$$ | /$$/       $$$$$$$$//$$$$$$  |/$$$$$$  |$$ |      
        $$ |__$$ |$$ |__$$ |$$ |  $$/ $$ |/$$/           $$ |  $$ |  $$ |$$ |  $$ |$$ |      
        $$    $$ |$$    $$ |$$ |      $$  $$<            $$ |  $$ |  $$ |$$ |  $$ |$$ |      
        $$$$$$$$ |$$$$$$$$ |$$ |   __ $$$$$  \           $$ |  $$ |  $$ |$$ |  $$ |$$ |      
        $$ |  $$ |$$ |  $$ |$$ \__/  |$$ |$$  \          $$ |  $$ \__$$ |$$ \__$$ |$$ |_____ 
        $$ |  $$ |$$ |  $$ |$$    $$/ $$ | $$  |         $$ |  $$    $$/ $$    $$/ $$       |
        $$/   $$/ $$/   $$/  $$$$$$/  $$/   $$/          $$/    $$$$$$/   $$$$$$/  $$$$$$$$/ 

        By The Hacker Tool Maker Developer XX @hacker on Telegram
    """,
    start_color=Color.yellow_green,
    end_color=Color.dark_magenta
)

print(f"""
    {Style.BRIGHT}Choose a tool to run:{Style.RESET_ALL}

    {Style.BRIGHT}{Fore.LIGHTBLACK_EX}1. {Style.RESET_ALL}Light Proxy checker
    {Style.BRIGHT}{Fore.LIGHTBLACK_EX}2. {Style.RESET_ALL}Heavy Proxy checker
    {Style.BRIGHT}{Fore.LIGHTBLACK_EX}3. {Style.RESET_ALL}Residential Proxy checker
""")

tool_choice = input(f"    {Style.BRIGHT}{Fore.LIGHTBLACK_EX}>{Style.RESET_ALL} ")

if tool_choice not in ["1", "2", "3"]:
    print(f"    {Style.BRIGHT}{Fore.RED}ERROR{Style.RESET_ALL} Invalid tool choice.")
    exit()

clear_screen()

print(f"""
    {Style.BRIGHT}Enter the path to the proxy list (empty = proxies.txt):{Style.RESET_ALL}
""")

proxy_list_path = input(f"    {Style.BRIGHT}{Fore.LIGHTBLACK_EX}>{Style.RESET_ALL} ")

if proxy_list_path == "":
    proxy_list_path = "proxies.txt"

if not os.path.exists(proxy_list_path):
    print(f"    {Style.BRIGHT}{Fore.RED}ERROR{Style.RESET_ALL} The file {proxy_list_path} does not exist.")
    exit()

with open(proxy_list_path, "r") as f:
    proxies_list = [line.strip() for line in f]

print(f"""
    {Style.BRIGHT}Enter the path to the output file (empty = output-[date].txt):{Style.RESET_ALL}
""")

output_file_path = input(f"    {Style.BRIGHT}{Fore.LIGHTBLACK_EX}>{Style.RESET_ALL} ")

if output_file_path == "":
    output_file_path = f"output-{time.strftime('%Y-%m-%d %H-%M-%S')}.txt"

if not os.path.exists("output"):
    os.mkdir("output")

output_file_path = os.path.join("output", output_file_path)

clear_screen()

print(f"""
    {Style.BRIGHT}How many threads do you want to use?{Style.RESET_ALL}
""")

thread_count = input(f"    {Style.BRIGHT}{Fore.LIGHTBLACK_EX}>{Style.RESET_ALL} ")

if not thread_count.isdigit():
    print(f"    {Style.BRIGHT}{Fore.RED}ERROR{Style.RESET_ALL} Please enter a number.")
    exit()

clear_screen()

tool_name = ["Light Proxy Checker", "Heavy Proxy Checker", "Residential Proxy Checker"][int(tool_choice) - 1]

print(f"""
    {(Fore.LIGHTBLACK_EX + "- " + Style.RESET_ALL + "- ")*18}
    -
    {Fore.LIGHTBLACK_EX}-  {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}IN:{Style.RESET_ALL} {proxy_list_path}{Style.RESET_ALL}
    -  {Style.BRIGHT}{Fore.LIGHTBLACK_EX}OUT:{Style.RESET_ALL} {output_file_path}{Style.RESET_ALL}
    {Fore.LIGHTBLACK_EX}-  {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}COUNT:{Style.RESET_ALL} {len(proxies_list)}{Style.RESET_ALL}
    -  {Style.BRIGHT}{Fore.LIGHTBLACK_EX}MODE:{Style.RESET_ALL} {tool_name}{Style.RESET_ALL}
    {Fore.LIGHTBLACK_EX}-  {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}THREADS:{Style.RESET_ALL} {thread_count}{Style.RESET_ALL}
    - 
    {(Fore.LIGHTBLACK_EX + "- " + Style.RESET_ALL + "- ")*18}
""")

def light_job(proxy):
    global proxies_checked, working_proxies, dead_proxies
    proxy_ip, working = tester.ip_check(proxy)

    if working:
        with open(output_file_path, "a") as f:
            f.write(proxy + "\n")

        with open(output_file_path + ".csv", "a") as f:
            f.write(f"{proxy_ip},{proxy.strip()}\n")

        with print_lock:
            print(f"{get_colored_timestamp()} - {Style.BRIGHT}{Fore.GREEN}WORKING{Style.RESET_ALL} {proxy.strip()}")

        working_proxies += 1
    else:
        with print_lock:
            print(f"{get_colored_timestamp()} - {Style.BRIGHT}{Fore.RED}DEAD{Style.RESET_ALL} {proxy.strip()}")
        dead_proxies += 1

    proxies_checked += 1
    update_stats()

def heavy_job(proxy):
    global proxies_checked, working_proxies, dead_proxies
    proxy_ip, fraud_score = tester.get_fraud_score(proxy)

    if fraud_score != -1:
        with open(output_file_path, "a") as f:
            f.write(f"{proxy.strip()}\n")

        with open(output_file_path + ".csv", "a") as f:
            f.write(f"{proxy_ip},{proxy.strip()},{fraud_score}\n")

        with print_lock:
            print(f"{get_colored_timestamp()} - {Style.BRIGHT}{Fore.GREEN}WORKING{Style.RESET_ALL} {proxy.strip()} {fraud_score}")

        working_proxies += 1
    else:
        with print_lock:
            print(f"{get_colored_timestamp()} - {Style.BRIGHT}{Fore.RED}DEAD{Style.RESET_ALL} {proxy.strip()}")
        dead_proxies += 1

    proxies_checked += 1
    update_stats()

def resi_job(proxy):
    global proxies_checked, working_proxies, dead_proxies
    proxy_ip, residential = tester.resi_check(proxy)

    if residential:
        with open(output_file_path, "a") as f:
            f.write(proxy + "\n")

        with open(output_file_path + ".csv", "a") as f:
            f.write(f"{proxy_ip},{proxy.strip()}\n")

        with print_lock:
            print(f"{get_colored_timestamp()} - {Style.BRIGHT}{Fore.GREEN}RESIDENTIAL{Style.RESET_ALL} {proxy.strip()}")

        working_proxies += 1
    else:
        with print_lock:
            print(f"{get_colored_timestamp()} - {Style.BRIGHT}{Fore.RED}NON-RESI{Style.RESET_ALL} {proxy.strip()}")
        dead_proxies += 1

    proxies_checked += 1
    update_stats()

set_title("Hacker Tool - Starting...")

match tool_choice:
    case "1":
        with ThreadPoolExecutor(max_workers=int(thread_count)) as executor:
            for proxy in proxies_list:
                executor.submit(light_job, proxy)
    case "2":
        with ThreadPoolExecutor(max_workers=int(thread_count)) as executor:
            for proxy in proxies_list:
                executor.submit(heavy_job, proxy)

    case "3":
        with ThreadPoolExecutor(max_workers=int(thread_count)) as executor:
            for proxy in proxies_list:
                executor.submit(resi_job, proxy)

    case _:
        print(f"    {Style.BRIGHT}{Fore.RED}ERROR{Style.RESET_ALL} Invalid tool choice.")
        exit()

set_title("Hacker Tool - Finished")

print("\n" + "\t" + Style.BRIGHT + Fore.CYAN + "--- Summary ---" + Style.RESET_ALL)
print("\t" + f"{Style.BRIGHT}Total Proxies Checked:{Style.RESET_ALL} {proxies_checked}")
print("\t" + f"{Style.BRIGHT}Working Proxies:{Style.RESET_ALL} {working_proxies}")
print("\t" + f"{Style.BRIGHT}Dead Proxies:{Style.RESET_ALL} {dead_proxies}")
percentage_working = (working_proxies / proxies_checked) * 100 if proxies_checked > 0 else 0
print("\t" + f"{Style.BRIGHT}Percentage Working:{Style.RESET_ALL} {percentage_working:.2f}%")
elapsed_time = time.time() - start_time
cpm = int((proxies_checked / elapsed_time) * 60) if elapsed_time > 0 else 0
print("\t" + f"{Style.BRIGHT}Checks Per Minute (CPM):{Style.RESET_ALL} {cpm}")