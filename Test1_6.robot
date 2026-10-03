*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${customer_site_url}    https://acb-qa-customer-ui.creditstrong.com/login
${browser}    chrome
${blUiLoading}                      css:div.block-ui-wrapper.block-ui-main.active
${txtEmail}     //input[@id='username']
${email}    testing_qa_Mvv3Dw@yopmail.com
${txtPassword}  //input[@id='password']
${password}     Test!234

*** Test Cases ***
LoginTest
    open browser    https://www.toolsqa.com/     ${browser}
