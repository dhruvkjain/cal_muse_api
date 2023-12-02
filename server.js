const express = require('express');
const app = express();
app.use(express.json({ extended: false }));
const cors = require('cors');
app.use(cors());  

const { spawn } = require('child_process');

spawn('pip install numpy',(error, stdout, stderr) => {
  if (error) {
    console.error(`Error installing numpy: numpy`);
    return;
  }

  // Output of the npm install command
  console.log(`Package numpy installed successfully`);
  console.log(`stdout: ${stdout}`);
  console.log(`stderr: ${stderr}`);
});



app.post('/plot',(req,res)=>{
  
  // const pythonProcess = spawn('python', ['test.py', req.body.x, req.body.y, req.body.z, req.body.k, '.\jpg']);

  // pythonProcess.stdout.on('data', (data) => {
  //   // console.log(`Python stdout: ${data}`); 
  //   res.send(data);
  // });
  // pythonProcess.stderr.on('data', (data) => {
  //   console.error(`Python stderr: ${data}`);
  //   res.status(400).json(data);
  // });
  // pythonProcess.on('close', (code) => {
  //   console.log(`Python process exited with code ${code}`);
  // });
})


const PORT = process.env.PORT || 3000
app.listen(PORT);