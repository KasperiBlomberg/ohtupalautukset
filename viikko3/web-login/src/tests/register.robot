*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kas
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration
    Register Page Should Be Open

Register With Valid Username And Too Short Password
    Set Username  kas
    Set Password  sal
    Set Password Confirmation  sal
    Submit Registration
    Register Page Should Be Open

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kas
    Set Password  salasanaa
    Set Password Confirmation  salasanaa
    Submit Registration
    Register Page Should Be Open

Register With Nonmatching Password And Password Confirmation
    Set Username  kas
    Set Password  salasana123
    Set Password Confirmation  salasana1234
    Submit Registration
    Register Page Should Be Open

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration
    Register Page Should Be Open

Login After Successful Registration
    Set Username  kas
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  kas
    Set Password  salasana123
    Submit Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username  kas
    Set Password  salasana123
    Set Password Confirmation  salasana12
    Submit Registration
    Register Page Should Be Open
    Click Link  Login
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}

Submit Registration
    Click Button  Register

Submit Credentials
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open