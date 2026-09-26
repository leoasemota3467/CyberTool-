#!/usr/bin/env python3
"""CyberTool - cross-platform defensive security toolkit."""

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

from modules.port_scanner import scan_ports
from modules.dns_tools import dns_lookup
from modules.http_checker import check_http
from modules.tls_checker import check_tls
from modules.headers_checker import check_headers
from modules.hash_tools import hash_file
from modules.password_checker import check_password
from modules.local_info import local_info
from modules.report import save_report


def print_result(title, data):
    print(f"\n=== {title} ===")
    if isinstance(data, dict):
        for k, v in data.items():
            print(f"{k}: {v}")
    else:
        print(data)


def main():
    parser = argparse.ArgumentParser(
        prog="cybertool",
        description="Cross-platform defensive security toolkit for authorized testing."
    )
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("ports", help="Scan TCP ports on an authorized host")
    p.add_argument("host")
    p.add_argument("-p", "--ports", default="1-1024",
                   help="Port/range, e.g. 22,80,443 or 1-1024")
    p.add_argument("--timeout", type=float, default=0.5)

    p = sub.add_parser("dns", help="Resolve a domain")
    p.add_argument("domain")

    p = sub.add_parser("http", help="Check an HTTP/HTTPS URL")
    p.add_argument("url")

    p = sub.add_parser("tls", help="Inspect TLS certificate information")
    p.add_argument("host")
    p.add_argument("--port", type=int, default=443)

    p = sub.add_parser("headers", help="Check common HTTP security headers")
    p.add_argument("url")

    p = sub.add_parser("hash", help="Hash a local file")
    p.add_argument("file")
    p.add_argument("--algorithm", default="sha256",
                   choices=["md5", "sha1", "sha256", "sha512"])

    p = sub.add_parser("password", help="Check password strength locally")
    p.add_argument("password")

    sub.add_parser("local", help="Show local system/network information")

    p = sub.add_parser("save", help="Save JSON data from a file into a report")
    p.add_argument("file")

    args = parser.parse_args()

    try:
        if args.command == "ports":
            result = scan_ports(args.host, args.ports, args.timeout)
            print_result("PORT SCAN", result)
        elif args.command == "dns":
            result = dns_lookup(args.domain)
            print_result("DNS LOOKUP", result)
        elif args.command == "http":
            result = check_http(args.url)
            print_result("HTTP CHECK", result)
        elif args.command == "tls":
            result = check_tls(args.host, args.port)
            print_result("TLS CHECK", result)
        elif args.command == "headers":
            result = check_headers(args.url)
            print_result("SECURITY HEADERS", result)
        elif args.command == "hash":
            result = hash_file(args.file, args.algorithm)
            print_result("FILE HASH", result)
        elif args.command == "password":
            result = check_password(args.password)
            print_result("PASSWORD CHECK", result)
        elif args.command == "local":
            result = local_info()
            print_result("LOCAL SYSTEM", result)
        elif args.command == "save":
            data = json.loads(Path(args.file).read_text(encoding="utf-8"))
            path = save_report(data)
            print(f"Report saved to: {path}")
        else:
            parser.print_help()
    except KeyboardInterrupt:
        print("\nInterrupted.")
        return 130
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
