# *Introducing the next level of naming conventions!*
After `CamelCase` and `snake_case`, we now present `EAEEAE__r_PL_C_M_NTc_S_`.

It's incredibly simple, based on the much-loved `sARCASTICcASE`:  
Pull each vowel forward and replace it with an underscore.  
Now place two underscores between the important starting block and the rear part of the name.  

__Improvements compared to conventional naming conventions:__  
1. See the most important building blocks of modern language at first glance.

2. Instantly recognize from the front vowels whether it's the same word, similar to a checksum, this saves a large part of the reading time.

3. Easy conversion through our AI-powered formatter `EAEEAEOE__r_PL_C_M_NTc_S_2c_D_`

To make the entry as easy as possible for beginners and experts alike, we have decided to make our tool open source.

```py
def EAEEAEOE__r_PL_C_M_NTc_S_2c_D_(s: str, OE__v_W_LS='aeiouAEIOU') -> str:

    return f"{''.join(c for c in s if c in OE__v_W_LS)}__{''.join('_' if c in OE__v_W_LS else c for c in s)}"
```

Usage:
1. Install python3.9.13
2. Run our tool on a given variable name written in sARCASTICcASEWrite better code.
3. Write better code!

We expect that this contribution will enrich the coding community and look forward to a soon revision of PEP8 and the Linux kernel coding style.

@thisRyan & @nonchris  
Your inventors of [ExceptionalProgramming](https://gist.github.com/nonchris/39ac230b6870af421e39c8a6cd21d47e) & `EAEEAE__r_PL_C_M_NTc_S_`

Special thanks to @paulmiro for helping with the implementation and @lgoette for the emotional support!  

`EEOAIEOUu__n_V_Rg_NN_g_V_y___P`!


## Setup

###### Setup a [venv](https://docs.python.org/3/library/venv.html) (optional, but recommend)
`python3 -m venv venv`   
`source venv/bin/activate` 


##### Using pip to install the bot as editable package:  
` python3 -m pip install -e .`  
`export TOKEN="your-key"`  
`discord-bot`  
##### Or using the launch script:  
`pip install -r requirements.txt`  
`export TOKEN="your-key"`   
`python3 ~/git/discord-bot/launcher.py`  

### Intents
The bot uses all intents by default, those are required for such simple things like 'display member-count at startup'.  
You need to enable those intents in the [discord developers portal](https://discord.com/developers/applications) 
under `*YourApplication*/Bot/Privileged Gateway Intents`.   
It's possible reconfigure the requested intents in `main.py` if you don't need them.  
But I'd suggest using them all for the beginning, especially if you're relatively new to discord.py.  
This will only be an issue if your bot reaches more than 100 servers, then you've got to apply for those intents. 

#### Optional env variables
| parameter |  description |
| ------ |  ------ |
| `PREFIX="b!"`  | Command prefix |
| `OWNER_NAME="unknwon"` | Name of the bot owner |
| `OWNER_ID="100000000000000000"` | ID of the bot owner |
| `ACTIVITY_NAME=f"{PREFIX}help"`| Activity bot plays |  

The shown values are the default values that will be loaded if nothing else is specified.  
Expressions like `{PREFIX}` will be replaced by during loading the variable and can be used in specified env variables.

Set those variables using env-variables (suggested):  
`export PREFIX="b!"`  
Or use a json-file expected at: `./data/config.json` like:  
```json
{
  "TOKEN": "[your-token]",
  "PREFIX": "b!"
}
```

_If a variable is set using env and json **the environment-variable replaces the json**!_

### documentation
In order to render this documentation, just call `doxygen`
