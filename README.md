# Archiver

It's discord application to archive chat logs.

## Installation

```/bin/bash
$ pyenv virtualenv 3.7.4 archiver
$ pyenv local archiver
$ pip install -r requirements.txt
```

## Specification

### Bot (Client)

It's written with [discord.py] on [python 3.7.4].

[discord.py]: https://github.com/Rapptz/discord.py
[python 3.7.4]: https://www.python.org/downloads/release/python-374/

### Database

It uses [couchbase] as database to store logs (i.e. chats).

Because couchbase support scale-out easily with web interface, I believe it helps us manage infra effeciently.

[couchbase]: https://couchbase.com/
