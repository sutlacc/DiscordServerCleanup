import sys



#Script

def run_script():
    import discord
    from discord.ext import commands
    from datetime import datetime, timedelta
    import configparser

    config = configparser.ConfigParser()
    config.read('config.ini')

    BOT_TOKEN = config['Options']['token']
    SERVER_ID = int(config["Options"]["server_id"])
    KICK_TIME = int(config["Options"]["inactive_days"])
    VC_LOG_ID = int(config["Options"]["vc_log_id"])

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    bot = commands.Bot(command_prefix="", intents=intents)

    result_date = datetime.now() - timedelta(KICK_TIME)
    talked = []

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user} ({bot.user.id})")

        server = bot.get_guild(SERVER_ID)
        await parse_server(server)
        if VC_LOG_ID != 0:
            await check_voice_logs(server)
        
        await kick_members(server, talked)

    async def parse_server(server):
        for channel in server.channels:
            if isinstance(channel, discord.VoiceChannel):
                await parse_channel(channel)
            elif isinstance(channel, discord.TextChannel):
                await parse_channel(channel)
                for thread in channel.threads:
                    await parse_channel(thread)
            elif isinstance(channel, discord.ForumChannel):
                for post in channel.threads:
                    await parse_channel(post)

    async def parse_channel(child):
        async for message in child.history(after=result_date):
            id = message.author.id
            if id not in talked:
                talked.append(id)
    
    async def check_voice_logs(server):
        import re
        channel = server.get_channel(VC_LOG_ID)
        async for message in channel.history(after=result_date):
            if message.embeds:
                for embed in message.embeds:
                    if embed.description:
                        if "voice" in embed.description:
                            match = re.search(r"<@(\d+)>", embed.description)
                            if match:
                                id = int(match.group(1))
                                talked.append(id)

    async def kick_members(server, arr):
        will_be_kicked = []
        for member in server.members:
            if member.id not in talked and not member.bot and member.id != bot.user.id and member.id != server.owner.id:
                join_date = member.joined_at.replace(tzinfo=None)
                if join_date < result_date:
        
                    print(member.name + " will be kicked")
                    will_be_kicked.append(member.id)
        
        if len(will_be_kicked) == 0:
            print("No one will be kicked")
        
        await bot.close()
    
    bot.run(BOT_TOKEN)



#Setup

def setup_venv():
    import os
    import subprocess
    import platform
    import venv

    env_dir = "./.venv"

    print("Creating virtual enviroment and installing neccesary packages")
    venv.create(env_dir, with_pip=True)
    pip_path = os.path.join(env_dir, 'Scripts', 'pip') if platform.system() == 'Windows' else os.path.join(env_dir, 'bin', 'pip')
    subprocess.check_call([pip_path, 'install', '-r', 'requirements.txt'])

    print("Running script")
    python_path = os.path.join(env_dir, 'Scripts', 'python') if platform.system() == 'Windows' else os.path.join(env_dir, 'bin', 'python')
    subprocess.check_call([python_path, 'run.py', "-run"])



#Main

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-run":    
        run_script()
    else:
        setup_venv()

if __name__ == "__main__":
    main()