def fun(s):
    # return True if s is a valid email, else return False
    try:
        user, domain = s.split("@")
        web, extension = domain.split(".")
    except:
        return False
    if not(extension.isalpha()) or len(extension) > 3:
        return False
    elif not(web.isalnum()):
        return False
    elif user.replace("_", "").replace("-", "").isalnum():
        return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
