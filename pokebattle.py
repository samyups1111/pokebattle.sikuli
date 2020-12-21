import time

while True:
      if exists("1607732027116.png"):
          click(Pattern("1607730227353.png").targetOffset(-63,-18))
          wait("1607784230440.png")
          click(Pattern("1607784230440.png").targetOffset(-79,-29))
          time.sleep(8.5)
      elif exists("1607749912573.png"):  
          click(Pattern("1607749912573.png").targetOffset(249,0)) 
          while exists(Pattern("1607749912573.png").targetOffset(249,0)):
              keyDown(Key.LEFT)
              time.sleep(.25)
              keyUp()
              keyDown(Key.RIGHT)
              time.sleep(.5)
              keyUp()
      elif exists(Pattern("1607789365226.png").similar(0.58)):
          click(Pattern("1607789365226.png").similar(0.57))
          while exists(Pattern("1607789365226.png").similar(0.57)):
              keyDown(Key.LEFT)
              time.sleep(.25)
              keyUp()
              keyDown(Key.RIGHT)
              time.sleep(.5)
              keyUp()
      else:
          break
    
