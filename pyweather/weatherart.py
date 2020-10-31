from styling import Color


def clear_sky():
    print("""{bold}{yellow}
       .   \\_,!,_/   ,
        `.,'     `.,'
         /         \\
      -- :         : --  
         \\         /
        ,'`._   _.'`.
       '   / `!` \\   `
    {end}""".format(bold=Color.BOLD, yellow=Color.YELLOW, end=Color.END))


def few_clouds():
    print("""{bold}
                        {yellow}\\   |   /{end}{bold}
              .-~~~-.     {yellow}_____{end}{bold}
      .- ~ ~-(       )_ _{yellow}/      \\ ~ ~{end}{bold}
     /                     ~ -. {yellow}|{end}{bold}
    |                           \\ {yellow} ~ {end}{bold}
        ~- . _____________ . -~
    {end}""".format(bold=Color.BOLD, end=Color.END, yellow=Color.YELLOW))


def scattered_clouds():
    print("""{bold}
              .-~~~-.
      .- ~ ~-(       )_ _
     /                     ~ -.
    |                           \\
     \\                         .'
       ~- . _____________ . -~
    {end}""".format(bold=Color.BOLD, end=Color.END))


def broken_clouds():
    print("""{bold}
              .-~~~-.{end}        -.{bold}
      .- ~ ~-(       )_ _{end}        )_ _{bold}   
     /                     ~ -.{end}        ~ -. {bold} 
    |                           \\{end}          \\{bold}
     \\                         .'{end}          .'{bold}
       ~- . _____________ . -~{end}  ______ . -~{bold}  
    {end}""".format(bold=Color.BOLD, end=Color.END))


def rain():
    print("""{bold}
              .-~~~-.
      .- ~ ~-(       )_ _
     /                     ~ -.
     \\                         .'
       ~- . _____________ . -~
       {blue}’   ’   ’   ’   ’   ’
      ’   ’   ’   ’   ’   ’
    {end}""".format(bold=Color.BOLD, blue=Color.BLUE, end=Color.END))


def thunderstorm():
    print("""{bold}
                  .-~~~-.
      .- ~ ~-(       )_ _
     /                     ~ -.
     \\                         .'
       ~- . _____________ . -~
        {blue}’{end}{bold}   {yellow}/    /{end}{bold}   {blue}’   ’  
       ’{end}{bold}    {yellow}\\   \\{end}{bold}   {blue}’   ’
      ’{end}{bold}     {yellow}/  /{end}{bold}   {blue}’   ’{end}{bold}
            {yellow}\\ \\{end}
    """.format(bold=Color.BOLD, blue=Color.BLUE, yellow=Color.YELLOW, end=Color.END))


def snow():
    print("""{bold}
       .      .
       _\/  \/_
        _\/\/_
    _\_\_\/\/_/_/_
     / /_/\/\_\ \\
        _/\/\_
        /\  /\\
       '      '
    {end}""".format(bold=Color.BOLD, end=Color.END))


def mist():
    print("""{bold}
         ~~~~
      ~~~~~~~~~
           ~~~~~~~
      ~~~~~~~
        ~~~~~~~~~~~~~
    {end}""".format(bold=Color.BOLD, end=Color.END))


clear_sky()
few_clouds()
scattered_clouds()
broken_clouds()
rain()
thunderstorm()
snow()
mist()
