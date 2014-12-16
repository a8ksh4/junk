#/usr/local/bin/forever /usr/local/bin/nodemon --exitcrash /webgame/node/server.js
forever -w --watchDirectory `pwd` server.js
