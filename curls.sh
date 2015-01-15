#!/bin/bash
rm curl_out.txt
echo 'curl -X GET "google.com"'
curl -X GET 'google.com' >> curl_out.txt
echo 'curl -X GET "slashdot.org"'
curl -X GET 'slashdot.org' >> curl_out.txt
echo 'curl -X HEAD "slashdot.org"'
curl -X HEAD 'slashdot.org' >> curl_out.txt
