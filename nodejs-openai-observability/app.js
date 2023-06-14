const http = require('http');
const https = require('https');
var url = require('url');

const { createLogger, format, transports } = require('winston');
const { combine, timestamp, label, prettyPrint } = format;

const logger = createLogger({
  level: 'info',
  format: combine(
    timestamp(),
    prettyPrint()
  ),
  defaultMeta: { service: 'openai-client-service' },
  transports: [
    new transports.File({ filename: 'openai.log' }),
  ],
});

const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY
});
const openai = new OpenAIApi(configuration);

const hostname = '127.0.0.1';
const port = 8090;

function report_metric(openai_response) {
  var post_data = "openai.promt_token_count,model=" + openai_response.model + " " + openai_response.usage.prompt_tokens + "\n";
  post_data += "openai.completion_token_count,model=" + openai_response.model + " " + openai_response.usage.completion_tokens + "\n";
  post_data += "openai.total_token_count,model=" + openai_response.model + " " + openai_response.usage.total_tokens + "\n";
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
  var metric_req = http.request(post_options, (resp) => {}).on("error", (err) => { 
    logger.log('error', `OpenAI error ${err}`);
  });
  metric_req.write(post_data);
  metric_req.end();
}

const server = http.createServer(async (req, res) => {
  var params = url.parse(req.url, true).query;
  logger.log('info', `endpoint called ${url.parse(req.url, true).pathname}`);
  if (url.parse(req.url, true).pathname == '/' && params.prompt) {
    try {
      const response = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: params.prompt,
        temperature: 0,
        max_tokens: 10,
      });
      const completion = response.data.choices[0].text;
      report_metric(response.data);
      // log completion
      logger.log('info', `OpenAI response promt_tokens:${response.data.usage.prompt_tokens} completion_tokens:${response.data.usage.completion_tokens} total_tokens:${response.data.usage.total_tokens}`);
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
  logger.log('info', `Server running at http://${hostname}:${port}/`);
});