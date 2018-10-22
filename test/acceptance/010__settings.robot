*** Settings ***
| Library | SoapLibrary |
| Library | Collections |

*** Variables ***

| *** Test Cases *** |
| Check strict setting gets set |
|                   | &{settings}= | Create Dictionary | strict=False |
|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | settings=&{settings} |
|                   | Should Be Equal | ${client.settings.strict} | False |

| Check raw_response gets set |
|                   | &{settings}= | Create Dictionary | raw_response=True |
|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | settings=&{settings} |
|                   | Should Be Equal | ${client.settings.raw_response} | True |

| Check forbid_dtd gets set |
|                   | &{settings}= | Create Dictionary | forbid_dtd=True |
|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | settings=&{settings} |
|                   | Should Be Equal | ${client.settings.forbid_dtd} | True |

| Check forbid_entities gets set |
|                   | &{settings}= | Create Dictionary | forbid_entities=False |
|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | settings=&{settings} |
|                   | Should Be Equal | ${client.settings.forbid_entities} | False |

| Check forbid_external gets set |
|                   | &{settings}= | Create Dictionary | forbid_external=False |
|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | settings=&{settings} |
|                   | Should Be Equal | ${client.settings.forbid_external} | False |

| Check xml_huge_tree gets set |
|                   | &{settings}= | Create Dictionary | xml_huge_tree=True |
|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | settings=&{settings} |
|                   | Should Be Equal | ${client.settings.xml_huge_tree} | True |

| Check force_https gets set |
|                   | &{settings}= | Create Dictionary | force_https=False |
|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | settings=&{settings} |
|                   | Should Be Equal | ${client.settings.force_https } | False |

| Check extra_http_headers gets set |
|                   | ${headers}= | Create Dictionary | test=True |
|                   | &{settings}= | Create Dictionary | extra_http_headers=${headers} |
|                   | ${client}= | Create Soap Client | ${CALCULATOR WSDL URL} | settings=&{settings} |
|                   | Dictionaries Should Be Equal | ${client.settings.extra_http_headers } | ${headers} |