"""Get system information"""

import psutil
import platform
from datetime import datetime

uname = platform.uname()

def get_size(bytes, suffix="B"):
    """
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

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

def get_memory_info() -> dict:
    """Get the memory information"""
    result = {}
    svmem = psutil.virtual_memory()
    result['total'] = get_size(svmem.total)
    result['available'] = get_size(svmem.available)
    result['used'] = get_size(svmem.used)
    result['percentage'] = get_size(svmem.free)
    swap = psutil.swap_memory()
    result['swap_total'] = get_size(swap.total)
    result['swap_free'] = get_size(swap.free)
    result['swap_used'] = get_size(swap.used)
    result['swap_percentage'] = swap.percent

    return result
