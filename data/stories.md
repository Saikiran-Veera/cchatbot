## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
## Careerpath
* CareerOpportunity
  - utter_CareerOpportunity

## details path
* details
    - detail_form
    - form{"name": "detail_form"}
    - form{"name": null}

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## great path-2
* greet_2
  - utter_greet_init
* mood_great
  - utter_happy
  
## great path-3
* greet_2
  - utter_greet_init
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
  
## RPA path
* RPA
  - utter_rpa_def
  
## RPA benefits
* RPA_Benefits
  - utter_rpa_ben
  
## RPA Tools
* RPA_Tools
  - utter_rpa_tools
  
## Company profile
* Company_Profile
  - utter_company_profile

## Company Service
* Company_Services
  - utter_company_services
  
## Client
* Clients
  - utter_client
  
## Contact
* Contact
  - utter_contact
  
## AI
* AI
  - utter_AI
  
## Importance of AI
* Importance_of_AI
  - utter_importance_of_AI
  
## Applications of AI
* Applications_of_AI
  - utter_applications_of_AI
  
## Job Application
* Job_Application
  - utter_job_application
  
## Machine Learning
* ML
  - utter_ML
  
## NLP
* NLP
  - utter_NLP
  
## Robotics
* Robotics
  - utter_robotics
## Automation
* Automation
  - utter_Automation
## MachineLearningBenefits
* MachineLearningBenefits
  - utter_MachineLearningBenefits
## AIvsCognitive
* AIvsCognitive
  - utter_AIvsCognitive
## Blueprism
* Blueprism
  - utter_Blueprism
## Uipath
* Uipath
  - utter_Uipath
## AbusiveContent
* AbusiveContent
  - utter_AbusiveContent
## MachineLearningApplication
* MachineLearningApplication
  - utter_MachineLearningApplication
## Surprise
* Surprise
  - utter_Surprise
## Actions
* Actions
  - utter_Actions
## words
* W-words
  - utter_W-words
## How
* How 
  - utter_How 
## Asking
* Asking
  - utter_Asking
## CompanyUniqueness
* CompanyUniqueness
  - utter_CompanyUniqueness
## BotIdentity
* BotIdentity
  - utter_BotIdentity
## MachinelearningAlgorithm
* MachinelearningAlgorithm
  - utter_MachinelearningAlgorithm
## WhatRUdoing
* WhatRUdoing
  - utter_WhatRUdoing
## CompanyProduct
* CompanyProduct
  - utter_CompanyProduct
## Location
* Location
  - utter_Location
## Agent
* Agent
  - utter_Agent
## VirtechStrength
* VirtechStrength
  - utter_VirtechStrength
## UiPathvsBluePrism
* UiPathvsBluePrism
  - utter_UiPathvsBluePrism
## RPALanguages
* RPALanguages 
  - utter_RPALanguages
## BotUnique
* BotUnique
  - utter_BotUnique
## CompanyExperience
* CompanyExperience
  - utter_CompanyExperience 
## GeneralAboutYou
* GeneralAboutYou
  - utter_GeneralAboutYou
## GeneralEnding
* GeneralEnding
  - utter_GeneralEnding
## GeneralGreetings
* GeneralGreetings
  - utter_GeneralGreetings
## GeneralNegativeFeedback
* GeneralNegativeFeedback
  - utter_GeneralNegativeFeedback
## GeneralSecurityAssurance
* GeneralSecurityAssurance
  - utter_GeneralSecurityAssurance
## Privacy
* Privacy
  - utter_Privacy
## RPAapplications
* RPAapplications
  - utter_RPAapplications
    
## default fallback
* bot_challenge
  - action_default_fallback
  
  
