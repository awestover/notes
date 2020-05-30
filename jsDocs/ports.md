## port forwarding / tunelling

ngrok is ok

localhost.run is really nice (no download beyond openssh-server)
ssh -R 80:localhost:3000 ssh.localhost.run

localtunnel (from npm)
is ok
lt -s nameofthing -p 3000 

none of these require router config stuff

all should be cross platform

ngrok kinda works

but localtunnel is super cool

npm install -g localtunnel
lt --subdomain X --port 3000



