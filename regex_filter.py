import re

if __name__ == '__main__':
    N = int(input().strip())

    gmail_users = []

    for _ in range(N):
        firstName, emailID = input().strip().split()
        if re.search(r'@gmail\.com$', emailID):
            gmail_users.append(firstName)

    gmail_users.sort()

    for name in gmail_users:
        print(name)
