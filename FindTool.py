import subprocess

def main():
    swapout = input("enter name")

    findcommand = f'find / -name "{swapout}" 2> /dev/null'

    result = subprocess.run(findcommand, shell=True, capture_output=True, text=True)

    print(result.stdout)

if __name__ == "__main__":
    main()
