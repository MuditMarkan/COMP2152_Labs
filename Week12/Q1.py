# ============================================================
#  WEEK 12 LAB — Q1: SCANNER INHERITANCE
#  COMP2152 — Mudit Markan
# ============================================================

import socket
import urllib.request
import urllib.error  # Added to handle specific HTTP exceptions


class Scanner:
    """Parent class — shared by all scanner types."""

    def __init__(self, target):
        self.target = target
        self.results = []

    # TODO: Write display_results(self)
    #   Print "Results for {self.target}:"
    #   If self.results is empty: print "  (no results)"
    #   Otherwise: print each result with "  " indent
    def display_results(self):
        print(f"Results for {self.target}:")
        if not self.results:  # if results list is empty
            print("  (no results)")
        else:
            for result in self.results:
                print(f"  {result}")


class PortScanner(Scanner):
    """Child class — scans for open ports."""

    # TODO: Write __init__(self, target, ports)
    #   Call the parent constructor: super().__init__(target)
    #   Store self.ports (a list of port numbers)
    def __init__(self, target, ports):
        super().__init__(target)  # Call parent constructor
        self.ports = ports

    # TODO: Write scan(self)
    #   Loop through self.ports
    #   For each port:
    #     Create a socket, set timeout to 1, use connect_ex
    #     If result == 0: append f"Port {port}: OPEN" to self.results
    #     Else: append f"Port {port}: closed" to self.results
    #     Close the socket
    def scan(self):
        for port in self.ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # 1 second timeout
            result = sock.connect_ex((self.target, port))
            if result == 0:  # Port is open
                self.results.append(f"Port {port}: OPEN")
            else:  # Port is closed
                self.results.append(f"Port {port}: closed")
            sock.close()


class HTTPScanner(Scanner):
    """Child class — scans HTTP paths for accessible pages."""

    # TODO: Write __init__(self, target, paths)
    #   Call the parent constructor: super().__init__(target)
    #   Store self.paths (a list of URL paths like "/", "/admin")
    def __init__(self, target, paths):
        super().__init__(target)  # Call parent constructor
        self.paths = paths

    # TODO: Write scan(self)
    #   Loop through self.paths
    #   For each path:
    #     Try: urllib.request.urlopen(f"http://{self.target}{path}")
    #       Append f"{path} → {response.status} (accessible)" to self.results
    #     Except: Append f"{path} → NOT FOUND" to self.results
    def scan(self):
        for path in self.paths:
            try:
                # Build the full URL
                url = f"http://{self.target}{path}"
                # Open the URL and get response
                response = urllib.request.urlopen(url)
                # If successful, append with status code
                self.results.append(f"{path} → {response.status} (accessible)")
                response.close()
            except urllib.error.HTTPError as e:
                # HTTP error (404, 403, etc.)
                self.results.append(f"{path} → {e.code} {e.reason}")
            except Exception as e:
                # Other errors (connection refused, timeout, etc.)
                self.results.append(f"{path} → NOT FOUND ({str(e)})")


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q1: SCANNER INHERITANCE")
    print("=" * 60)

    print("\n--- Port Scanner ---")
    ps = PortScanner("127.0.0.1", [22, 80, 443])
    print(f"  Scanning {ps.target} ports...")
    ps.scan()
    ps.display_results()

    print("\n--- HTTP Scanner ---")
    hs = HTTPScanner("127.0.0.1", ["/", "/admin", "/.git/config"])
    print(f"  Scanning {hs.target} paths...")
    hs.scan()
    hs.display_results()

    print("\n" + "=" * 60)