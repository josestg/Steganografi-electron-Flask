const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;


var mainWindow = null;

app.on('window-all-closed', function() {
  //if (process.platform != 'darwin') {
    app.quit();
  //}
});

app.on('ready', function() {
  // call python?
  var subpy = require('child_process').spawn('python', ['../server/run.py']);
  //var subpy = require('child_process').spawn('./dist/hello.exe');
  var rq = require('request-promise');
  var mainAddr = 'http://127.0.0.1:1337/';

  var openWindow = function(){
    mainWindow = new BrowserWindow({
      width: 800, 
      height: 600,
      webPreferences: {
        nodeIntegration: false,
        preload: './preload.js'
      }
    });
    // mainWindow.loadURL('file://' + __dirname + '/index.html');
    mainWindow.loadURL('http://127.0.0.1:1337/');
    // mainWindow.webContents.openDevTools();
    mainWindow.on('closed', function() {
      mainWindow = null;
      subpy.kill('SIGINT');
    });
  };

  var startUp = function(){
    rq(mainAddr)
      .then(function(htmlString){
        console.log('server started!');
        openWindow();
      })
      .catch(function(err){
        startUp();
      });
  };

  // fire!
  startUp();
});
