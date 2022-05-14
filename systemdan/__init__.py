"""
    System Information
"""
# systemdan/__init__.py

__app_name__ = "systemdan"
__version__ = "0.0.1"


(
    SUCCESS,
    NOT_SUPPORTED_ERR,
) = range(2)

ERRORS = {
    SUCCESS: "Success",
    NOT_SUPPORTED_ERR: "this system does not support this feature",
}
