import { eventsClient, EventIngestEventType } from "@dynatrace-sdk/client-classic-environment-v2";
import { execution } from '@dynatrace-sdk/automation-utils';

export default async function ({ execution_id }) {
  const exe = await execution(execution_id);
  const checkResult = await exe.result('check_prediction');
  const violations = await checkResult.violations;
  // Raise an event for each violation
  violations.forEach(function (violation) {
    eventsClient.createEvent({ 
      body : {
        eventType: EventIngestEventType.ResourceContentionEvent,
        title: 'Predictive Disk Capacity Alarm',
        entitySelector: 'type(DISK),entityId("' + violation['dt.entity.disk'] + '")',
        properties: {
          'dt.entity.host' : violation['dt.entity.host']
        }
      }
    }); 
  });  
};