from io import StringIO

import click
from click import Context
from rich.console import Console
from rich.markdown import Markdown
from pathlib import Path
from subprocess import Popen, PIPE

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("file_path", type=click.Path(exists=True), required=False)
@click.option("--width", "-w", default="130", help="Width of text. Default: 130. 'full' for full screen")
@click.option("--no-pager", is_flag=True, default=False, help="Print to terminal. Don't use pager (e.g 'less')")
@click.pass_context
def cli(context: Context, file_path, width, no_pager):

    markdown_text = _get_markdown_text(file_path)
    if markdown_text is None:
        click.echo(context.get_help())
        return True

    width = _get_width(width)
    string_io = StringIO()
    console = Console(file=string_io, width=width, force_terminal=True)

    markdown_object = Markdown(markdown_text)

    console.print(markdown_object)

    text = string_io.getvalue()

    if no_pager:
        print(text)

    else:
        text_bytes = text.encode()
        less(text_bytes)


def _get_markdown_text(file_path):

    if file_path is None:
        readme = 'README.md'
        if Path(readme).exists():
            return Path(readme).read_text()
        else:
            return None

    path_object = Path(file_path)
    text = path_object.read_text()
    return text


def _get_width(width):
    if width == "full":
        return None
    else:
        return int(width)


def less(data):
    process = Popen(["less", "-R"], stdin=PIPE)

    process.stdin.write(data)
    process.communicate()
