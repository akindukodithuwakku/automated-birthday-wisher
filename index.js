const functions = require('firebase-functions');
const { exec } = require('child_process');
const path = require('path');

// Define a cloud function to send birthday emails
exports.sendBirthdayEmails = functions.pubsub.schedule('every 24 hours').onRun((context) => {
  // Path to your Python script
  const scriptPath = path.join(__dirname, 'send_birthday_emails.py');

  // Execute the Python script
  exec(`python ${scriptPath}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing script: ${error.message}`);
      return;
    }

    if (stderr) {
      console.error(`Script error output: ${stderr}`);
      return;
    }

    console.log(`Script output: ${stdout}`);
  });

  return null;
});
