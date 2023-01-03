// Dynatrace workflow action to simulate and ingest of demo metrics
// 
import { coreClient } from '@dynatrace-sdk/client-core';
import { metricsClient } from '@dynatrace-sdk/client-classic-environment-v2';

function rand(min, max) {
  return Math.floor(min + Math.random()*(max - min + 1))
}

export default async function({execution_id}) {      
  // your code goes here
  const today = new Date();
  const year  = today.getFullYear();
  const month = (today.getMonth() + 1).toString().padStart(2, "0");
  const day   = today.getDate().toString().padStart(2, "0");
  
  const level_1 = 75 - day;
  const level_2 = 30 - day;

  var metricBody = "host.disk.free,hostname=prod-useast-01,diskname=c " + (level_1 + rand(0, 5)) + "\n";
  metricBody += "host.disk.free,hostname=prod-useast-01,diskname=mnt " + (50 + rand(0, 5)) + "\n"
  metricBody += "host.disk.free,hostname=prod-sydney-05,diskname=/ " + (level_2 + rand(0, 3)) + "\n"
  metricBody += "host.disk.free,hostname=prod-sydney-05,diskname=/root " + (40 + rand(0, 5)) + "\n"
  // add metrics below

  
  // log out the complete metric ingest payload    
  console.log(metricBody);
  
  const c = {
    body : metricBody
  }
  
  const result = await metricsClient.ingest(c);
  console.log(result);
}