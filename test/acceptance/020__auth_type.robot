*** Settings ***
| Library | SoapLibrary |

| *** Test Cases *** |
| Check Auth Type gets set |
|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} |
|                   | ${auth_type}= | Get Auth Type | ${client} |
|                   | Should Be Equal | NONE | ${auth_type} | msg=Auth is not set to NONE |

|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | auth_type=BASIC |
|                   | ${auth_type}= | Get Auth Type | ${client} |
|                   | Should Be Equal | BASIC | ${auth_type} | msg=Auth is not set to BASIC |

|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | auth_type=PROXY |
|                   | ${auth_type}= | Get Auth Type | ${client} |
|                   | Should Be Equal | PROXY | ${auth_type} | msg=Auth is not set to PROXY |

|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | auth_type=DIGEST |
|                   | ${auth_type}= | Get Auth Type | ${client} |
|                   | Should Be Equal | DIGEST | ${auth_type} | msg=Auth is not set to DIGEST |

|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | auth_type=XYZ |
|                   | ${auth_type}= | Get Auth Type | ${client} |
|                   | Should Be Equal | NONE | ${auth_type} | msg=Unknown Auth is not set to NONE |