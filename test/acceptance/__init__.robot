*** Settings ***
Documentation   The SoapLibrary Robot Testing Framework library
Suite Setup     Suite Setup

*** Variables ***

| *** Keywords *** |
| Suite Setup               | [Documentation] | Suite setup for the SoapLibrary |
|                           | Set Suite Variable | ${CALCULATOR WSDL URL}    | http://localhost:8080/Calculator/soap11/description | children=True |
|                           | Set Suite Variable | ${TEST WSDL URL}          | http://localhost:8080/TestService/soap11/description | children=True |
|                           | Set Suite Variable | ${SECURE TEST WSDL URL}   | http://localhost:8080/secure/TestService/soap11/description | children=True |
|                           | Set Suite Variable | ${SECURE TEST URL}        | http://localhost:8080/secure/TestService/soap11 | children=True |
|                           | Set Suite Variable | ${WSDL DIR}               | http://localhost:8080/wsdls | children=True |
|                           | Set Suite Variable | ${SECURE WSDL DIR}        | http://localhost:8080/secure/wsdls | children=True |
