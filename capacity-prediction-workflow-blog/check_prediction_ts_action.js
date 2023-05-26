import { execution } from '@dynatrace-sdk/automation-utils';

const THRESHOLD = 5;
const TASK_ID = 'predict_disc_capacity';

export default async function ({ execution_id }) {
  const exe = await execution(execution_id);
  const predResult = await exe.result(TASK_ID);
  const result = predResult['result'];
  const predictionSummary = { violation: false, violations: new Array<Record<string, string>>() };
  console.log("Total number of predicted lines: " + result.output.length);
  // Check if prediction was successful.
  if (result.resultStatus == 'SUCCESSFUL' && result.executionStatus == 'COMPLETED') {
    console.log('Prediction was successful.')
    // Check each predicted result, if it violates the threshold.
    for (let i = 0; i < result.output.length; i++) {
      const prediction = result.output[i];
      // Check if the prediction result is considered valid
      if (prediction.analysisStatus == 'OK' && prediction.forecastQualityAssessment == 'VALID') {
        const lowerPredictions = prediction.timeSeriesDataWithPredictions.records[0]['dt.davis.forecast:lower'];
        const lastValue = lowerPredictions[lowerPredictions.length-1];
        // check against the threshold
        if (lastValue < THRESHOLD) {
          predictionSummary.violation = true;
          // we need to remember all metric properties in the result, 
          // to inform the next actions which disk ran out of space
          predictionSummary.violations.push(prediction.timeSeriesDataWithPredictions.records[0]);
        }
      }
    }
    console.log(predictionSummary.violations.length == 0 ? 'No violations found :)' : '' + predictionSummary.violations.length + ' capacity shortages were found!')
    return predictionSummary;
  } else {
    console.log('Prediction run failed!');
  }
}