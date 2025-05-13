# DependencyVulnScanner
Simple Python tool to check for outdated dependencies and suggest updates
---

## 📌 Features

- Reads dependencies directly from a `requirements.txt` file.
- Checks each package against the latest version on PyPI.
- Warns when a package is outdated.
- Simple command-line interface.
- Lightweight and easy to extend.

---

## 🚀 Usage

1. **Install Dependencies**  
   ```bash
   pip install requests
2. **Add Dependencies**
   flask==1.1.2
requests==2.19.1
django==2.2.0
3. **Run Tool**
   python dependency_vuln_scanner.py
4. Example Output
   🔎 Checking Dependencies for Vulnerabilities...

⚠️ [requests] You have version 2.19.1, but the latest is 2.31.0. Consider updating!
✅ [flask] You’re using the latest version (1.1.2).
⚠️ [django] You have version 2.2.0, but the latest is 4.2.10. Consider updating!

✅ Dependency Check Complete!
