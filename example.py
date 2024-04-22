# Remembering Context
>>> from th_gpt import TH_GPT
>>> chat = TH_GPT()
>>> chat.send_message("How tall is the Empire State Building in meters? Short answer.")
'The Empire State Building is 381 meters tall, not including its antennas.'
>>> chat.send_message("How many feet is that? Short answer.")
'The Empire State Building is 1,250 feet tall, excluding its antennas.'


# Without remembering Context
>>> from th_gpt import TH_GPT
>>> chat = TH_GPT()
>>> chat.send_message_without_context("How tall is the Empire State Building in meters? Short answer.") 
'The Empire State Building is 381 meters tall, not including its antenna.'
>>> chat.send_message_without_context("How many feet is that? Short answer.")
'Can you specify the measurement you need converted into feet?'