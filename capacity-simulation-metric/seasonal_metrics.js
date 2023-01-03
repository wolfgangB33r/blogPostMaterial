// This action continously simulates metrics with variable seasonality
// 
import { coreClient } from '@dynatrace-sdk/client-core';
import { metricsClient } from '@dynatrace-sdk/client-classic-environment-v2';

const METRIC_NAME_PREFIX = "sim.seasonal" 
const PERIODS_MIN = [15, 60, 6 * 60, 24 * 60]
const NOISE_LEVEL = [0, 1, 2, 3, 5]

function rand(min, max) {
  return Math.floor(min + Math.random()*(max - min + 1))
}

function seasonal_generator(period_minutes, noise_level, minute) {
    return (Math.cos(2 * Math.PI * minute / period_minutes) * 10) + 10 + Math.random() * noise_level;
}

export default async function({execution_id}) {      
  const today = new Date();
  
  var metricBody = "";
  var minutes = today.getTime() / 1000 / 60;

  for (let p = 0; p < PERIODS_MIN.length; p++) {
    for (let n = 0; n < NOISE_LEVEL.length; n++) {
      var mkey = "_" + NOISE_LEVEL[n] + "_" + PERIODS_MIN[p];
      var value = seasonal_generator(PERIODS_MIN[p], NOISE_LEVEL[n], minutes);
      metricBody += METRIC_NAME_PREFIX + mkey + ",key1=value1 " + value + "\n";
    }
  }
  console.log(metricBody);
  
  const c = {
    body : metricBody
  }
  
  const result = await metricsClient.ingest(c);
  console.log(result);
}