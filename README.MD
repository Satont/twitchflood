# Twitch flood

Simple script for chat flood some channel

# How to use

- install python 3+
- add your bot tokens in `tokens.txt` in following format:

```
oauth:token
oauth:token
```

- install dependencies `$ pip install -r requirements.txt`

After that lets use our script!

```sh
$ python app.py dota2ruhub 5 Privet from mother Russia!
```

where `dota2ruhub` = channel, `5` = delay in seconds, `Privet from mother Russia!` = message

Based on [Twitch-flood-bot](https://github.com/Zenaker/Twitch-flood-bot), what was written for python 2.7 and not
working with cyrillic. My script working with that.
