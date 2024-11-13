## Crawler

This script is designed to discover hidden directories and subdomains on a target website. It can be useful for security professionals conducting reconnaissance on a web server.

### Features

- **Directory Discovery**: Scans for hidden directories on a web server.
- **Subdomain Discovery**: Optionally, it can discover subdomains by uncommenting the subdomain discovery section.

### How It Works

The script reads a list of common directory names or subdomains from a wordlist file and appends each name to the target URL. If the request to a constructed URL is successful, it identifies the URL or subdomain as "discovered."

### Usage

1. **Directory Discovery**
   - Update `target_url` with the IP address or domain of your target server.
   - Ensure you have a wordlist file containing directory names, and update the path if necessary:
     ```python
     with open("/home/kali/Downloads/common.txt", "r") as wordlist_file:
     ```

2. **Subdomain Discovery**
   - Uncomment the "Discovering Subdomains" code section if you want to perform subdomain discovery.
   - Use a suitable subdomain wordlist and update its path:
     ```python
     with open("/home/kali/Downloads/subdomainslist.txt", "r") as wordlist_file:
     ```

3. **Run the Script**:
   ```bash
   python crawler.py
   ```

### Requirements

- **Python 3.x**
- **Requests Library**: Install using:
  ```bash
  pip install requests
  ```

### Example

For `target_url = "192.168.**.**"`, if the script finds a valid directory, it outputs:
```bash
[+] Discovered URL --> http://192.168.**.**/admin
```

### Important Note
This tool should be used **only on servers for which you have explicit permission**. Unauthorized scanning is illegal and unethical.

### Authors

- [Zaid Sabih](https://ie.linkedin.com/in/zaid-sabih-al-quraishi-5444a6127)
- [Uzoeshi Daniel](https://www.linkedin.com/in/daniel-ikenna-33b709235)
