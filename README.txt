Byld Hackathon App
Food Collaboration | IIIT-D Web App | FoodForces
Team : Archit, Prabhat

GitHub project link : https://github.com/nahimilega/Byld_Hackthon
Old : https://drive.google.com/open?id=13vzZeFy_U2VuEpQwbBfQZTtEzDEYEt_r

Front end : HTML/CSS/JS
Back end : Django

Idea : If you want to order from Dominos, but they have a 1+1 offer on medium pizzas. If you're ordering alone, you can't avail this offer. This app attempts to connect 2 or more people in IIIT-D based on need of food delivery from same restaurant
Objective : To connect 2 or more people in IIIT-D based on need of food delivery from same restaurant
Advantage to Uses: Using this app, they can take advantage of promotional offers, meet minimum delivery requirements etc.

Structure:-
- Page 1: Home screen - Gmail authentication link
- Page 2: List of restaraunts - you can choose restaraunt, how much will you order of, etc
- Page 3: List of people who are already wanting that restaurant, else no


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Front-end HTML resources:-
https://developers.google.com/identity/sign-in/web/
https://stackoverflow.com/questions/6235735/how-to-add-social-login-services-from-google-facebook-yahoo-etc-to-my-website

Changes to make:-
Login with IIIT-D email users only.
For now, we will give option of only 10 restaraunts
A web app, not a mobile app. Paste URL in android development kit thingy


PHASE 1
1. Need to login to app
2. ONLINE/OFFLINE select status
3. Tab - Select restaraunts (1 or more). There will be a checklist of restaraunts
4. If you cllick on Dominos, default waiting time is 30 mins/1 hour. After 1 hr or so the request automatically expires
5. Can leave comments - what type of promotion, est. order value, etc
You hit enter
6. All options of people come with their names within your time slot. Also the fact that you’re ordering from Dominos is updated on other’s devices
7. If nobody wants to order except you, message: “Nobody wants to order at the moment”. Will keep searching though. I think every 1 min it will keep updating
8. Notification will be sent to everybody who wants to order from Dominos if o. Of people interested >= 2
9. Name of the other person will appear
10. You can click and chat with the person

PHASE 2
Abiltity to indicate whether you're interested in ordering with another user or not
