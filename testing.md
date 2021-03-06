# Testing

> [To return to the previous document please click here](https://github.com/mayasaffron/self-isolation-watch/blob/master/README.md) 

## Table of contents

- [**Accessibility**](#Accessibility)
    - [Symptoms page](#Symptoms)
    - [Login page](#Login)
    - [Register page](#Register)
    - [My symptoms page](#My-symptoms)
- [**Responsiveness**](#Responsiveness)
- [**User stories**](#User-stories-testing)
- [**Usability**](#Usability-testing)
    - [Symptoms page](#Symptoms-page-usability)
    - [Register page](#Register-page-usability)
    - [Login page](#Login-page-usability)
    - [Add symptom](#Add-symptom-usability)
    - [Edit symptom](#Edit-symptom-usability)
    - [Delete symptom](#Delete-symptom-usability)
- [**Validators and Linters**](#Validators-and-Linters)
    - [WW3 HTML validation](#WW3-HTML-validation)
    - [WW3 CSS validation](#WW3-CSS-validation)
    - [PEP8 validation](#PEP8-validation)
    - [Javascript validation](#Javascript-validation)

## Accessibility
* I used [wave](https://wave.webaim.org/) to achieve better accessibility on my site. 

### Symptoms

![First attempt with wave](/testing/accesibility/wave-test-1-(homepage).png)  
* I had a serious contrast issue, so I immediately resolved this on every page. 

![After resolving contrast issue](/testing/screenshots/wave-test-2-(homepage).png). 
* I started to understand the importance of the contrast issues and labelling objects that I wouldn't assume necessary to label. For example, lists and navbars. 
![After adding more aria-labels where necessary](/testing/screenshots/wave-test-3-(homepage).png)
![Final wave test on homepage](/testing/screenshots/wave-test-final.png)

* Due to my sites restrictions on what content can be seen by other users, I was not able to run the 'my symptoms' page through the wave test. To ensure I was able to maintain the same diligence to the accessibility of the site, across all pages, I added wave's google chrome extension to my browser. 
[google chrome extension](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh/related) 


 ### Login

![Login page](/testing/screenshots/wave-login.png)
* The empty link being sighted on the page is the scroll to top function which appears as dormant on the login and register pages because, the pages have so little contnet that the function is not activated. To add clarity to the scroll to top button/ link, i added a aria- label, explaiinng that it was a scroll to top link. 

 ### Register
![register page](/testing/screenshots/wave-register.png)
* On the register page, I also had a link button to 'log in' (if users already had an account). The wave test pointed out that this was in fact bad usability and could actually be confusing for a user, therefore contributing to bad user experience. 

* I removed the login link. 

* In aiming to be an 'easy to use site', I had added surplus buttons for user ease. However, I had overpopulated the site with excessive buttons, which had the opposite effect! 

 ### My symptoms

![My symptoms](/testing/screenshots/wave-my_symptoms.png)
* The missing 'form label' is for the first question on the add symptom form 
``` <div class="input-field status-options">
                    <select id="isolation_status" name="isolation_status" class="validate" aria-label="isolation-status dropdown" required> 
                    <label for="isolation_status"> </label>
                        <option value="" disabled selected>What is your Self-isolation status?</option>
                        {% for stat in status %}
                        <option value="{{ stat.isolation_status }}">
                            {{ stat.isolation_status }}
                        </option>
                        {% endfor %}
                       
                    </select>                    
                    </div> 
```

* Due to the nature of this input field, it was less aesthetically pleasing, responsive to have a label AND a disabled selected option. I opted for the disabled selected option instead of a label because the disabled selected option could function as a label. I also added an aria-label for users who rely on labels. 

## Responsiveness

* Materialize is made for responsive and upwards, therefore I kept the use of col sizes minimal and made sure everything would fit a small screen first and mainly used the col size of s12. 

### Footer
* Just at desktop/ iPad pro screen size, my main issue was the footer on all pages sitting at the bottom of the page, this happens when an object is too big for its container and overspills outside of the main HTML. 
![footer on homepage](/testing/responsiveness/ipad-pro-homepage(2).png)
![login on homepage](/testing/responsiveness/login.png)
![registeration on homepage](/testing/responsiveness/ipad-pro-register.png)

* My first action was to change the position of the footer to 'relative' and 'absolute' in turn. neither of these options made all three pages' footers responsive.

* I then added an id to the footer and trialled different positions through the id. This was again no help. 

#### Solution 

- I referred back to materialize, which was where I had used the footer template and added some positioning to the body and main. This made the footer responsive on all pages. 
```
body{
    background-color: #FFE1A8;
    font-family: 'Roboto', 'sans-serif';
    color: #472D30;
    text-align: center;
    font-size: 20px;
    padding: 1rem 0rem 0rem 0rem;
    display: flex;
    min-height: 100vh;
    flex-direction: column;

}

  main {
    flex: 1 0 auto;
  }
```

- Something I learnt with this error, is that if you are going to use a library and templates from the library in your developing process, you must be aware that the entire framework, relies on (sometimes hidden) positioning/ sizing, these will affect aspects of your entire project. although it may seem like the easiest option in early development, to use libraries, it may not always be the easiest option in the long run. 

### footer layout on mobile 

- Similarly, on the iPhone 5 screen size, I was troubled by the layout of the footer. 

![footer layout](/testing/responsiveness/iphone-5-footer-layout.png)

I made some changes and simplified the content, but I was still unhappy that at the small device size it was still 3 columns. I thought I had understood the materialize grid system to mean that s12 m4 l4 meant that, the columns would take up all 12 spaces (the entire screen width) when being viewed at this size. 4/12 for each column when viewed on medium and large screens. 

- To try to solve this I adjusted the column sizes and kept checking them again. 

#### Solution 
- unresolved. 

### add symptom form 

- On the add symptom form, when a user clicks on the input fields, the labels became slightly obstructed. 
![add symptom form](/testing/responsiveness/ipad-pro-add-symptom-form(1).png)

* Using inspect in dev tools, I adjusted the position of the label in the input field.

#### Solution 

- I added a bit of extra room to the top and left of the input field label so that when the field is clicked on and being added to, the labels are still not obstructed 
-*I did the same for the text area's of the input fields and eventually managed to make the form more aesthetically pleasing and readable 
```
.input-field>label {
color: black;
left:2rem;
top:.50rem;
}
```
![add symptom form](/testing/responsiveness/ipad-pro-add-symptom-form(2).png)
![add symptom form](/testing/responsiveness/ipad-pro-add-symptom-form(3).png)
![add symptom form- iPhone 5](/testing/responsiveness/iphone-5-add-symptom-form.png)

### Overspill from content causing responsiveness issue
- At desktop screen size there was a vertical overspill of content, causing the page to jiggle from side to side. I also saw a horizontal overspill too.

![Overspill](/testing/responsiveness/footer-overspill(1).png)
![horizontal overspill](/testing/responsiveness/horizontal-overspill(1).png)
#### solution 
- Using the [unicorn revealer tool](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) 
I scrolled to see the issue and where the overspills lie. 
![Overspill](/testing/responsiveness/footer-overspill(2).png)
![horizontal overspill](/testing/responsiveness/horizontal-overspill(2).png)

- Eventually, I saw the overspill was in the footer.
![Overspill](/testing/responsiveness/footer-overspill(3).png)
- Also in the `body` element.

- To solve this I added a `div` with the class of `container`
![Solved](/testing/responsiveness/overspill-solved(1).png)
![Solved](/testing/responsiveness/overspill-solved(2).png)

- To solve the overspill in the body, I removed some extra padding I had added. 
![Solved](/testing/responsiveness/horizontal-overspill-solved.png)

## User stories testing

- *'As a recent self isolator, I want to keep track of what symptoms I have and how long I have had them so that I have more information to give to the doctor.'*

#### How this has been achieved

* When a user has added a symptom by filling out the add symptom form, they have said when they started to feel the symptoms and this is shown on on their list of symptoms on their profile page (my symptoms)
![tracking symtpoms](/testing/user-stories/track-symptoms.png)


- *'As a key worker, I want to browse through patients' symptoms, so that I can speed up diagnosis. '*

#### How this has been achieved
- A user can present a screenshot of their symptoms, which have all been saved and easily found on their profile page.

- *'As a recent self isolator, I want to update the symptoms I have had so that I can find out how far from recovery I am.'*

#### How this has been achieved
![Updating symtpoms](/testing/user-stories/update-symptom(1).png)
![Updating symtpoms](/testing/user-stories/update-symptom(2).png)
![Updating symtpoms](/testing/user-stories/update-symptom(3).png)
![Updating symtpoms](/testing/user-stories/update-symptom(4).png)
![Updating symtpoms](/testing/user-stories/updated-symptom.png)

- A user can update their symptoms and see it listed with their other symptoms, once saved.

- *'As a recent self isolator, I want to read through other peoples symptoms and compare, so that I can find out if my symptoms are typical.'*

#### How this has been achieved
![Readable symptoms](/testing/user-stories/readable-symptoms(1).png)
![Readable symptoms](/testing/user-stories/readable-symptoms(2).png)
- Users can see the list of symptoms on the homepage and will be able to see if the entries have been made by themselves or others from the 'created by:' and the absence of the edit and delete buttons. 
![Readable symptoms](/testing/user-stories/readable-symptoms(3).png)

- A user can even search through the list and see if other users have entered symptoms with keywords that the user was planning on using in their symptom name/ description!

![Readable symptoms](/testing/user-stories/readable-symptoms(4).png)
- In the testing of this user story, I was prompted to create an if statement to provide the user with feedback if their searched keyword was not present in any of the symptom entries. 

![Readable symptoms](/testing/user-stories/readable-symptoms(5).png)
![Readable symptoms](/testing/user-stories/readable-symptoms(6).png)

- If the user has searched a keyword that is present somewhere in the symptoms, that will also be displayed. 

- I was very happy with the functionality of the search box. 

## Usability testing

### Symptoms page usability 

![user lands on homepage](/testing/usability/home(1).png)
* Name of the page is highlighted in navbar, user knows they are on the symptoms page. 

* User reads the text and clicks 'get started now'.
![user clicks on 'get started now'](/testing/usability/home(2).png)

* Button highlights- aesthetically pleasing, the user is given feedback that they have hovered/ clicked on the button.
![User is taken to register page](/testing/usability/home(3).png)

* User is taken to register page after clicking, again register is highlighted and page is simple and functional. 

* *If user is already logged in and clicks this same button, they are redirected to the add add symptom form* 

![search bar on homepage](/testing/usability/home(4).png)
* If the user comes back to the homepage, they are met with the search bar. If they perform a none format fitting search, they are told what is wrong and how to solve the issue. 
![none formatting search item](/testing/usability/home(5).png)

* If, search item does not match any of the listed symptoms, the user sees a message explaining that with a link. 

- This message could be stronger and more obviously a feedback message. 

!['search item doesnt exist' message](/testing/usability/home(13).png)
Here I have added a div with class 'alert' around the if statement which actions the feedback text, letting the user know that their search item was unmatched and what they should do next. I checked its accessibility too and found no issues with style. 

- *If user clicks on the link to add the symptom, they are redirected to the login page.*

- *If user is already logged in and clicks this same button, they are redirected to the add add symptom form* 

* User resets and scrolls down to find the list of added symptoms.
![user resets search item](/testing/usability/home(6).png) 

* User is informed with text that the list is clickable after clicking, they see the description. 
![user clicks symptom on list- description appears](/testing/usability/home(7).png) 
![user clicks symptom on list- description disappears](/testing/usability/home(8).png)

* Scrolling down to bottom of page, copy url functionality is hovered, clicked and gives feedback. 
![copy url functionality is hovered](/testing/usability/home(9).png)
![copy url functionality is clicked](/testing/usability/home(10).png)
![copy url functionality gives feedback](/testing/usability/home(11).png)


* Link in footer works, however when testing I noticed I had forgotten to add `"_blank"` attribute. I have since added and the link now opens to a new tab. 
![user lands on homepage](/testing/usability/home(12).png)


### Register page usability
- After clicking one of the homepage links or after clicking register in the nav bar, user arrives at the registration page 
![register](/testing/usability/register(1).png)
![register](/testing/usability/register(2).png)

* The registration page nav bar link is highlighted, the registration form provides feedback of the allowances of choosing a username and or password. 

* Originally, I had added a pattern that the user must adhere when choosing a username and password. I did this because I wanted to improve my defensive programing, however, after testing, I realised that these features actually inhibited a good UX. I since removed them and now the only requirements for a username/ password are the minimum lengths. 

* After successfully registering, the user is taken directly to the 'my symptoms' page where they are informed that they have no symptoms currently and are encouraged to add one.
![register](/testing/usability/register(3).png)

* Initially I had a link to the add symptom form, however again when testing, I realised that it was actually confusing to have an additional link for a process which is a mere scroll away! 
![register](/testing/usability/register(4).png)

* If the user tries to login with a username that is already in use they are taken to the login page 
![register](/testing/usability/register(5).png)

### Login page usability 
- When logging in with an error, the user is taken to an error page, which does not say the specific reason they have not successfully logged in, but gives all possible reasons. I felt this was better defensive programming than a mere flash message. 
![login](/testing/usability/login(1).png)
![login](/testing/usability/login(2).png)

- The link in error page, brings user back to login. 
![login](/testing/usability/login(3).png)
![login](/testing/usability/login(4).png)

- If login is successful; 
![login](/testing/usability/login(5).png)

### Add symptom usability
- When the user has logged in / registered and now wants to add a symptom,
![add symptom](/testing/usability/add_symptom(1).png)

- The user fills in the form and receives feedback once complete. 
![add symptom](/testing/usability/add_symptom(2).png)

### Edit symptom usability
- When the user wants to edit;

![edit symptom](/testing/usability/edit_symptom(1).png)

- The text at the top of the page explains to the user why it is important to continually update their symptoms.

![edit symptom](/testing/usability/edit_symptom(2).png)

- The users' original form is loaded.

![edit symptom](/testing/usability/edit_symptom(3).png)

- When changes are made to the form, the user clicks the save button. 

![edit symptom](/testing/usability/edit_symptom(4).png)

- At this point, the user is given feedback that the symptom is updated and where it can be found. 

### Delete symptom usability
- When deleting a symptom; 
![deleting symptom](/testing/usability/delete-symptom(1).png)
![deleting symptom](/testing/usability/delete-symptom(2).png)

- A modal will appear asking the user if they are sure they want to delete. 
- If yes, they will be given a feedback message, prompting them to add another. I didn't think a link to 'add symptom' was necessary, again,  it may have contributed to bad UX.
![deleting symptom](/testing/usability/delete-symptom(3).png)

- If no, the box simply closes. 
![deleting symptom](/testing/usability/delete-symptom(4).png)

## Validators and Linters

### WW3 HTML validation 
As expected, each of my pages flagged errors due to my use of jinja code, I also had some warnings about the misuse of the `aria-label` attribute, however since I had added these after taking the accessibility of my site into account, I thought that the wave tool was likely to be a better judge of the use of this particular attribute and felt comfortable with my choice. 

Other than the jinja code-related errors, I had no other HTML validation errors. 

### WW3 CSS validation 
- My CSS had no errors.
![CSS Validator](/testing/usability/CSS-Validator.png)

### PEP8 validation 
- My python code had no errors.
![PEP8](/testing/usability/PEP8.png)


### Javascript validation 
- My javascript code had no errors but did have 3 warnings. The warnings were about the use of keywords such as `let` and `const`, to avoid any issues with this, in the future I would ensure that all of my JS functions had an `error` response, if anything I was using, was not supported in the users' browser. Similar to the error function I used for the creation of my copy to clipboard function. 
```
clipboard.on('error', function(e) {
alert("Oops, it looks like this function isn't supported on your browser! Don't worry, Just copy this: https://self-isolation-watch.herokuapp.com/"); 
```

![JS-Hint](/testing/usability/JS-Hint.png)


> [To return to the previous document please click here](https://github.com/mayasaffron/self-isolation-watch/blob/master/README.md) 