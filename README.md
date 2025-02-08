# NetGate  
**Block or unblock internet access for specific applications using Windows Firewall.**  
`NetGate` allows users to block or unblock internet access for applications, this uses the Windows Firewall by adding and removing rules. This is a potential prevention on security that simplifies the addition and removal of Windows Firewall Rules. Example usages can be seen below. 
## Features
- Windows Firewall Simplified
- Block internet access for any application
- Restore internet access
- Simple command-line interface
- No external dependencies (uses built-in `netsh`)
## Example Usages
### Update Prevention
Most updates require an internet connection for completion, allowing prevention.
### Gaming Experience Enhancement
An offline mode can be forced by cutting off connections for the game. 
### Bandwidth Management
Allow control of bandwidth by disabling connections.
### Testing
Developers or testers who want to test/simulate how an application behaves without internet access.
### Data Sharing
Stops unwanted personal or application related data from being sent to and from servers.
### Malware Protection
By cutting off internet access for potential (specific) malware, this can allow users to run potentially suspicious software while significantly **reducing** the risk.
## Prerequisites  
- Windows OS  
- Python 3.7+ installed  
- Administrator privileges (to modify firewall rules)  
## Installation
1. Download latest version [Python](https://www.python.org/downloads/).
2. Download and run `NetGate.py` (as administrator).
3. Enter the full path of the applicaiton. Example: `"C:\Users\MyUser\Desktop\MyApplication.exe"`.
4. Type and enter `b` for **block** (block connection for the application) or `u` for **unblock** (unblock connection for application).
5. You will see completion/failure printed in terminal. 
## Disclaimer
Cutting off internet access to applications is not a complete or effective security solution. Example usages may state protection against certain specific malware, but really is not a recommendation (why this is a **Potential** and **NOT** guaranteed). Disabling application updates and the restriction of specific data from being sent, may violate terms and you should check these before using `NetGate`, some updates may improve security far better than NetGate can offer and some data may be required and not optional (if they were optional, there should be a way to stop this, please do your research). By using `NetGate` you are responsible for all actions, I do not promote `NetGate` for illegal usage or usages that may violate specific terms, I am not responsible for anything you have used this project for. `NetGate` is **NOT** security, it's a shortcut.
## FAQs
### Can I run malware?
If you know or have suspicions that you are running malware, it is recommended to not run at all. `NetGate` is **NOT** a security solution, it is a **potential** prevention. 
### Can I use this tool on macOS or Linux?
No, `NetGate` is designed for Windows only because it uses the Windows Firewall (netsh advfirewall) to add or remove rules. This tool is not compatible with macOS or Linux.
### What if I accidentally block the wrong application?
You can unblock any application by running the tool again, this will remove **all** rules that were created.
### Does this prevent malware?
No, `NetGate` does not prevent malware, it can cut off the connection, but will not prevent the execution of malware.
### Is NetGate legal?
`NetGate` is legal if used as intended and is exaplined what is the correct usage of NetGate. You are responsible for your actions.
### Can I block only certain network connections (like specific IP addresses or ports)?
`NetGate` blocks all outbound connections for the specific application. If you need more control, I recommend you use **Windows Firewall**.
### How can I see which applications have internet access blocked?
You can check the list of active firewall rules on your Windows system by running the following command in the command prompt or PowerShell: `netsh advfirewall firewall show rule name=all`.
### Is NetGate safe?
`NetGate` is nothing but a shortcut to the Windows Firewall, there is no other function that `NetGate` serves.
### Will NetGate be updated?
`NetGate` has fullfilled its purposes and I see no reason to update `NetGate` apart from fixes. The intended purpose of `NetGate` is simply as a shortcut and not a complete security solution.
