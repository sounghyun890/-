import asyncio
import discord,os
import datetime

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
        game = discord.Game("욕 찾기")#상태 메세지
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game("!도움 듣는 중")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)        
# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
        
now = datetime.datetime.now()
time = f"{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분"

@client.event
async def on_message_delete(message):#메세지가 삭제 되면
    if message.author.bot:return
    channel = client.get_channel(849536197273059338)
    embed = discord.Embed(title=f"삭제됨", description=f"유저 : {message.author.display_name}({message.author}) \n서버 : {message.guild.name} \n채널 : {message.channel.mention}", color=0xFF0000)
    embed.add_field(name="삭제된 내용", value=f"내용 : {message.content}", inline=False)
    embed.set_footer(text=f"TNS 봇 | {time}")
    await channel.send(embed=embed)


@client.event    
async def on_message_edit(before, after):#메세지 수정 되면(작동 안함)
    if message.author.bot:return
    channel = client.get_channel(849536197273059338)
    embed = discord.Embed(title=f"수정됨", description=f"유저 : {before.author.mention} 채널 : {before.channel.mention}", color=0xFF9900)
    embed.add_field(name="수정 전 내용", value=before.content, inline=True)
    embed.add_field(name="수정 후 내용", value=after.content, inline=True)
    embed.set_footer(text=f"{before.guild.name} | {time}")
    await channel.send(embed=embed)

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot:
        return None 

    id = message.author.id
    channel = message.channel

    if message.content == "!도움":
        embed = discord.Embed(title = "TNS 봇의 도움말", description = '''
        욕 검열 봇입니다
욕 추가 및 수정을 원하시면 로그 서버의 버그 리포트 채팅방을 이용해주세요

봇 로그 보러가기 https://discord.gg/hFryJ4zYyw

하트 누르러 가기 https://koreanbots.dev/bots/848795383751639080''', color = 0x08FFFA)
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
    bad = bad + message_content.find("ㅗ")
    bad = bad + message_content.find("븅신")
    bad = bad + message_content.find("따까리")
    bad = bad + message_content.find("새끼")
    bad = bad + message_content.find("찐따")
    bad = bad + message_content.find("porn")
    bad = bad + message_content.find("빠큐")
    bad = bad + message_content.find("시놈발")
    bad = bad + message_content.find("시이발")
    bad = bad + message_content.find("ㅅ ㅂ")#47
    bad = bad + message_content.find("미친")
    bad = bad + message_content.find("ㄷㅊ")
    bad = bad + message_content.find("ㄷ ㅊ")#51
    bad = bad + message_content.find("자지")
    bad = bad - message_content.find("자지마")#50
    bad = bad + message_content.find("폐륜")
    bad = bad + message_content.find("불알")
    bad = bad + message_content.find("ㅈ같")
    bad = bad + message_content.find("ㅈ랄")
    bad = bad + message_content.find("기모찌")
    bad = bad + message_content.find("자위")
    bad = bad + message_content.find("딸딸이")
    bad = bad + message_content.find("TLQKF")
    bad = bad + message_content.find("SEX")
    bad = bad + message_content.find("Sex")
    bad = bad + message_content.find("섹슥")
    bad = bad + message_content.find("미친놈")
    bad = bad + message_content.find("싸가지")
    bad = bad - message_content.find("ㅗㅜㅑ")
    bad = bad - message_content.find("개세끼")
    bad = bad - message_content.find("게세끼")
    bad = bad - message_content.find("씌발")
            
    
    
    if bad >= -65 :
        a = await message.channel.send(message.author.mention+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]")
        await message.delete() 
        await asyncio.sleep(7)
        await a.delete()
    await bot.process_commands(messsage)

access_token = os.environ["token"]
client.run(access_token)
