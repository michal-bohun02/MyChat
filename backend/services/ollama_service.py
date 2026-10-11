from ollama import AsyncClient

async def send_prompt(messages):

  stream = await AsyncClient().chat(
    model='qwen2.5:7b',
    messages=messages,
    stream=True,
  )

  return stream

async def get_answer(stream,messages):
  in_thinking = False
  content = ''
  thinking = ''
  async for chunk in stream:
    if chunk.message.thinking:
      if not in_thinking:
        in_thinking = True
        print('Thinking:\n', end='', flush=True)
      print(chunk.message.thinking, end='', flush=True)
      thinking += chunk.message.thinking
    elif chunk.message.content:
      if in_thinking:
        in_thinking = False
        print('\n\nAnswer:\n', end='', flush=True)
      # print(chunk.message.content, end='', flush=True)
      content += chunk.message.content
  messages.append({ 'role': 'assistant', 'thinking': thinking, 'content': content })
  return {"content": content}
