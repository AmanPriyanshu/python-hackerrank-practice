def fun(s):
    alphanum = "".join([str(i) for i in range(10)]+[chr(i) for i in range(65, 65+26)]+[chr(i) for i in range(97, 97+26)])
    specials = "-_"
    # return True if s is a valid email, else return False
    if s.find('@') != -1 and s.find('.') != -1:
        try:
            user = s[:s.find('@')]
            if len(user) == 0:
                return False
            domain = s[s.find('@')+1:s.find('.')]
            ext = s[s.find('.')+1:]
            if len(ext)>3:
                return False
            if not domain.isalnum():
                return False

            l = list(filter(lambda x: x in alphanum+specials, user))
            if len(l)!= len(user):
                return False
            return True
        except:
            return False
    else:
        return False
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