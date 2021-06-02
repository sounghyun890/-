import asyncio
import discord,os

client = discord.Client()


@client.event
async def on_ready():
    print("로그인 된 봇:") #화면에 봇의 아이디, 닉네임이 출력되는 코드
    print(client.user.name)
    print(client.user.id)
    print("===========")
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("TNS(TANAT STUDIO) 베타 테스트")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game("신천고 검열봇")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game("!도움 듣는 중")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)        
# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
        


# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot:
        return None 

    id = message.author.id
    channel = message.channel

    if message.content.startswith('안녕'):
        channel = message.channel
        await channel.send('안녕하세요 저희채널에 오신걸 환영합니다')

    if message.content == "!도움":
        embed = discord.Embed(title = "TNS 봇의 도움말", description = '''
        욕 검열 봇입니다
욕 추가 및 수정을 원하시면 타나트TANAT#2601
을 추가해주세요''', color = 0x8258FA)
        await message.author.send(embed = embed)
        await message.delete()
    if message.author.bot:
    
        await message.author.send(embed = embed) # message.channel.send를 message.author.send로
    message_content = message.content
    
    bad = message_content.find("ㅅㅂ")
    bad = bad + message_content.find("ㅂㅅ")
    bad = bad + message_content.find("ㅄ")
    bad = bad + message_content.find("씨발")
    bad = bad + message_content.find("닥쳐")
    bad = bad + message_content.find("꺼져")
    bad = bad + message_content.find("느금마")
    bad = bad + message_content.find("잘생김")
    bad = bad + message_content.find("니 엄마")
    bad = bad + message_content.find("지랄")
    bad = bad + message_content.find("싸발")
    bad = bad + message_content.find("좇")
    bad = bad + message_content.find("ㅈㄴ")
    bad = bad + message_content.find("ㅈㄹ")
    bad = bad + message_content.find("ㄴㄱㅁ")
    bad = bad + message_content.find("좆")
    bad = bad + message_content.find("시발")
    bad = bad - message_content.find("시발점")
    bad = bad + message_content.find("ㄲㅈ")
    bad = bad + message_content.find("쌔끼")
    bad = bad + message_content.find("fuck")
    bad = bad + message_content.find("Tlqkf")
    bad = bad + message_content.find("tlqkf")
    bad = bad + message_content.find("병신")
    bad = bad + message_content.find("박근혜")
    bad = bad + message_content.find("섹스")
    bad = bad + message_content.find("보지")
    bad = bad - message_content.find("보지마")
    bad = bad + message_content.find("쉣")
    bad = bad + message_content.find("너의 어머니")
    bad = bad + message_content.find("샤발")
    bad = bad + message_content.find("섹 스")
    bad = bad + message_content.find("씨 발")
    bad = bad + message_content.find("닥ㅊ")
    bad = bad + message_content.find("ㅈㄹㄴ")
    bad = bad + message_content.find("병 신")
    bad = bad + message_content.find("*발")
    bad = bad + message_content.find("*신")
    bad = bad + message_content.find("야발")
    bad = bad + message_content.find("ㅅ1ㅂ")#35
    bad = bad + message_content.find("조까")
    bad = bad + message_content.find("퍽큐")
    bad = bad + message_content.find("ㅗㅗ")
    bad = bad + message_content.find("븅신")
    bad = bad + message_content.find("따까리")
    bad = bad + message_content.find("새끼")
    bad = bad + message_content.find("찐따")
    bad = bad + message_content.find("porn")
    bad = bad + message_content.find("빠큐")
    bad = bad + message_content.find("시놈발")
    
    
    if bad >= -45 :
        a = await message.channel.send(message.author.mention+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]")
        await message.delete()
        await asyncio.sleep(3)
        await a.delete()
    await bot.process_commands(messsage)

access_token = os.environ["token"]
client.run(access_token)
