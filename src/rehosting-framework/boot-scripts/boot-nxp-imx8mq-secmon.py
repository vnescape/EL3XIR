import os
import sys

import click

from secmonRehosting import install_logging
from secmonRehosting.rehostingEnvironments.imx8mq.factories import SecMonImx8mqAvatarFactory


@click.command()
@click.argument("secmon_binary_path")
@click.option("--avatar-output-dir", type=click.Path(exists=False))
def main(secmon_binary_path, avatar_output_dir):

    install_logging()

    if avatar_output_dir:
        print("Using output dir {} with avatar2".format(avatar_output_dir), file=sys.stderr)

        # create directory if it doesn't exist
        # that saves the user from creating it beforehand
        os.makedirs(avatar_output_dir, exist_ok=True)

        factory = SecMonImx8mqAvatarFactory()

        context = factory.get_rehosting_context(secmon_binary_path, avatar_output_dir)

        runner = factory.get_runner(context)

        runner.cont()
        print("Imx8mq SecMonitor booted!")


if __name__ == "__main__":
    main()