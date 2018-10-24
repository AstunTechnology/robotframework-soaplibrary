*** Settings ***
Documentation   Test for basic helper functionality

| Library       | SoapLibrary |
| Library       | Collections |

#| *** Test Cases *** |
#| serialize_object tests |
#|                   | Set Test Variable | ${xml} | <outer><inner>test</inner></outer> |
#|                   | ${obj}= | SoapLibrary.Serialize Object | ${xml} |
#|                   | Log | ${obj} |
#|                   | Dictionary Should Contain Key | ${obj} | outer |
#|                   | Dictionary Should Contain Item | ${obj.outer} | inner | test |
