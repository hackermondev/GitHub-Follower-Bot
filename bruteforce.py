import random

words = list('abcdefghijklmnopqrstuvwxyz1234567890')

def generate_text(length):
  text = ''
  for i in range(0, length):
    text += random.choice(words)
  return text
