# Wabbajack free auto-downloader

## Description

Automate mouse clicks using image detection to download Wabbajack mod lists as a free nexus user.

## Disclaimer

I fully support the Nexus page and you SHOULD consider buying their premium version, which has faster download speeds and also helps keeping the lights on.

This script was made for people that are not avid users of Nexus, but every once in a while like to download a simple mod list to play with.

## How it works

It'll look for the following button (Nexus download page) every three seconds.

![image](./input_images/1_button.png)

If it finds it, it'll press it.

If it doesn't, it'll log that it wasn't found and move.

The loop will iterate 99999 times. After that, the program will end.

If you need more than that, just start it again.

## Requirements

1) Install python. `(This script was tested against version 3.13.7)`
2) In a prompt, enter: `pip install pyautogui keyboard numpy opencv-python pillow pyscreeze`
3) This was made to run on a Windows environment, was never tested with macOS or a Linux desktop distro.

## Custom Variables

1) max_loop: the amount of loops you want to run (default 2)
2) click_interval: interval between each mouse clicks in second (default 1)
3) loop_interval: interval between each loop in second  (default 1)

## How to run

1) You can either `Double click "custom_automation.py"` or run `python custom_automation.py`.
2) Press "Escape" to quit
3) Set the custom variables, start the script, run your own mouse click automation.

## Future changes

1) Add a customisation environment file to allow customizing the variables without having to modify the script itself.

## Credits

This is a fork of [image_autoclicks](https://github.com/well-c/image_autoclicks), the original script was made to be generic, this is already set to work with the Nexus download page. You should check their work too.
