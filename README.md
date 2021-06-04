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

Fill files in `./quotes` folder. You should register a bot for Discord, then create file `./.env` with this content: 

```
DISCORD_TOKEN=<#your_token#>
```

Start bot with `python covenants.py`