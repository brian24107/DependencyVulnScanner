import requests

def read_dependencies(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().split('==')[0] for line in file if '==' in line]

def check_vulnerability(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            latest_version = data['info']['version']
            return latest_version
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def main():
    packages = read_dependencies('requirements.txt')
    print("\n🔎 Checking Dependencies for Newer Versions...\n")
    for package in packages:
        latest_version = check_vulnerability(package)
        if latest_version:
            print(f"[{package}] Latest Version: {latest_version}")
        else:
            print(f"[{package}] Could not check version.")
    print("\n✅ Check Complete!")

if __name__ == "__main__":
    main()
