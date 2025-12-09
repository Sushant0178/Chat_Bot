
import subprocess
from aii import Query, takeCommand


def search_in_system():
    query = takeCommand().lower()
    query== takeCommand()
    local_path = r''  # r is raw for dealing with backslashes
    # network_path = r'\\your\network\fold\path'

# for a network location
    # subprocess.Popen(f'explorer /root,"search-ms:query={query_string}&crumb=location:{network_path}&"')

# for a local folder
    subprocess.Popen(
        f'explorer /root,"search-ms:query={query}&crumb=folder:{local_path}&"')

