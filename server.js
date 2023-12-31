const express = require('express');
const app = express();
app.use(express.json({ extended: false }));
const cors = require('cors');
app.use(cors());  

const { spawn } = require('child_process');


// -----------------------------------------------------------------------
const installProcessn = spawn('pip', ['install', 'numpy']);
installProcessn.on('close', (code) => {
  if (code === 0) {
    console.log(`Package numpy installed successfully`);
  } else {
    console.error(`Error installing numpy`);
  }
});
installProcessn.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});
installProcessn.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

// -----------------------------------------------------------------------
const installProcessscipy = spawn('pip', ['install', 'scipy']);
installProcessscipy.on('close', (code) => {
  if (code === 0) {
    console.log(`Package scipy installed successfully`);
  } else {
    console.error(`Error installing scipy`);
  }
});
installProcessscipy.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});
installProcessscipy.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});


// -----------------------------------------------------------------------
const installProcessmatplotlib = spawn('pip', ['install', 'matplotlib']);
installProcessmatplotlib.on('close', (code) => {
  if (code === 0) {
    console.log(`Package matplotlib installed successfully`);
  } else {
    console.error(`Error installing matplotlib`);
  }
});
installProcessmatplotlib.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});
installProcessmatplotlib.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

// -----------------------------------------------------------------------
const installProcessmpl_toolkits = spawn('pip', ['install', 'pypuf']);
installProcessmpl_toolkits.on('close', (code) => {
  if (code === 0) {
    console.log(`Package pypuf installed successfully`);
  } else {
    console.error(`Error installing pypuf`);
  }
});
installProcessmpl_toolkits.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});
installProcessmpl_toolkits.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});






app.post('/plot',(req,res)=>{
  
  let ranNum ;
  // setTimeout(()=>{
    const pythonProcess = spawn('python', ['test.py', req.body.x, req.body.y, req.body.z, '.\jpg']);
    pythonProcess.stdout.on('data', (data) => {
      ranNum = data;
      res.send(data);
    });
    pythonProcess.stderr.on('data', (data) => {
      ranNum = "problem";
      res.status(400).json("problem");
    });
  // } , 10000)
})


const PORT = process.env.PORT || 3000
app.listen(PORT);