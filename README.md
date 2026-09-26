# CyberTool

CyberTool is a cross-platform, Python-based defensive security toolkit designed to run on **Windows, Linux, macOS, and Termux**.

## Features

- TCP port scanner with a safety-limited port range
- DNS/IP lookup
- HTTP/HTTPS connectivity checks
- TLS certificate and protocol inspection
- Common HTTP security-header checks
- Local file hashing
- Local password-strength analysis
- Basic local system information
- JSON reports
- Python standard library only

## Installation

### PC

Install Python 3.9+ and then:

```bash
git clone https://github.com/YOUR-USERNAME/cybertool.git
cd cybertool
python cybertool.py
```

On some Linux/macOS systems use `python3 cybertool.py`.

### Termux

```bash
pkg update
pkg install python git
git clone https://github.com/leoasemota3467/cybertool.git
cd cybertool
python cybertool.py
```

## Examples

```bash
python cybertool.py ports 192.168.1.1 -p 22,80,443
python cybertool.py ports 192.168.1.1 -p 1-1024
python cybertool.py dns example.com
python cybertool.py http https://example.com
python cybertool.py tls example.com
python cybertool.py headers https://example.com
python cybertool.py hash myfile.zip
python cybertool.py password "your-password"
python cybertool.py local
```

## Authorization

Only scan systems, networks, files, and websites that you own or have explicit permission to test. CyberTool intentionally avoids exploit delivery, credential theft, stealth/persistence, and unauthorized access features.

## Roadmap

Planned defensive modules include:

- configurable scan profiles
- CSV/HTML reports
- IPv6 improvements
- local service inventory
- file-integrity baselines
- plugin architecture
- unit tests and CI
- optional rich terminal UI
