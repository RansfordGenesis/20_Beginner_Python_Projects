def email_slicer():
    print("Welcome to Email Slicer")
    print("")
    
    email = input("Input a valid email to slice: ")
    (username, domain) = email.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


email_slicer()