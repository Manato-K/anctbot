import discord
import sys
from discord.ext.commands import Bot

token = 'token'

client = discord.Client()
bot = Bot("!")


@client.event
async def on_ready():
    CHANNEL_ID = number
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('ログインしたうお\nコマンド知らない場合は\n-help\nと入力してね')
    print('ログインしました。')


@client.event
async def on_member_join(member):
    ms = f'{member.mention}学生会へようこそ！\n-(ハイフン小文字)の後に学年を入力して送信してね\n例-1年生'
    await client.get_channel(number).send(ms)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '-help':
        await message.channel.send('''
        ```
        -x年生 //学年役職を設定
        -xE 姓 名 //ニックネームの設定
        -goodbye //botさよならバイバイ
        -fuck //学年役職を外す
        -nick 後ろに名前入力//ニックネームの変更
        -cleanup //チャンネル履歴削除
        役職設定:
        -1年生 //1年生のロールが付きます
        -2年生 //2年生のロールが付きます
        -3年生 //3年生のロールが付きます
        -4年生 //4年生のロールが付きます
        -5年生 //5年生のロールが付きます
        -監査 //監査のロールが付きます
        ```
        ''')
    if message.content == '-cleanup':
        if message.author.guild_permissions.adminidtrator:
            await message.channel.purge()
            await message.channel.send('チャンネル履歴を削除したよ！')
        else:
            await message.channel.send('おめぇにそんな権限はねぇ！！')
    if message.content == '-musichelp':
        await message.channel.send('''
        ```
        -play
        -
        ''')
    if message.content == '-helps':
        await message.channel.send('-fuckと送って役職を消してね\nそうしたらもう一回\n-(ハイフン小文字)の後に学年を入力して送信してね')

    if message.content == '-goodbye':
        await message.channel.send('''
        グッバイ
        ''')
        await client.logout()
        await sys.exit()

    if message.content.startswith('-nick'):
        test = message.content.lstrip('-nick')
        await message.author.edit(nick=test)
        reply = f'{message.author.mention}ニックネームを変更しました！'
        await message.channel.send(reply)

    if message.content == '-1年生' or message.content == '-１年生':
        role = discord.utils.get(message.guild.roles, name='1年生')
        await message.author.add_roles(role)
        reply = f'{message.author.mention}学年役職を付けたよ\n次は-(ハイフン小文字)の後にじ自分の学年名前を入力してね(例: -4E 〇〇 〇〇 )\nもし間違えたら-helps\nと打ってね'
        await message.channel.send(reply)
    elif message.content == '-fuck':
        role = discord.utils.get(message.guild.roles, name='1年生')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention}学年の役職を取り消したよ！'
        await message.channel.send(reply)

    if message.content == '-2年生' or message.content == '-２年生':
        role = discord.utils.get(message.guild.roles, name='2年生')
        await message.author.add_roles(role)
        reply = f'{message.author.mention}学年役職を付けたよ\n次は-(ハイフン小文字)の後にじ自分の学年名前を入力してね(例: -4E 〇〇 〇〇 )\nもし間違えたら-helps\nと打ってね'
        await message.channel.send(reply)
    elif message.content == '-fuck':
        role = discord.utils.get(message.guild.roles, name='2年生')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention}学年の役職を取り消したよ！'
        await message.channel.send(reply)

    if message.content == '-3年生' or message.content == '-３年生':
        role = discord.utils.get(message.guild.roles, name='3年生')
        await message.author.add_roles(role)
        reply = f'{message.mention}学年役職を付けたよ次\nは-(ハイフン小文字)の後にじ自分の学年名前を入力してね(例: -4E 〇〇 〇〇 )\nもし間違えたら-helps\nと打ってね'
        await message.channel.send(reply)
    elif message.content == '-fuck':
        role = discord.utils.get(message.guild.roles, name='3年生')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention}学年の役職を取り消したよ！'
        await message.channel.send(reply)

    if message.content == '-4年生' or message.content == '-４年生':
        role = discord.utils.get(message.guild.roles, name='4年生')
        await message.author.add_roles(role)
        reply = f'{message.mention}学年役職を付けたよ\n次は-(ハイフン小文字)の後にじ自分の学年名前を入力してね(例: -4E 〇〇 〇〇 )\nもし間違えたら-helps\nと打ってね'
        await message.channel.send(reply)
    elif message.content == '-fuck':
        role = discord.utils.get(message.guild.roles, name='4年生')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention}学年の役職を取り消したよ！'
        await message.channel.send(reply)

    if message.content == '-5年生' or message.content == '-５年生':
        role = discord.utils.get(message.guild.roles, name='5年生')
        await message.author.add_roles(role)
        reply = f'{message.mention}学年役職を付けたよ\n次は-(ハイフン小文字)の後にじ自分の学年名前を入力してね(例: -4E 〇〇 〇〇 )\nもし間違えたら-helps\nと打ってね'
        await message.channel.send(reply)
    elif message.content == '-fuck':
        role = discord.utils.get(message.guild.roles, name='5年生')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention}学年の役職を取り消したよ！'
        await message.channel.send(reply)

    if message.content == '-監査' or message.content == 'ー監査':
        role = discord.utils.get(message.guild.roles, name='監査')
        await message.author.add_roles(role)
        reply = f'{message.mention}に監査の役職を付けた'
        await message.channel.send(reply)

    # mugi
    if message.content.startswith('-del'):
        if message.author.guild_permissions.administrator:
            role = discord.get_role(message.content.lstrip('-del'))


@bot.event
async def on_message_error(ctx, error):
    ch = 583226074272497672
    embed = discord.Embed(title="エラー情報", description="", color=0xf00)
    embed.add_field(name="エラー発生:サーバー名", value=ctx.guild.name, inline=False)
    embed.add_field(name="エラー発生:サーバーID", value=ctx.guild.name, inline=False)
    embed.add_field(name="エラー発生:ユーザー名", value=ctx.guild.name, inline=False)
    embed.add_field(name="エラー発生:ユーザーiD", value=ctx.guild.name, inline=False)
    embed.add_field(name="発生エラー", value=error, inline=False)

    m = await bot.get_channel(ch).send(embed=embed)
    await ctx.send(f"エラー発生！！！ごめんなさいちょっと待ってね")


client.run(token)
