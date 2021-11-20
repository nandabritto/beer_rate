# Testing

During code development of each function tests were in place to be sure that it was running as expected. The following sections describe all tests are done and error handling in place.

## Code Validation Testing

#### Python (PEP8) Validation


#### CSS Code Validation

#### JavaScript Code Validation


## Exploratory Testing
=============================================================================================

### Initial User Testing (Alpha)

A session was held with an end user. The feedback obtained is listed below:

1. **Navbar**

   1.1 The page which we are is slightly highlighted, I would like a more visual appealing color to better differentiate which page I am.

   1.2 "Beer Styles" dropdown menu is mixed with operational menu options. I would like to have on Left: "Best Beer" (as home), "Beer Reviews", "Beer Styles" and "Search your beer". On Right, "Register", "Login", "Logout".

2. **Home Page**

   1.1 I would like to have option to login directly form there, without needing to go to login page, and then log in.

3. **Register User Page**

   3.1 When entered a password that do not match, a very quick message appeared on top, but it was not possible to read in time. I would like this message sticks on bottom of "Register" container so users can read and understand error.

   3.2 When logged successful, I have been redirected to home page, page which I just came from. I would like to be redirected to reviews page, where I can actually use information on website.

4. **Beer Reviews page**

   4.1 I would like to have option to search, filter and choose different sort option (like Money-Value) directly on page, without needing to go through top bar

   4.2 - The "Beer reviews" title looks blended with background image, I would like to use larger box with different text size or even some logo image. This "Beer reviews" there may also not be required if top bar use more distinct color when page is the one selected.

   4.3 Buttons "First Next Last" looks too close to card box and background color blend then. I would like a better visual to differentiate they are buttons and not random text on foot of page.

   4.4 The page should inform default sort order, like displaying "Latest beer reviews" instead of just "Beer reviews" and sort that page by review date.

5. **Review Detail Page**

   5.1 On bottom of review container, where we see "Written by:", I would rather to have it as "Review by: <name of author>"  and on same row "Created at: <date>"


+ After evaluation of user comments, some featurs were modified to increase user experince. 


# Code Validation

## Automated tests
=============================================================================================
### **Members App** 

All functions on members app were tested using unittests. 

  * Views 
<p><img src="media/readme/unittests_ss/members_unitest_testviews.jpg"></p>

  * Forms 
<p><img src="media/readme/unittests_ss/members_unitest_testforms.jpg"></p>

  * Members Unittests Overall
<p><img src="media/readme/unittests_ss/members_unitest_membersoverall.jpg"></p>

=============================================================================================
### **Post App** 

  * Views 
<p><img src="media/readme/unittests_ss/post_unitest_testviews.jpg"></p>

  * Forms 
<p><img src="media/readme/unittests_ss/post_unitest_testforms.jpg"></p>

 * Urls 
<p><img src="media/readme/unittests_ss/post_unitest_testurls.jpg"></p>

 * Models
<p><img src="media/readme/unittests_ss/post_unitest_testmodels.jpg"></p>

  * Post Unittests Overall
<p><img src="media/readme/unittests_ss/post_unitest_testoverall.jpg"></p>

### **Overal Test on plataform** 

Ate the end of development og this project (fase 1 - before submission day), coverage tool were used to assert that all functions were covered by automated tests. 

<p><img src="media/readme/unittests_ss/coverage_beer_app.jpg"></p>

+ **post/views.py**

    The lines uncovered by unit tests on post/views.py refers to update view function. This was described on bugs section in readme.md. As this automated test were not done, manual tests were conducted to be sure that feature were working as expected and without errors. 

+ **django_beerapp/settings.py**

    This uncovered lines refers to databased used (f production or development) and it was tested manually as well. 

## Manual Testing
============================================================================================
### Desktop

  Mozilla Firefox, Google Chrome, Microsoft Edge: everything is working good. Page loads, all features are working and no problems were found in adding, updating, deleting or siply seeing the content. 

### Mobile

  Tested with Xiaomi Mi6 and Xiaomi Mi8 and plataform works well and without any issues. 

