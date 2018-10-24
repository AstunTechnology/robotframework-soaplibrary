*** Settings ***
Documentation   Basic authentication tests for the SoapLibrary
| Library | SoapLibrary |

| *** Keywords *** |
| Call Authenticated Service Without Credentials |
|                   | Create Soap Client | ${SECURE TEST WSDL URL} |
| Call Authenticated Service With Credentials |
|                   | Create Soap Client | ${SECURE TEST WSDL URL} | username=bob | password=bob | auth_type=STANDARD |


| *** Test Cases *** |
| Http Authentication tests Without Credentials | [Documentation] | Http Authentication |
|                   | Run Keyword And Expect Error | HTTPError: 401 Client Error: Authentication Required for url: http://localhost:8080/secure/TestService/soap11/description | Call Authenticated Service Without Credentials |
| Basic Http Authentication tests With Credentials | [Documentation] | Basic Http Authentication |
|                   | Create Soap Client | ${SECURE TEST WSDL URL} | username=bob | password=bob | auth_type=BASIC |

# TODO: Create local webservices to test against
#| Proxy Http Authentication tests With Credentials | [Documentation] | Basic Http Authentication |
#|                   | Create Soap Client | ${SECURE TEST WSDL URL} | username=bob | password=bob | auth_type=PROXY |
#| Digest Http Authentication tests With Credentials | [Documentation] | Basic Http Authentication |
#|                   | Create Soap Client | ${SECURE TEST WSDL URL} | username=bob | password=bob | auth_type=DIGEST |

| *** Test Cases *** |
| Authenticated method call with credentials |
|                   | ${client}= | Create Soap Client | ${SECURE TEST WSDL URL} | username=bob | password=bob | auth_type=BASIC |
|                   | ${answer}= | Call Soap Method | ${client} | theAnswer |
|                   | Should Be Equal As Integers | ${answer} | 42 |