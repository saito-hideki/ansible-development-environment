"""Parse the command line arguments."""
import argparse

from ._version import __version__


def parse() -> argparse.Namespace:
    """Parse the command line arguments.

    Returns:
        The arguments
    """
    parser = argparse.ArgumentParser(
        description="A pip-like ansible collection installer.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--version",
        action="version",
        help="Version specifier.",
        version=__version__,
    )

    subparsers = parser.add_subparsers(
        title="subcommands",
        description="valid subcommands",
        help="additional help",
        dest="subcommand",
    )

    parent_parser = argparse.ArgumentParser(add_help=False)

    parent_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Increase output verbosity.",
    )
    parent_parser.add_argument(
        "collection_specifier",
        help="Collection name or path to collection with extras.",
    )
    parent_parser.add_argument(
        "--venv",
        help="Target virtual environment.",
    )


    install_usage = """Usage:
        pip4a install .
        pip4a install -e .
        pip4a install -e .[test]
        python -m pip4a install ansible.utils"""

    install = subparsers.add_parser(
        "install",
        epilog=install_usage,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parent_parser],
    )
    install.add_argument(
        "-e",
        "--editable",
        action="store_true",
        help="Install editable.",
    )

    _uninstall = subparsers.add_parser(
        "uninstall",
        epilog=install_usage,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parent_parser],
    )
    return parser.parse_args()
