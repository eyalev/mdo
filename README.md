
# mdo

View markdown documents in the terminal.

Markdown rendering is done by [Rich](https://github.com/willmcgugan/rich).

## Install

With [pipx](https://github.com/pipxproject/pipx)

```
$ pipx install mdo
```

With `pip`:

```
$ pip install mdo
```

## Usage

```
$ mdo FILE

# E.g: mdo README.md
```

From `$ mdo --help`:

```
Usage: mdo [FILE_PATH] [OPTIONS]

Options:
  -w, --width TEXT  Width of text. Default: 130. 'full' for full screen
  --no-pager        Print to terminal. Don't use pager (e.g 'less')
  -h, --help        Show this message and exit.
```
