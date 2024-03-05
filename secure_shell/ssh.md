# SSH (Secure Shell)

SSH, or Secure Shell, is a cryptographic network protocol used for secure communication between a client and a server over an insecure network.

Key features include:

- **Encryption**: Ensures that all data exchanged, including passwords, commands, and files, is encrypted to protect against eavesdropping and interception.

- **Authentication**: SSH supports multiple authentication methods, with public key authentication being the most secure and commonly used.

- **Integrity**: Utilizes cryptographic hashes to verify the integrity of the transmitted data, detecting any tampering during transit.

- **Tunneling and Port Forwarding**: Allows for the secure tunneling of network connections and the forwarding of ports, facilitating secure communications over insecure networks.

SSH is widely used for managing servers, accessing remote development environments, and securely transferring files. It typically runs on TCP port 22 and is available across various platforms including Linux, macOS, and Windows.

### Why Use SSH Over HTTPS

SSH (Secure Shell) and HTTPS (Hypertext Transfer Protocol Secure) are both secure protocols used for communication over the internet. However, they serve different purposes and have distinct advantages. Here's why you might choose SSH over HTTPS:

- **Remote Shell Access**: SSH provides a secure way to access and control remote systems' shell environments, which is essential for server administration and executing remote commands, whereas HTTPS is primarily used for secure browsing and web transactions.

- **Secure File Transfers**: SSH includes SCP (Secure Copy Protocol) and SFTP (SSH File Transfer Protocol) for secure file transfers, offering more flexibility and control than HTTPS-based file transfers.

- **Port Forwarding/Tunneling**: SSH allows for secure port forwarding and the creation of encrypted tunnels for other protocols, enabling secure and private use of services like databases, email, and more over an insecure network.

- **No Need for a Web Server**: SSH communication doesn't require a web server or SSL/TLS certificates setup, making it simpler for non-web-based secure communications and tasks.

- **Interactive Sessions**: SSH supports interactive sessions, allowing users to work on remote systems as if they were local, which is not possible with HTTPS.

SSH is typically preferred for system administration, remote file manipulation, and secure access to network services, whereas HTTPS is the standard for secure web browsing and web-based transactions.

## Creating an SSH Key Pair

1. **Open Terminal**: Start by opening your terminal application.

2. **Generate SSH Key**: Use the `ssh-keygen` command to generate a new SSH key pair.

    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```

    - `-t rsa` specifies the type of key to create, in this case, RSA.
    - `-b 4096` provides the number of bits in the key, making it more secure than the default 2048 bits.
    - `-C "your_email@example.com"` is a comment to help identify the key, typically using your email.

3. **Specify Key Location**: When prompted, press `Enter` to save the key pair in the default location (`~/.ssh/id_rsa`), or specify a different path.

    ```
    Enter file in which to save the key (/your/home/.ssh/id_rsa):
    ```

4. **Enter Passphrase** (Optional): For added security, enter a passphrase when prompted. This will be required every time the private key is used.

    ```
    Enter passphrase (empty for no passphrase):
    ```

5. **Locate SSH Keys**: Your new SSH key pair is stored in the specified location. The public key file ends with `.pub`.

    - Private Key: `~/.ssh/id_rsa`
    - Public Key: `~/.ssh/id_rsa.pub`

Your SSH key pair is now ready to use. Add your public key to servers or services you wish to access securely with SSH.

## SSH Best Practices

### 1. Use Key-Based Authentication
Prefer using SSH keys over passwords for authentication. SSH keys are more secure and less susceptible to brute-force attacks.

```bash
# Generate an SSH key pair
ssh-keygen -t rsa -b 4096
```

### 2. Protect Your Private Key
Keep your private key secure. Use a strong passphrase and restrict access to the file.

# Set file permissions to read/write for the user only

```
bash
chmod 600 ~/.ssh/id_rsa
```


### 3. Disable Root Login
Avoid logging in as the root user directly. Use a regular user account and escalate privileges as needed using sudo.
```
bash
# Edit the SSH daemon configuration
sudo nano /etc/ssh/sshd_config
# Set the following option
PermitRootLogin no
```

### 4. Use Fail2Ban or Similar Tools
Implement tools like Fail2Ban to monitor and block repeated failed login attempts, reducing the risk of brute-force attacks.

### 5. Regularly Update SSH Software
Keep your SSH client and server software up-to-date to ensure you have the latest security patches.

### 6. Limit SSH Access Using Firewalls
Restrict which IP addresses or networks can attempt to connect to your SSH server using firewall rules.

### 7. Use SSH Agent Forwarding with Caution
SSH agent forwarding can be convenient but also presents a security risk. Use it sparingly and only on trusted machines.

### 8. Implement Two-Factor Authentication (2FA)
Enhance security by adding an additional layer of authentication beyond the SSH key.

### 9. Monitor SSH Access Logs
Regularly review your SSH access logs to detect unauthorized attempts or other suspicious activities.

### 10. Use Port Knocking or Change Default Port
Consider using port knocking or changing the default SSH port (22) to reduce the exposure to automated attacks.