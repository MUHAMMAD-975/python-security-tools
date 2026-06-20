#python-security-tools  
"A modular security toolkit built in Python, demonstrating password generation, hashing, salting, and CLI tool design."

---

##Project Structure

```
python-security-tools/
│
├── main.py          #Controller module (menu + workflow)
├── generator.py     # Password generator module
├── hasher.py        # Hashing + salting module
└── README.md       #Documentation
```

---

##Features

###Password Generator  
- User‑defined length  
- Character sets (upper, lower, digits, symbols)  
- Input validation  
- Secure random generation  

###Hashing + Salting  
- SHA‑256 hashing  
- Random salt generation  
- Secure password storage concepts  
- Returns both salt + hash  

###Modular Architecture  
- Each feature lives in its own module  
- `main.py` acts as the controller  
- Easy to expand with new tools  

---

##Learning Goals

This project helps me learn:

- Python basics  
- Functions & modules  
- Input validation  
- Loops & logic  
- Hashing & salting  
- CLI tool design  
- GitHub workflow  
- Real cybersecurity fundamentals  

---

##How to Run

### **1. Clone the repository**
```
git clone https://github.com/<your-username>/python-security-tools
```

### **2. Navigate into the folder**
```
cd python-security-tools
```

### **3. Run the main program**
```
python3 main.py
```
## Example Output

```
$ python3 main.py

Python Security Tools
1. Generate Password
2. Hash a Password
3. Exit

Choose option: 1
Enter password length (8-64): 16
Generated: X#mK9$pL2@nQ7!vR

Hash it? (y/n): y
Salt:  a3f8c2...
Hash:  e7d91b...
```
---

##Modules Explained

### **main.py**
Controls the entire program:
- Menu system  
- Calls generator module  
- Calls hasher module  
- Loops until user exits  

### **generator.py**
Handles:
- Asking for password length  
- Validating input  
- Building character sets  
- Generating secure passwords  

### **hasher.py**
Handles:
- Importing hashlib  
- Creating salts  
- Hashing passwords  
- Returning salt + hash  

---

##Future Improvements

- Save password + hash to a file  
- Add more security tools as I learn  

---

##Author

**Muhammad**  
Learning Python, Cloud, and Cybersecurity.  
Building projects from a mobile‑only setup using Acode + Termux + GitHub.
