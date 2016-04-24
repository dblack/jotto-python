import player
c = player.Computer()

print c.secret_word

while c.guessed_humans_word is not True:
  c.guess_humans_word()
