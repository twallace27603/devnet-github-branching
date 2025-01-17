import yaml
import paramiko

def load_router_details(yaml_file):
    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)

def connect_to_router(router):
    print(f"Connecting to {router['hostname']} at {router['ip']}...")
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=router['ip'],
            username=router['username'],
            password=router['password']
        )
        print(f"Connected to {router['hostname']}")
        # Example: Run a command
        stdin, stdout, stderr = ssh.exec_command("show version")
        print(stdout.read().decode())
        ssh.close()
    except Exception as e:
        print(f"Failed to connect to {router['hostname']}: {e}")

def main():
    routers = load_router_details('routers.yaml')['routers']
    for router in routers:
        connect_to_router(router)

if __name__ == "__main__":
    main()
