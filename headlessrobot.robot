*** Settings ***
Library    SeleniumLibrary
Library    ImapLibrary

*** Test Cases ***
Chrome
    Open Browser                     https://login.live.com/login.srf                                           headlesschrome
    Sleep                            30
    Wait Until Page Contains         Sign in
    Maximize Browser Window
    Capture Page Screenshot
    Input Text                       xpath://input[@class='form-control ltr_override' and @name='loginfmt']     test@qxf2.com
    Capture Page Screenshot
    Click Button                     xpath://input[@class='btn btn-block btn-primary' and @id='idSIButton9']    
    Capture Page Screenshot
    Wait Until Page Contains         Sign in
    Wait Until Element Is Visible    xpath://input[@name='passwd' and @type='password']
    Input Text                       xpath://input[@name='passwd' and @type='password']                         SkypeQxf2!Kxf2
    Capture Page Screenshot
    Sleep                            30
    Wait Until Element Is Visible    xpath://input[@class='btn btn-block btn-primary' and @type='submit']
    Click Button                     xpath://input[@class='btn btn-block btn-primary' and @type='submit']
    Sleep                            30
    Capture Page Screenshot
    Handle Alert                     DISMISS                                                                    60
    Capture Page Screenshot
    Wait until Page Contains         Microsoft
    Sleep                            30
    Capture Page Screenshot
    Open Browser                     https://www.skype.com/en/                                                  headlesschrome
    Maximize Browser Window
    Sleep                            30
    Capture Page Screenshot
    Wait until Page Contains         Skype 
    Sleep                            30                                                                         
    Capture Page Screenshot






