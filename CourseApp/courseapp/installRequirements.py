import subprocess

def install_requirements(requirements_file):
    with open(requirements_file, 'r') as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]

    for requirement in requirements:
        subprocess.run(['pip', 'install', requirement])

if __name__ == "__main__":
    requirements_file = 'requirements.txt'
    install_requirements(requirements_file)
