*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page
Test Teardown  Reset Database
Library    Telnet

*** Variables ***
${VALID_USERNAME}  testuser
${VALID_PASSWORD}  testpassword1

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ${VALID_USERNAME}
    Set Password  ${VALID_PASSWORD}
    Set Password Confirmation  ${VALID_PASSWORD}
    Submit Register
    Register Should Succeed
    

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  ${VALID_PASSWORD}
    Set Password Confirmation  ${VALID_PASSWORD}
    Submit Register
    Register Should Fail With Message  Username must be at least three characters long

Register With Valid Username And Invalid Password
    Set Username  ${VALID_USERNAME}
    Set Password  ajkllkkkkk
    Set Password Confirmation  ajkllkkkkk
    Submit Register
    Register Should Fail With Message  Password must contain numbers and letters

Register With Nonmatching Password And Password Confirmation
    Set Username  ${VALID_USERNAME}
    Set Password  ${VALID_PASSWORD}
    Set Password Confirmation  ${VALID_PASSWORD}1
    Submit Register
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  ${VALID_USERNAME}
    Set Password  ${VALID_PASSWORD}
    Set Password Confirmation  ${VALID_PASSWORD}
    Submit Register
    Welcome Page Should Be Open
    Login User  ${VALID_USERNAME}  ${VALID_PASSWORD}
    Login Should Succeed
    

Login After Failed Registration
    Set Username  ${VALID_USERNAME}
    Set Password  ${VALID_PASSWORD}
    Set Password Confirmation  ${VALID_PASSWORD}1
    Submit Register
    Register Should Fail With Message    Password and password confirmation do not match
    Login User    ${VALID_USERNAME}  ${VALID_PASSWORD}
    Login Should Fail With Message    Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
