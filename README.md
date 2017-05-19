# Q-less, an IoT solution for food court and restaurant queue management 
## This was done for the **24 hour** Bosch BoT hackathon, Singapore, with the theme of smart buildings and IoT
## Our team clinched **1st place** for the event and here is our solution 

Q-Less consists of the following features:
1. Real time tracking of seat occupancy data which is beamed to a central Wifi hub using RF transmission 
2. Cloud server hosted in [Heroku](https://www.heroku.com/) with seat dispatching algorithm 
3. Database of queue orders, existing users and food court seat layout 
4. App (currently on Android) which allows the user to place orders and receive notifications of estimated wait time
5. Web dashboard for food court store owners to service incoming order request

In this repository, you will find:
1. The entire server side code, developed in Django
2. Web interface in HTML / CSS / JQuery which is served concurrently with the back end

You may find the repository for our app in the link below:
[Q-less app]()