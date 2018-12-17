# Twitch flood

Simple script for chat flood some channel

# How to use

- install python 3+
- add your bot tokens in `tokens.txt` in following format:

```
oauth:token
oauth:token
```

After that lats use our script!

```sh
$ pip install -r requirements.txt
$ python app.py channelname delay message
```

An example:

```sh
$ python app.py dota2ruhub 5 Privet from mother Russia!
```

Based on [Twitch-flood-bot](https://github.com/Zenaker/Twitch-flood-bot), what was written for python 2.7 and not
working with cyrillic. My script working with that.
