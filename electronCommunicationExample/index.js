// In main process.
const { app, BrowserWindow, ipcMain } = require('electron')

function createWindow () {
  // Create the browser window.
  let win = new BrowserWindow({ width: 800, height: 600 })

  // and load the index.html of the app.
  win.loadFile('index.html')
}

app.on('ready', createWindow)

ipcMain.on('asynchronous-message', (event, arg) => {
  console.log(arg) // prints "ping"
  event.sender.send('asynchronous-reply', 'pong')
})

ipcMain.on('synchronous-message', (event, arg) => {
	console.log(arg) // prints "ping"
	event.returnValue = 'pong'
})
