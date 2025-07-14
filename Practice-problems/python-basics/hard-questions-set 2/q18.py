# Center user's name in a banner using dashes.
name = input("Enter your first name: ")
total_length = 26
banner_text = "Welcome " + name
side_length = (total_length - len(banner_text)) // 2
banner = "-" * side_length + banner_text + "-" * side_length
print(banner)