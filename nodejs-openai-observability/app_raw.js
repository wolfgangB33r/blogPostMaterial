const http = require('http');
const https = require('https');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    var post_data = JSON.stringify({
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Say this is a test!"}],
        "temperature": 0.7
      });

    // An object of options to indicate where to post to
    var post_options = {
        host: 'api.openai.com',
        port: '443',
        path: '/v1/chat/completions',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + process.env.OPENAI_API_KEY,
            'Content-Length': Buffer.byteLength(post_data)
        }
    };

    var req = https.request(post_options, (resp) => {
        let data = '';
        // A chunk of data has been received.
        resp.on('data', (chunk) => {
            console.log("Chunk" + chunk);
            data += chunk;
        });
        // The complete response has been received. 
        resp.on('end', () => {
            console.log(JSON.parse(data));
            res.statusCode = 200;
            res.setHeader('Content-Type', 'text/plain');
            res.end('Ok');
        });
      
      }).on("error", (err) => {
        res.statusCode = 500;
        res.setHeader('Content-Type', 'text/plain');
        res.end("Error: " + err.message);
      });

      req.write(post_data);
      req.end();

});

server.listen(port, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});