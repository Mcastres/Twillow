# Twillow

You need more followers on Twitter ? Make yourself known through a script that makes you follow every user's followers

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Be sure to have Python on your computer

### Installing

```
$> pip install -r requirements.txt
```
Then you need to create an [application](https://apps.twitter.com/) with Read & Write permission

This being done, you must fill your tokens in `main.py`

```
self.consumer_key           = ''
self.consumer_secret        = ''
self.access_token           = ''
self.access_token_secret    = ''
```

Alright the script is good to go!

### How it works

The script is very simple. If you want to follow every followers of `elonmusk` account:

```
$> python main.rb elonmusk
>> You are now following every followers of elonmusk
```

Great! Now you're following users who are following Elon musk

It will create a `elonmusk_follower_ids` file. If you launch the same command again it will unfollow every users inside this file (elonmusk followers).

## Why

This is some Growth hacking trick, if you want to growth your business it is essential to be known on social networks.
By following interesting users, there is a chance that they will follow you back.
