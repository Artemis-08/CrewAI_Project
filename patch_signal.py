"""
Patch for Windows compatibility with crewai
"""
import signal
import sys
import os

# Add missing signal constants on Windows
if sys.platform == 'win32':
    if not hasattr(signal, 'SIGHUP'):
        signal.SIGHUP = 1
    if not hasattr(signal, 'SIGQUIT'):
        signal.SIGQUIT = 3
    if not hasattr(signal, 'SIGTRAP'):
        signal.SIGTRAP = 5
    if not hasattr(signal, 'SIGALRM'):
        signal.SIGALRM = 14
    if not hasattr(signal, 'SIGCHLD'):
        signal.SIGCHLD = 17
    if not hasattr(signal, 'SIGCONT'):
        signal.SIGCONT = 18
    if not hasattr(signal, 'SIGSTOP'):
        signal.SIGSTOP = 19
    if not hasattr(signal, 'SIGTSTP'):
        signal.SIGTSTP = 20
    if not hasattr(signal, 'SIGTTIN'):
        signal.SIGTTIN = 21
    if not hasattr(signal, 'SIGTTOU'):
        signal.SIGTTOU = 22

# Disable RAG for now to avoid ChromaDB issues
os.environ['CREWAI_TOOLS_RAG_ENABLED'] = 'false'
