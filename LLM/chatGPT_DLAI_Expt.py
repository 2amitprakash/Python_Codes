import openai
import os
from IPython.display import display, HTML

openai.api_key  = os.getenv('OPENAI_API_KEY')

# Helper function
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

##########################
text_2 = f"""
First, you'll tokenize the input words using this same tokenizer that was used \
to train the network. These tokens are then added into the input on the encoder \
side of the network, passed through the embedding layer, and then fed into the \
multi-headed attention layers. The outputs of the multi-headed attention layers \
are fed through a feed-forward network to the output of the encoder. At this \
point, the data that leaves the encoder is a deep representation of the \
structure and meaning of the input sequence. This representation is inserted \
into the middle of the decoder to influence the decoder's self-attention mechanisms. \
Next, a start of sequence token is added to the input of the decoder. This triggers \
the decoder to predict the next token, which it does based on the contextual \
understanding that it's being provided from the encoder. The output of the decoder's \
self-attention layers gets passed through the decoder feed-forward network and \
through a final softmax output layer. At this point, we have our first token. \
You'll continue this loop, passing the output token back to the input to trigger \
the generation of the next token, until the model predicts an end-of-sequence token. \
At this point, the final sequence of tokens can be detokenized into words, and you have your output.
"""
prompt = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions, \ 
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \ 
then simply write \"No steps provided.\"

\"\"\"{text_2}\"\"\"
"""
response = get_completion(prompt)
print(response)
