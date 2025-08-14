#!/usr/bin/env python3
"""
Script to run both Django servers on different ports
"""
import subprocess
import time
import sys
import os

def run_server(project_path, port, project_name):
    """Run a Django server on the specified port"""
    print(f"Starting {project_name} on port {port}...")
    
    # Change to project directory
    os.chdir(project_path)
    
    # Run the server
    try:
        subprocess.run([
            sys.executable, "manage.py", "runserver", f"127.0.0.1:{port}"
        ], check=True)
    except KeyboardInterrupt:
        print(f"\n{project_name} server stopped.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting {project_name}: {e}")

def main():
    print("Starting Django SSO Servers...")
    print("=" * 40)
    
    # Start SSO Server (mtfa) on port 8000
    print("1. Starting SSO Server (mtfa) on port 8000")
    print("   - This will handle authentication")
    print("   - Access at: http://127.0.0.1:8000")
    print()
    
    # Start SSO Client on port 8001
    print("2. Starting SSO Client on port 8001")
    print("   - This will redirect to SSO server for login")
    print("   - Access at: http://127.0.0.1:8001")
    print()
    
    print("Press Ctrl+C to stop all servers")
    print("=" * 40)
    
    # Start both servers
    try:
        # Start SSO Server in background
        server_process = subprocess.Popen([
            sys.executable, "mtfa/manage.py", "runserver", "127.0.0.1:8000"
        ])
        
        # Wait a moment for server to start
        time.sleep(3)
        
        # Start SSO Client
        client_process = subprocess.Popen([
            sys.executable, "sso_client/manage.py", "runserver", "127.0.0.1:8001"
        ])
        
        # Wait for either process to finish
        while True:
            if server_process.poll() is not None:
                print("SSO Server stopped unexpectedly")
                client_process.terminate()
                break
            if client_process.poll() is not None:
                print("SSO Client stopped unexpectedly")
                server_process.terminate()
                break
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping servers...")
        server_process.terminate()
        client_process.terminate()
        print("All servers stopped.")

if __name__ == "__main__":
    main()
