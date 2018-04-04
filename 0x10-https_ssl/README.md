# 0x10-https_ssl

## 
### 0-https_abc
* File contains answers to questions:
  * What is HTTPS? Secure HTTP - 1
  * Why do you need HTTPS? To encrypt all communication between the client and the website servers - 2
  * Where should you put the certificate when you set up HTTPS on your website? On your website web server(s) - 3

### 1-world_wide_web
* Displays information for subdomains `www`, `lb-01`, `web-01`, `web-02`
  * Takes in domain (required) and subdomain (optional)
  * Output: The subdomain `[SUB_DOMAIN]` is a `[RECORD_TYPE]` record and points to `[DESTINATION]`
    * If no subdomain entered, shows information for all subdomains listed above

### 2-haproxy_ssl_termination
* Contains the contents of the /etc/haproxy/haproxy.cfg file after creating certbot

