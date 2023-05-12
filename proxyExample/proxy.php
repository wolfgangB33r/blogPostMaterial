<?php
    // Get the config from GitHub
    $json = file_get_contents('https://raw.githubusercontent.com/wolfgangB33r/metric/master/proxyexample.json');
    $obj = json_decode($json);
    // Add artifical slowdowns here
    usleep($obj->proxydelayms * 1000);
    // Forward the X-Dynatrace tracing header here
    $dtheader = '';
    $headers =  getallheaders();
    foreach($headers as $key=>$val){
        if(strcasecmp($key, 'X-Dynatrace') == 0) {
            $dtheader = $val;
        }
    }
    // Simulate a fail (500 return in case the GitHub config sais so)
    if($obj->proxyreturn == '200')
    {
        $ch = curl_init("http://DYNATRACE_MONITORED_DESTINATION_ENDPOINT"); 
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
            'X-Dynatrace: ' . $dtheader,
            'test: ' . 'wolfgang'
        ));
        
        $data = curl_exec($ch);
        curl_close($ch);

    } else {
        http_response_code( $obj->proxyreturn );
    }
     
?>
