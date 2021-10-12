"""CliffStructlogExpt application

cliff & structlog Experiment Command-line App

This module is connected to the `cliff_structlog_expt` command via a
an options.entry_points console_scripts item in setup.cfg.
"""
import sys

import cliff.app
import cliff.commandmanager

import cliff_structlog_expt


class CliffStructlogExptApp(cliff.app.App):
    CONSOLE_MESSAGE_FORMAT = "%(name)s %(levelname)s: %(message)s"

    def __init__(self):
        super().__init__(
            description="cliff & structlog Experiment Command-line App",
            version=cliff_structlog_expt.__version__,
            command_manager=cliff.commandmanager.CommandManager(
                "cliff_structlog_expt.app", convert_underscores=False
            ),
            stderr=sys.stdout,
        )


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    app = CliffStructlogExptApp()
    return app.run(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
