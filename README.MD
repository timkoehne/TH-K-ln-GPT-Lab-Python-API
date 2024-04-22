# TH Köln GPT-Lab Python API
This project provides a python interface to access GPT4 through [TH Köln GPT-Lab](https://ki.th-koeln.de/interface.php). 
Just like the website this only works from within the university network (vpn) and with a valid CampusID login.


# Preparation
This uses your browsers cookies to login so you need to provide it once.


You'll need to use the browsers development tools to find these and save them into ```cookies.json``` according to ```cookies_template.json```. After sending a message you should be able to find your cookies in the network tab like this:
![img](extra/where%20to%20find%20cookies.png)

After that your login should be valid for a while. If it becomes invalid just login using your browser, since they share the same cookie this also refreshes your api login.



# Usage
## Conversation with continuous context
```python
>>> from th_gpt import TH_GPT
>>> chat = TH_GPT()
>>> chat.send_message("How tall is the Empire State Building in meters?")
'The Empire State Building is 381 meters tall, not including its antennas.'
>>> chat.send_message("How many feet is that?")
'The Empire State Building is 1,250 feet tall, excluding its antennas.'
```

## Conversation without continuous context
```python
>>> from th_gpt import TH_GPT
>>> chat = TH_GPT()
>>> chat.send_message_without_context("How tall is the Empire State Building in meters?") 
'The Empire State Building is 381 meters tall, not including its antenna.'
>>> chat.send_message_without_context("How many feet is that?")
'Can you specify the measurement you need converted into feet?'

```