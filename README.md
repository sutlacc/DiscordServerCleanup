# DiscordServerCleanup
A single script to manage and clean up inactive Discord server members

## How to setup
### 1. Install python
Ensure you have python installed on your system.
 - **Windows**: download Python from [here](https://www.python.org/downloads/)
 - **Linux**: Use your package manager(e.g., `sudo apt install python3` on Ubuntu)

### 2. Download and Extract
Download and Extract the compressed source files:
 - [Download for Windows (.zip)](https://github.com/sutlacc/DiscordServerCleanup/archive/refs/tags/v1.0.zip)
 - [Download for Linux (.tar.gz](https://github.com/sutlacc/DiscordServerCleanup/archive/refs/tags/v1.0.tar.gz)

### 3. Edit config.ini
Open the **config.ini** file in a text editor and set the following settings:
 - `bot_token`: Your Discord bot’s token
 - `server_id`: ID of the Discord server you want to cleanse
 - `inactivity_days`: Number of days a member can be inactive before getting kicked
 - `vc_log_id`: The ID of your Dyno voice log channel (if applicable). If you don't have one, set this to `0` to disable the feature.

### 4. Run
Double-click the `run.py` file and watch your wrath unfold across the server as the inactive are purged without mercy. The script will handle the setup automatically, so no extra installations are required.

If double-clicking doesn’t work! Open a terminal in the folder where the script is located and run the following command:
  `python run.py`

## Roadmap:
 - Optimized mode for larger servers
 - Scheduled cleanup to automate the process at regular intervals

If you encounter any issues or have suggestions, please feel free to open an issue or share your feedback on the repository. Contributions are welcome!
