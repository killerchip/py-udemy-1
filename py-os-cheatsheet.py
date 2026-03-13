# =============================================================================
# PYTHON `os` MODULE CHEATSHEET
# =============================================================================
import os

# =============================================================================
# 1. CURRENT DIRECTORY
# =============================================================================

os.getcwd()                         # return current working directory as string
os.chdir("/path/to/dir")            # change current working directory

# =============================================================================
# 2. FILES & DIRECTORIES
# =============================================================================

os.listdir(".")                     # list names in directory (default: cwd)
os.mkdir("new_dir")                 # create a single directory
os.makedirs("a/b/c")                # create directories recursively (like mkdir -p)
os.makedirs("a/b/c", exist_ok=True) # same, but no error if already exists
os.rmdir("empty_dir")               # remove an EMPTY directory
os.removedirs("a/b/c")             # remove empty directories recursively
os.remove("file.txt")               # delete a file
os.rename("old.txt", "new.txt")     # rename or move a file/directory
os.replace("old.txt", "new.txt")    # like rename, but overwrites destination

# =============================================================================
# 3. PATH CHECKS
# =============================================================================

os.path.exists("file.txt")          # True if path exists (file or dir)
os.path.isfile("file.txt")          # True if path is a file
os.path.isdir("my_dir")             # True if path is a directory
os.path.isabs("/home/user")         # True if path is absolute
os.path.getsize("file.txt")         # file size in bytes

# =============================================================================
# 4. PATH MANIPULATION  (prefer pathlib for new code)
# =============================================================================

os.path.join("dir", "sub", "f.txt") # join path components: 'dir/sub/f.txt'
os.path.split("/dir/file.txt")       # ('dir/', 'file.txt') -> (head, tail)
os.path.splitext("file.txt")         # ('file', '.txt') -> (name, extension)
os.path.basename("/dir/file.txt")    # 'file.txt'
os.path.dirname("/dir/file.txt")     # '/dir'
os.path.abspath("file.txt")          # full absolute path from relative path
os.path.expanduser("~/docs")         # expand ~ to home directory

# =============================================================================
# 5. WALKING DIRECTORY TREES
# =============================================================================

for root, dirs, files in os.walk("."):   # recursively walk directory tree
    for f in files:
        print(os.path.join(root, f))     # root=current dir, dirs=subdirs, files=filenames

# =============================================================================
# 6. ENVIRONMENT VARIABLES
# =============================================================================

os.environ                          # mapping of all environment variables
os.environ["HOME"]                  # get env var (raises KeyError if missing)
os.environ.get("HOME", "/default")  # get env var with fallback
os.environ["MY_VAR"] = "value"      # set env var for current process
os.getenv("HOME")                   # same as os.environ.get(), returns None if missing

# =============================================================================
# 7. PROCESS & SYSTEM INFO
# =============================================================================

os.getpid()                         # current process ID
os.getppid()                        # parent process ID
os.cpu_count()                      # number of CPUs (logical cores)
os.sep                              # path separator ('/' on Unix, '\\' on Windows)
os.linesep                          # line separator ('\n' Unix, '\r\n' Windows)
os.name                             # OS name: 'posix' (Unix/Mac) or 'nt' (Windows)

# =============================================================================
# 8. RUNNING SYSTEM COMMANDS  (prefer subprocess for new code)
# =============================================================================

os.system("ls -la")                 # run shell command, returns exit code
os.popen("ls").read()               # run command, return output as file object

# =============================================================================
# 9. ONE-LINERS FOR THE REST
# =============================================================================

os.stat("file.txt")                 # full stat result (size, mtime, permissions, ...)
os.chmod("file.txt", 0o755)         # change file permissions (Unix)
os.link("src", "dst")               # create a hard link
os.symlink("src", "dst")            # create a symbolic link
os.readlink("symlink")              # return target path of a symbolic link
os.urandom(16)                      # return N cryptographically random bytes
os.get_terminal_size()              # terminal width and height as (columns, lines)
os.scandir(".")                     # efficient iterator of DirEntry objects (faster than listdir)
