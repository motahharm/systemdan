"""Get system information"""

import psutil
import platform
from datetime import datetime

uname = platform.uname()

def get_system_name() -> str:
    return uname.system
def get_node_name() -> str:
    return uname.node
def get_release() -> str:
    return uname.release
def get_version() -> str:
    return uname.version
def get_machine() -> str:
    return uname.machine
def get_processor() -> str:
    return uname.processor

def get_all_info() -> dict:
    """Get all system information"""
    result = {}
    result['system'] = get_system_name()
    result['node'] = get_node_name()
    result['release'] = get_release()
    result['version'] = get_version()
    result['machine'] = get_machine()
    result['processor'] = get_processor()
    result['boot_time'] = get_boot_time()
    result['cpu_info'] = get_cpu_info()
    return result

def get_boot_time() -> datetime:
    """Get the boot time of the system"""
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    return bt

def get_cpu_info() -> dict:
    """Get the CPU information"""
    result = {}

    result['physical_cores'] = psutil.cpu_count(logical=False)
    result['total_cores'] = psutil.cpu_count(logical=True)

    cpufreq = psutil.cpu_freq()
    result['current_freq'] = cpufreq.current
    result['min_freq'] = cpufreq.min
    result['max_freq'] = cpufreq.max

    result['cpu_list'] = []
    for i, percentage in enumerate(
        psutil.cpu_percent(
            percpu=True, interval=1
            )
        ):
        result['cpu_list'].append(percentage)
    result['cpu_percent'] = psutil.cpu_percent()

    return result
