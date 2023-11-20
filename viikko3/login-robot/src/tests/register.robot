*** Keywords ***
Input New Command And Create User
    [Arguments]  ${username}  ${password}
    Input New Command
    Input Credentials   ${username}  ${password}

*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User  ${USED_USERNAME}  ${USED_PASSWORD}

*** Variables ***
${USED_USERNAME}     testi
${USED_PASSWORD}     testipassword2
${VALID_PASSWORD}    validpassword1


*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User    testiuser  ${VALID_PASSWORD}
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User    ${USED_USERNAME}    ${VALID_PASSWORD}
    Output Should Contain  User with username ${USED_USERNAME} already exists


Register With Too Short Username And Valid Password
    Input New Command And Create User  a  ${VALID_PASSWORD}
    Output Should Contain  Username must be at least three characters long


Register With Enough Long But Invalid Username And Valid Password
    Input New Command And Create User    1234567890123456789012345678901234567890123456789012345678901234    ${VALID_PASSWORD}
    Output Should Contain  Username must consist of letters only

Register With Valid Username And Too Short Password
    Input New Command And Create User  validuser  s
    Output Should Contain  Password must be at least eight characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Create User  user  qwertyuio
    Output Should Contain  Password must contain numbers and letters