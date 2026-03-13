# =============================================================================
# PYTHON `sys` MODULE CHEATSHEET
# =============================================================================
import sys

# =============================================================================
# 1. COMMAND-LINE ARGUMENTS
# =============================================================================

sys.argv                            # list of command-line args: ['script.py', 'arg1', 'arg2']
sys.argv[0]                         # script name (always first element)
sys.argv[1:]                        # actual arguments passed by the user

# =============================================================================
# 2. STANDARD STREAMS
# =============================================================================

sys.stdin                           # standard input stream (readable)
sys.stdout                          # standard output stream (writable)
sys.stderr                          # standard error stream (writable)

sys.stdin.read()                    # read all input from stdin
sys.stdout.write("hello\n")         # write to stdout (no automatic newline)
sys.stderr.write("error msg\n")     # write error message (bypasses stdout redirect)

# =============================================================================
# 3. EXIT & SHUTDOWN
# =============================================================================

sys.exit()                          # exit with code 0 (success)
sys.exit(1)                         # exit with code 1 (failure)
sys.exit("error message")           # print message to stderr and exit with code 1

# =============================================================================
# 4. PYTHON INTERPRETER INFO
# =============================================================================

sys.version                         # full version string: '3.11.2 (main, ...)'
sys.version_info                    # named tuple: (major, minor, micro, releaselevel, serial)
sys.version_info >= (3, 10)         # version check: True if Python 3.10+
sys.platform                        # platform string: 'linux', 'darwin', 'win32'
sys.executable                      # absolute path to the Python interpreter binary
sys.prefix                          # path to Python installation directory
sys.implementation.name             # interpreter name: 'cpython', 'pypy', etc.

# =============================================================================
# 5. MODULE & IMPORT SYSTEM
# =============================================================================

sys.modules                         # dict of all currently imported modules
sys.modules.get("os")               # get a module if already imported, else None
sys.path                            # list of directories searched for imports
sys.path.append("/my/custom/dir")   # add custom directory to import search path
sys.path.insert(0, "/priority/dir") # add with highest priority (searched first)
sys.builtin_module_names            # tuple of built-in module names (e.g. 'os', 'sys')

# =============================================================================
# 6. OBJECT SIZE & LIMITS
# =============================================================================

sys.getsizeof(object)               # memory size of object in bytes (shallow)
sys.getsizeof([1, 2, 3])            # e.g. 88 (does NOT count elements recursively)
sys.maxsize                         # max value of a Py_ssize_t: 9223372036854775807 (2^63-1)
sys.getrecursionlimit()             # current max recursion depth (default: 1000)
sys.setrecursionlimit(2000)         # set max recursion depth (use with caution)

# =============================================================================
# 7. REFERENCE COUNTING & GC
# =============================================================================

sys.getrefcount(object)             # reference count of object (+1 for the call itself)

# =============================================================================
# 8. ONE-LINERS FOR THE REST
# =============================================================================

sys.flags                           # command-line flags as named tuple (e.g. sys.flags.optimize)
sys.byteorder                       # native byte order: 'little' or 'big'
sys.float_info                      # float limits (max, min, epsilon, dig, ...)
sys.int_info                        # internal integer representation details
sys.hash_info                       # parameters of the numeric hash scheme
sys.hexversion                      # version as single hex int: e.g. 0x030b0200
sys.copyright                       # copyright notice string
sys.api_version                     # C API version number of the interpreter
sys.winver                          # Windows version string (Windows only)
sys.stdin.fileno()                  # file descriptor number of stdin (usually 0)
