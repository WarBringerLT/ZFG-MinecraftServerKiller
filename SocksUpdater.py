###############################################################
#                                                             #
#               SOCKS UPDATER by WarBringerLT                 #
#                       08 - 06 - 2022                        #
# Uses GitHub provided Proxy Lists.
# https://spys.me/socks.txt # https://github.com/clarketm/proxy-list
# https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt   # https://github.com/jetkai/proxy-list
# ARCHIVE: https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks4.txt 
# https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt 
# https://github.com/TheSpeedX/PROXY-List/blob/master/socks5.txt           
# https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt 
from os import path, chdir, getcwd
from sys import argv
import requests
from ipaddress import ip_address
from time import sleep
from bs4 import BeautifulSoup
#from ProxyChecker import proxy_checker
from itertools import cycle
from threading import Thread
import sys
import urllib.request, socket
from random import choice
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial

stop_flag = 0
if len(path.dirname(argv[0])) != 0:
	chdir(path.dirname(argv[0]))
# Set Working Dir to Script Location
App_Version = "v1.1"
LauncherPath = getcwd()
socket.setdefaulttimeout(30)
SOCKS4_WEBSITES = ["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
					"https://openproxy.space/list/socks4",
					"https://openproxylist.xyz/socks4.txt",
					"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
					"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
					"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
					"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
					"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
					"https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks4.txt",
					"https://www.freeproxychecker.com/result/socks4_proxies.txt",
					"https://www.proxy-list.download/api/v1/get?type=socks4",
					"https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks4.txt",
					"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt"]  
SOCKS5_WEBSITES = ["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
					"https://openproxy.space/list/socks5",
					"https://openproxylist.xyz/socks5.txt",
					"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
					"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
					"https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
					"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
					"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
					"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
					"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
					"https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks5.txt",
					"https://www.freeproxychecker.com/result/socks5_proxies.txt",
					"https://www.proxy-list.download/api/v1/get?type=socks5",
					"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt"]

print("\n\n[~] Starting up...\n[~] Importing Logging Engine...")

try: # Load Logging Module
	from Logger_Stripped import Logging # https://github.com/WarBringerLT/PythonLoggingSimplifier
	Logger = Logging()
	Logger.log("[+] Logger Started!")
	Logger.log("Importing and verifying all other Dependencies...")
except ImportError: exit(print(input("[!] Failed to load Logging Module! Please refer to GitHub Page to download the Dependencies. \n\n\n[Program Terminated.] = Press ENTER to Exit.")))

def Validate_IPv4(ipaddr):
	try: ip_address(ipaddr)
	except ValueError: return False # Not an IP

def FlushToFile(IP_List, filename):
	with open(filename, 'w') as outputfile:
		for IP in IP_List:
			IP = IP.strip('\r').strip('\n')
			outputfile.write(IP + '\n')


Logger.log("[+] Attempting to Update SOCKS4 & SOCKS5 IP's...")
Logger.log(f"[>] SOCKS4 Websites: {len(SOCKS4_WEBSITES)}")
Logger.log(f"[>] SOCKS5 Websites: {len(SOCKS5_WEBSITES)}")
Logger.log("[~] Attempting to Parse New SOCKS4 IP List...")
SOCKS4_NEW_IP_LIST = []

for Website in SOCKS4_WEBSITES:
		try:
			header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)","X-Requested-With": "XMLHttpRequest"}
			Website_Response = requests.get(Website, headers = header)
			IP_LIST_RAW      = BeautifulSoup(Website_Response.text, 'html.parser')         # Parse the list
			IP_LIST = IP_LIST_RAW.decode('utf-8').split("\n")  # Decode the strings
			for IP in IP_LIST:                                 # Loop each line in New List
				IP = IP.strip('\n')
				if Validate_IPv4(IP.split(":")[0]) is False: pass # If Line is not a valid IP address, then skip it
				else: SOCKS4_NEW_IP_LIST.append(IP.strip('\r').strip('\n')) # Othetwise, add it as a new IP :)	
			Logger.log(f"[+++] > Website ID: {SOCKS4_WEBSITES.index(Website)} - Provided - {len(IP_LIST)} New IP's :))))")
		except: Logger.log(f"[X] Website \"{Website}\" Returned Error Response. 0 IP's Gathered.")

