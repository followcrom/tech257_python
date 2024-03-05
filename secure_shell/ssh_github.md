# Setting Up SSH Keys for GitHub

### 1. Check for Existing SSH Keys
First, check if you already have SSH keys generated on your machine.

```bash
ls -al ~/.ssh
```

### 2. Generate a New SSH Key
If you need to generate a new SSH key, use the following command, substituting your GitHub email address.
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
When prompted, enter a name for the key pair, then press Enter to use the default file location.

### 3. Add SSH Key to SSH-Agent
Ensure the ssh-agent is running and add your SSH key.

```bash
eval `ssh-agent`
ssh-add ~/.ssh/<PRIVATE key name>
```

### 4. Add SSH Key to GitHub Account
Copy your SSH public key to the clipboard.

```bash
cat ~/.ssh/<PUBLIC key name>.pub | clip
```
#### Global:
Go to GitHub, and navigate to Settings > SSH and GPG keys > New SSH key.

#### Repo specific:
Go to GitHub, and navigate to Repo Settings > Deploy keys > Add deploy key.

Paste your PUBLIC key into the "Key" field and add a descriptive title. 

Click Add SSH key.

### 5. Test Your SSH Connection
Finally, test your connection to GitHub.

```bash
ssh -T git@github.com
```

If successful, you'll receive a message confirming your authentication.