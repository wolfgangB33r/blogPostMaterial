const http = require('http');
const https = require('https');
var url = require('url');

const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY
});
const openai = new OpenAIApi(configuration);

const hostname = '127.0.0.1';
const port = 8080;

function report_metric(openai_response) {
  var post_data = "openai.promt_token_count,model=" + openai_response.model + " " + openai_response.usage.prompt_tokens + "\n";
  post_data += "openai.completion_token_count,model=" + openai_response.model + " " + openai_response.usage.completion_tokens + "\n";
  post_data += "openai.total_token_count,model=" + openai_response.model + " " + openai_response.usage.total_tokens + "\n";
  console.log(post_data);
  var post_options = {
    host: 'localhost',
    port: '14499',
    path: '/metrics/ingest',
    method: 'POST',
    headers: {
      'Content-Type': 'text/plain',
      'Content-Length': Buffer.byteLength(post_data)
    }
  };
  var metric_req = http.request(post_options, (resp) => {}).on("error", (err) => { console.log(err); });
  metric_req.write(post_data);
  metric_req.end();
}

const server = http.createServer(async (req, res) => {
  var params = url.parse(req.url, true).query;
  
  console.log(url.parse(req.url, true).pathname);
    
  if (url.parse(req.url, true).pathname == '/' && params.prompt) {
    try {
      const response = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: params.prompt,
        temperature: 0,
        max_tokens: 10,
      });
      console.log(response);
      const completion = response.data.choices[0].text;
      report_metric(response.data);
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/plain');
      res.end(completion);
    } catch (error){
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end("Error");
    }
  } else {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end("You asked for nothing!");
  }
});

server.listen(port, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});