
# this is just some info on how to use electron

Basic setup:

npm init
echo "node_modules/" >> .gitignore
npm install --save-dev electron

touch index.html
touch index.js

in index.js (the main process)
  put a require('electron')

  good hello world:
    const { app, BrowserWindow } = require('electron')

    function createWindow () {
      // Create the browser window.
      let win = new BrowserWindow({ width: 800, height: 600 })

      // and load the index.html of the app.
      win.loadFile('index.html')
    }

    app.on('ready', createWindow)

in index.html (the main website)
  just put a website

ipc is a super good thing to include
it basically allows communication between the main process and the main website (or really any render process)


# useful resources

  [first-app](https://electronjs.org/docs/tutorial/first-app)
  [ipc-main](https://electronjs.org/docs/api/ipc-main)



