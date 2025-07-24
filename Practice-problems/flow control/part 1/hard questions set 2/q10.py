# ask for secret code and security level
secret_code = str(input("enter a secret code:"))
security_level = int(input("enter security level (1-10):"))
# check security conditions
security_check = (not(secret_code == "admin")) and (len(secret_code) > 7) and (security_level >= 5) or (security_level == 10)
print (security_check)