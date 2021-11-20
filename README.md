<h1 align=center> Best beer</h1>

<p align=center>Are you a beer lover?<br/> Would you like to know what people are saying about a beer that you are eager to buy? <br/>
 Would you like to have your own review list of all beers that you already tasted on your life?<br/> This app is for you! <br/>
On beer rating you can add a review about your favorites beers or research about beers that your are curous to tste it!! <br/>
Check it out! <br/>
Cheers! 

 <br>
 </p>

<img src="media/readme/bestbeer_mockup.jpg">

Live app link [here](https://bestbeer-app.herokuapp.com)

 ## Project Purpose



## User Experience

### User Stories

+ As a user, I would like to be able to …

1. Register on website using my username, email and password;
2. Check all beer reviews added on website;
3. Check beer review details about all added beers.
4. Search for a beer or beer style on navbar.

+ As a logged user, I would like to be able to …

1. Create a beer review of my favorites beers including :
 + Beer Name,
 + Beer Style,
 + My thoughts about the beer,
 + Beer bitterness level,
 + Beer maney and value ratio, and
 + Overall beer rating;
2. Create a new beer or beer style if my beer or beer style are not added on Database;
3. Check my beer review after added;
4. Edit or delete my beer reviews. 

### 1. Project Goal

   + Create a platafom that allows people (users) to evaluate beer and share their thoughts in beer reviews. 


### 2. Scope

 * A simple, straightforward intuitive UX experience;
 * A clear content; 
 * An easy navigation for the user trhough all the features;
 * A site that is visually appealing on most devices.

## Functional Scope 

The following flowchart shows the flow of "Best Beer" graphically.

<p align="center" width="100%">
<img width= "800" src="media/readme/bestbeer_flowchart.jpg">
</p>

### 3. Structure

* A clear and simple layout is in place to ensure users can navigate intuitively and have an easy experience.
* Navbar is fixed on top to facilitate users to navigate through pages easily. Small navigation is the same on all pages to ensure easy navigation.
* Add, Edit and Update Review are straightforward forms to alow the user use the features without isses.


### 4. Skeleton

Wireframes created with Balsamiq. The project was developed from initial wireframes and some modifications were made during the development process to assure better usability. 

Click to see wireframes:

[]() <br>


### 5. Surface

* Colours

The Colour scheme was generated using eye dropper plugin, to get one color from the logo image, and [coolors](https://coolors.co/) to generate the colour pallete.

<p align="center" width="100%">
  <img width="45%" src="media/readme/color_pallete.jpg">
</p>


* Font Selection
 
Two complimentary fonts were chosen with [Google Fonts](https://fonts.google.com/) to be used across the whole of the website.

The chosen fonts were Lobster for headings, and navbar and Open Sans for lists, buttons and paragraphs.
<p align="center" width="100%">
  <img width="33%" src="media/readme/fonts.png">
</p>


## Existing Features

### Navbar 

1. Fixed Navbar allow the user easy access to all pages. 

   1.1 Login and  Register User buttons present on navbar if the user is not logged. 

<p align="center" width="100%">
  <img width="90%" src="media/readme/features/navbar_logedout.jpg">
</p>

   1.2 Logout and Rate your beer buttons are present if the user is logged. 

<p align="center" width="100%">
  <img width="90%" src="media/readme/features/navbar loggedin.jpg">
</p>

   1.3 Beer reviews and search beer by name and style are present to all users (logged or not).

   1.4 User can search their prefered beer by name or style on navbar. 

   i. Beer style has a dropdown menu with all styles registered;

   ii. On Beer name seach, the user can add just few letters to find their prefered beer. 

<p align="center" width="100%">
  <img width="90%" src="media/readme/features/navbar_search.jpg">
</p>

   iii. If there no review for searched beer or style, user is informed about it. 

   iv. If any review is found on Database, user is redirect to a page with all reviews for that style or beer name. (Details about it on Beer style and Beer reviews page)

 
2. Colapsed navbar on smaller devices to wrap in all options and assure better navbar design.

<p align="center" width="100%">
  <img width="33%" src="media/readme/features/collapsed_navbar.jpg"></p>

### Beer review page 

1. On this page user can access beer reviews available on the website ordered by decrescing publication date. 

<p align="center" width="100%">
  <img width="90%" src="media/readme/features/beer_reviews.jpg"></p>

2. Each review card contains beer name, style, image, preview of beer review (full available on beer detail page), bitterness and money-value level, beer rating, author and publication date. 

* The entire card is a link to beer details page.

<p align="center" width="100%">
  <img height="50%" src="media/readme/features/beer_card.jpg"></p>

### Beer detail page 

1. On this page user can access the entire content for beer review. 
<p align="center" width="100%">
  <img width="90%" src="media/readme/features/review_detail.jpg"></p>

   1.1 If the reviews on this page was made for the user accessing it, two buttons became available:
   
<p align="center" width="100%">
  <img height="90%" src="media/readme/features/review_detail_buttons.jpg"></p>

     i. Edit Review (highlited on green)
     ii. Delete Review (highlited on red)

### Update Review Page 

1. On this page a logged user can change a review made by them. All fields are already populated, allowing the user to see which information they would like to change. 
2. The back buttton redirect user to the previous page wiithout changes on review. 

<p align="center" width="100%">
  <img width="90%" src="media/readme/features/update_review.jpg"></p>

+ Constrains : The beer rate stars are not populated on this version. This issue will be correct on a future version of the website. 

### Delete Review Page 

1. If user click to delete a review, they will be redirect to a delete page to confirm the deletion or cancel it. 

<p align="center" width="100%">
  <img width="90%" src=""></p>

### Beer Style and Beer Categories Pages 

1. After searcher a beer by its style on navbar, the user is redirect to this page where they can find all reviews related to the search. 

    1.1 Beer Style search example:
 <p align="center" width="100%">
  <img width="90%"  src="media/readme/features/style_page.jpg">
</p>
    1.2 Beer search example: 
 <p align="center" width="100%">
  <img height="90%" src="media/readme/features/beer_page.jpg">
</p>

2. If no review is available, a message will be in place to inform it and suggest a first review. 

 <p align="center" width="100%">
  <img width="50%" src="media/readme/features/no-reviews-container.jpg">
</p>

## Future Features

I would like to ...

1. Add a infinite carroussel to present beer reviews on reviews list webpage;
2. Create a placeholder image database to be added on post if user doesn't add a beer image on their review;
3. Add a beer style json database on Beer style form;
4. Add a beer json database on Beer Form; 
5. Include icon rating for bitterness and money value field. 
6. Include Brewery Name on beer review.


## Languages Used

Python 3.0

## Frameworks, Libraries & Programs Used

Balsamiq: Balsamiq was used to create the wireframes during the design process.
Favicon generator: Used to create favicon used on the website.
Font Awesome: Font Awesome was used on all pages to add icons for aesthetic and UX purposes.
Grammarly: Used to correct any spell mistakes on readme and app text.
Git: Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
GitHub: GitHub is used to store the project's code after being pushed from Git.
Google Fonts: Google fonts used to add fonts for aesthetic and UX purposes.
Django: 

## Testing and Code validation 

All testing and code validation details are described in a separate file called TESTING.md and can be found [here]().

## Project Bugs and Solutions:

| Bugs              | Solutions |
| ---               | --------- |
| Database inconsistency during unittests|Restart all project adding two different databases (development and production) in order to  make possible to run tests successfully.
| Update Review Unittest failed when tried to change a review | Debug Update review class models and change save function resolved the problem. 
| Navbar dropdown opening behing site divs | Add z-index to navbar resolved the problem. 
| Register feature were not showing the error when it hapenned | Debug Reiste function and remove else statment to redirect user to the same page when it happens. After delete this part of function, everything worked fine. 

## Deployment 

This app is deployed using Heroku.

<details>
<summary>Heroku Deployment steps </summary>
 
 1. Ensure all dependencies are listed on requirements.txt. 
 
 Write on python terminal ` pip3 freeze > requirements.txt` and a list with all requirements will be created to be read by Heroku. 
 
 2. Setting up your Heroku

    2.1 Go to Heroku website (https://www.heroku.com/). 
    2.2 Login to Heroku and go to Create App.
    
    <img src="media/readme/deployment/heroku_login.png">
    
    <img src="media/readme/deployment/heroku_login2.png">
    
    2.3 Click in New and Create a new app
    
    <img src="media/readme/deployment/heroku_newapp.png">
    
    2.4 Choose a name and set your location
    
    <img src="media/readme/deployment/heroku_createnewapp.png">

    2.5. Navigate to Resources tab 

    <img src="media/readme/deployment/heroku_resoursces_tab.png">

    2.6. Click on Resources and Seach for Heroku Postgres and select it on the list.
    
    <img src="media/readme/deployment/heroku-postgres.png">
    
    2.7. Navigate to the deploy tab
    
    <img src="media/readme/deployment/heroku_dashboard_deploy.png">
    
    2.8. Click in Connect to Github and search for 'nandabritto' GitHub account and 'search_your_brand' repository
    
    <img src="media/readme/deployment/heroku_github_deploy.png">
    
    2.9.  Navigate to the settings tab
    
    <img src="media/readme/deployment/heroku_dashboard_settings.png">
    
    2.10.  Click on Config Vars, and add your Cloudinary, Database URL (from herku-postgres) and Secret key.    
    <img src="media/readme/deployment/heroku_vars_settings.png">
    
 

3. Deployment on Heroku

    3.1.  Navigate to the Deploy tab.
    
    <img src="media/readme/deployment/heroku_dashboard_deploy.png">
    
    3.2.  Choose main branch to deploy and enable automatic deployment to build Heroku everytime any changes are pushed on the repository.
    
    <img src="media/readme/deployment/heroku_automatic_deploys.png">
    
    3.3 Click on manual deploy to build the app.  When complete, click on View to redirect to the live site. 
    
    <img src="media/readme/deployment/heroku_view.png">
</details>

<details>
<summary>Forking the GitHub Repository </summary>

* By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

    Log in to GitHub and locate the GitHub Repository
    At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
    You should now have a copy of the original repository in your GitHub account.

* Making a Local Clone

    Log in to GitHub and locate the GitHub Repository
    Under the repository name, click "Clone or download".
    To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
    Open Git Bash
    Change the current working directory to the location where you want the cloned directory to be made.
    Type git clone, and then paste the URL you copied in Step 3.

$ git clone https://github.com/nandabritto/Bestbeer

Press Enter. Your local clone will be created.
</details>


# Credits

### Media

+ All pictures and images used in this project are from [Depositphotos](https://depositphotos.com).

### Work based on other code

[Codemy](https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw) - Used as a base to develop several features as: login, registration and beer review form. <br>
[Pyplane](https://www.youtube.com/channel/UCQtHyVB4O4Nwy1ff5qQnyRw) - Star rating tutorial used to develop beer ratin feature. <br>
[Tutorials Point](https://www.tutorialspoint.com/django-handling-multiple-forms-in-single-view) - Used to add different  django forms on same add review page. <br>

### Media 

+ All media used 

# Acknowledgements

+ Stack Overflow is a valuable resource for solving lots of issues.
+ W3schools and Django documentation for general reference.

I would also like to thank:

+ My husband Guilherme for all the support on stressful moments, help to figure out lots of bugs and for reviewing everything.
+ Code institute tutors, for help with several issues and bugs.


