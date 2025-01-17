import yaml

def load_router_details(yaml_file):
    """Load router details from a YAML file."""
    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)

def connect_to_router(router):
    """Simulate connecting to a router and print its details."""
    print(f"Connecting to {router['hostname']} at {router['ip']}...")
    print(f"Using username: {router['username']}")
    print(f"Enable password: {router['enable_password']}")
    print(f"Device type: Cisco Router")
    print(f"Example command: 'show ip interface brief'")
    print(f"Connection to {router['hostname']} successful!")
    print("-" * 40)

routers = load_router_details('routers.yaml')['routers']
for router in routers:
    connect_to_router(router)
