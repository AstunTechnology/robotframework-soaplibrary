*** Settings ***
Documentation   Test for basic functionality
| Library | SoapLibrary |

| *** Test Cases *** |
| Load Remote WSDL |
|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} |
|                   | Should Be Equal | ${client.wsdl.location} | ${CALCULATOR WSDL URL} |

| Load Local WSDL |
|                   | ${url}= | Set Variable | ${CURDIR}\\wsdls\\calculator.wsdl |
|                   | ${client}= | Create Soap Client | ${url} |
|                   | Should Be Equal | ${client.wsdl.location} | ${url} |

| Check timeout gets set |
|                   | ${timeout}= | Convert To Integer | 9 |
|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | timeout=${timeout} |
|                   | Should Be Equal As Integers | ${client.transport.load_timeout} | ${timeout} |

| *** Test Cases *** |
| Calling webservice without params |
|                   | Create Soap Client | ${TEST WSDL URL} |
|                   | ${answer}= | Call Soap Method | theAnswer |
|                   | Should Be Equal As Integers | ${answer} | 42 |

| *** Test Cases *** |
| Calling webservice with params |
|                   | Create Soap Client | ${CALCULATOR WSDL URL} |
|                   | ${params}= | Create List | 7 | 3 |
|                   | ${answer}= | Call Soap Method | add | ${params} |
|                   | Should Be Equal As Integers | ${answer} | 10 |