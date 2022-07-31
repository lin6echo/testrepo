import keyring

x = keyring.get_credential(service_name="keyring_app", username=None)

username_var = x.username
password_var = x.password

print('Username:', username_var)
print('Password:', password_var)