# BostonHackProject [BostonHacks 2017 Project] 
by Ashley Deshields, Janice He, Ryan Kajardi, Andres Rodriguez, Gabriella Roman, and Christopher Trinh

## What is BostonHackProject?
BostonHackProject uses the Twilio Messaging API to create a Symptom Checker, which allows users to instantly identify possible conditions and receive health information based on their symptoms.

## How does it work?
The actual health stuff is done with some _Google magic_. Messages are sent by POSTing to the Messages resource on the Twilio Platform.

## How do you use it?
Simply send an SMS to +1(667)239-9678, and BostonHackProject will send back to the user three texts: 
- one text that reports the three most likeliest diseases or disorders
- one text that states the suggested course of action the user should take
- and one text that displays the accuracy of the information given.
