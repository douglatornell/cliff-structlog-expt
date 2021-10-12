"""CliffStructlogExpt plugin to test plugin entry point specification
and structlog integration

This module is connected to the `cliff_structlog_expt` command via a
an options.entry_points console_scripts item in setup.cfg.
"""
import logging
import cliff.command

logger = logging.getLogger(__name__)


class Foo(cliff.command.Command):
    """Do something foo-ish for cliff-structlog-expt."""

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.description = """
            Do something foo-ish for cliff-structlog-expt.
        """
        return parser

    def take_action(self, parsed_args):
        """Execute the `atlantis run` sub-command.

        :param parsed_args: Arguments and options parsed from the command-line.
        :type parsed_args: :class:`argparse.Namespace` instance
        """
        logger.info("Foo!!")
