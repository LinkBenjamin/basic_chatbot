from gpt4all import GPT4All

model = GPT4All('orca-mini-3b-gguf2-q4_0.gguf', allow_download=False)

system_prompt = '### System:\nYou are an AI assistant that follows instructions very well.  Help as much as you can.\n\n'
prompt_template = '### User:\n{0}\n\n### Response:\n'

with model.chat_session(system_prompt, prompt_template):
    while True:
        user_input = input("User:")
        if 'quit' in user_input.lower():
            break
        else:
            print(f"\n\n{model.generate(user_input)}\n\n")
