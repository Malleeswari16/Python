import re
import sys
def detect_text_origin (text):
  if re.search(r'\b(embark | delve) \b', text): 
    return "AI-generated text was detected."
  else:
    return "Human-written."
if __name__ == "__main__":
  text = " ".join(sys.argv[1:])
  print(detect_text_origin(text))
