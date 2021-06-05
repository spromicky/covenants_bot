# Covenants Bot

Bot for Discord, that load fun qoutes from `.txt` files in `./quotes` folder, randomize it and print for user. `./quotes` has that structure: 

- `personalized/` - folder that contain list of files with specialized quotes for user
- `general.txt` - general quotes that can be used in any content type
- `keys.txt` - quotes specialized for m+ content
- `raid.txt` - qutoes specialized for raid content

> Files in `./quotes/personalized/` folder should have name like `<#username#>.txt`. Important, that `<#username#>` it means global username in Discord.
> Every line in any quotes files - one valid phrase. 

Bot has commands:

- `craid` - take all quotes from `general.txt` + `raid.txt` (optional `personalized/<#username#>.txt`) and randomize one of this quotes
- `ckeys` - take all quotes from `general.txt` + `keys.txt` (optional `personalized/<#username#>.txt`) and randomize one of this quotes
- `rl` - hot reload of files

After randomize qoutes saved in cache, unique for user until end of the day. Everyday you can randomize new quote.


### How to use:

- install dependencies `pip3 install --user -U python-dotenv` `pip3 install -U --user discord.py`
- fill files in `./quotes` folder
- create a bot on [Discord site](https://discord.com/developers/applications/)
- create file `.env` with content 

```
DISCORD_TOKEN=<#your_token#>
```

- run bot with `python3 covenants.py`

All thanks to [this guide](https://realpython.com/how-to-make-a-discord-bot-python/)