# Flush IP's to a File
FlushToFile(SOCKS4_NEW_IP_LIST,'API_SOCKS4.list')
Logger.log(f"[!!] Saved ({len(SOCKS4_NEW_IP_LIST)}) New-Proxy IPs to \"API_SOCKS4.list\" file successfully!")


Logger.log("[~] Attempting to Parse New SOCKS5 IP List...")
SOCKS5_NEW_IP_LIST = []
for Website in SOCKS5_WEBSITES:
		try:
			header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)","X-Requested-With": "XMLHttpRequest"}
			Website_Response = requests.get(Website, headers = header)
			IP_LIST_RAW      = BeautifulSoup(Website_Response.text, 'html.parser')         # Parse the list
			IP_LIST = IP_LIST_RAW.decode('utf-8').split("\n")  # Decode the strings
			for IP in IP_LIST:                                 # Loop each line in New List
				IP = IP.strip('\n')
				if Validate_IPv4(IP.split(":")[0]) is False: pass # If Line is not a valid IP address, then skip it
				else: SOCKS5_NEW_IP_LIST.append(IP.strip('\r').strip('\n')) # Othetwise, add it as a new IP :)	
			Logger.log(f"[+++] > Website ID: {SOCKS5_WEBSITES.index(Website)} - Provided - {len(IP_LIST)} New IP's :))))")
		except: Logger.log(f"[X] Website \"{Website}\" Returned Error Response. 0 IP's Gathered.")

FlushToFile(SOCKS5_NEW_IP_LIST,'API_SOCKS5.list')
Logger.log(f"[!!] Saved ({len(SOCKS5_NEW_IP_LIST)}) New-Proxy IPs to \"API_SOCKS5.list\" file successfully!")

#Check_Them = "x"
#while (Check_Them.lower() != "y") and (Check_Them.lower() != "n"):
#	Check_Them = input("[<>] Would you like to scan for ALIVE Proxies from both lists? - [y/n]: ")
#	if Check_Them.lower() != 'y': exit(0)
# Continue portscanning


Logger.log("[!] Attempting to scan Socks4 List of IPs!")

def check_proxy(session, proxy, Type):
    check = 'http://manoip.lt'
    try:
        response = session.get(check, proxies={f'{Type}': f'{Type}://'+proxy}, timeout=5)
        status = response.status_code
        return status == 200
    except Exception:
        return False

def get_proxies(session, executor, Type):
	global ALIVE_SOCKS4, ALIVE_SOCKS5
	if Type == 'socks4':
		with open('API_ALIVE_SOCKS4.list', 'a') as outfile:
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0","Accept-Encoding": "*","Connection": "keep-alive"}
			session.headers.update(headers)
			futures = {executor.submit(partial(check_proxy, session), proxy, Type): proxy for proxy in SOCKS4_NEW_IP_LIST}

			for future in as_completed(futures):
				proxy = futures[future]
				is_good = future.result()
				if is_good:
					ALIVE_SOCKS4.append(proxy)
					outfile.write(proxy + '\n')
					Logger.log(f"[ALIVE] [SOCKS4] - Total Alive - {len(ALIVE_SOCKS4)}/{len(SOCKS4_NEW_IP_LIST)}")
	else:
		with open('API_ALIVE_SOCKS5.list', 'a') as outfile:
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0","Accept-Encoding": "*","Connection": "keep-alive"}
			session.headers.update(headers)
			futures = {executor.submit(partial(check_proxy, session), proxy, Type): proxy for proxy in SOCKS5_NEW_IP_LIST}

			for future in as_completed(futures):
				proxy = futures[future]
				is_good = future.result()
				if is_good:
					ALIVE_SOCKS5.append(proxy)
					outfile.write(proxy + '\n')
					Logger.log(f"[ALIVE] [SOCKS5] - Total Alive - {len(ALIVE_SOCKS5)}/{len(SOCKS5_NEW_IP_LIST)}")
	                


ALIVE_SOCKS4 = []
ALIVE_SOCKS5 = []
N_THREADS=100
with requests.Session() as session:
    with ThreadPoolExecutor(max_workers=N_THREADS) as executor:
        get_proxies(session, executor, "socks4")

with requests.Session() as session:
    with ThreadPoolExecutor(max_workers=N_THREADS) as executor:
        get_proxies(session, executor, "socks5")
        

