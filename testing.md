# Testing

## Accessibilty
My mentor alerted me to the importance of the accesibility of my site. 
i used [wave](https://wave.webaim.org/)
this was a screenshot of my first use of the tool. 
![1st attempt with wave](/testing/screenshots/wave-test-1-(homepage).png) as you can see, i had a serious contrast issue, so i immediatley resolved this on every page. 
my ![second attempt](/testing/screenshots/wave-test-2-(homepage).png) was better and i started to understamd the importance of the contrast issues and labelling objects that i wouldnt assume necessary to label. for example, lists and nav bars. ![third attempt](/testing/screenshots/wave-test-3-(homepage).png)
Due to my sites restrictions on what content can be seen by other users, i was not able to run the the my symptoms page through the wave test, however i simply applied the previous logic to this page and made necessary adjustments. 
![Final wave text](/testing/screenshots/wave-test-final.png)

### Responsiveness
luckily, materialize is made for responsive and upwards, therefore i kept the use of col sizes minimal and made sure everything would fit a small screen first and mainly used the col size of s12. 

### footer
Just at desktop/ ipad pro screen size,
my main issue was the footer on all pages sitting at the bottom of the page, this happens due to the varying of content on each page. 
![footer on homepage](/testing/responsiveness/ipad-pro-homepage(2).png)
![login on homepage](/testing/responsiveness/login.png)
![registeration on homepage](/testing/responsiveness/ipad-pro-register.png)

* my first action was to change the position of the footer to 'relative' and 'absolute' in turn. neither of these options made all three pages' footers responsive.
* I then added an id to the footer and trialed different positions through the id. This was again no help. 

#### solution 
- I referred back to materialize, which was where i had used the footer template and added some positioning to the body and main. This made the footer responsive on all pages. 
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
- Something i learnt with this error, is that if you are going to use a library and tmeplates from the library in ypour developing process, you must be aware that the entire framework, relies on (sometimes hidden) positioning/ sizing, these will effect aspects of your entire project. although it may seem like the easiest option in early developement, to use libraries, it may not always be the easiest option in the long run. 

### footer layout on mobile 
- similarly, on the iphone 5 screen size, i was troubled by the layout of the footer. 

![footer layout](/testing/responsiveness/iphone-5-footer-layout.png)

I made some changes and simplified the content, but i was still unhapy that at the small device size it was still 3 columns. i thought i had understood the materilaze grid system to mean that s12 m4 l4 meant that, the columns would take up all 12 spaces (the entire screen width) when being viewed at this size. 4/12 for each column when viewed on mediu,m and large screens. 

- to try to solve this i adjusted the column sizes and kept checking them again. 
- i did some research and added some media queries in. 

### solution 
- unresolved. 

### add symptom form 
on the add symptom form, when a user clicks on the input fields, the labels became slightly obstructed. 

![add symptom form](/testing/responsiveness/ipad-pro-add-symptom-form(1).png)


* Using inspect in dev tools, i adjusted the position of the label in the input field.

#### solutiom 
- i added a bit of extra room to the top and left of the input field label, so that when the field is clicked on and being added to, the labels are still not obstructed 
```
.input-field>label {
color: black;
left:2rem;
top:.50rem;
}
```
![add symptom form](/testing/responsiveness/ipad-pro-add-symptom-form(2).png)
![add symptom form](/testing/responsiveness/ipad-pro-add-symptom-form(3).png)


### add symptom form 
on the add symptom form, when a user clicks on the input fields, the labels became slightly obstructed. 

![add symptom form](/testing/responsiveness/ipad-pro-add-symptom-form(1).png)


* Using inspect in dev tools, i adjusted the position of the label in the input field.

#### solutiom 
- i added a bit of extra room to the top and left of the input field label, so that when the field is clicked on and being added to, the labels are still not obstructed 
```
.input-field>label {
color: black;
left:2rem;
top:.50rem;
}
```
![add symptom form](/testing/responsiveness/ipad-pro-add-symptom-form(2).png)
![add symptom form](/testing/responsiveness/ipad-pro-add-symptom-form(3).png)


i did the same for the text area's of the input fields and eventually maanged to make the form more aesthetically pleasing and readable 
![add symptom form- iphone 5](/testing/responsiveness/iphone-5-add-symptom-form.png)

## User stories testing

- 'As a recent self isolater, I want to keep track of what symptoms I have and how long I have had them, so that I have more information to give to the doctor.'

#### How this has been achieved
When a user has added a symptom by filling out the add symptom form, they have said when they started to feel the symptoms and this is shown on on their list of symptoms on their profile page (my symptoms)
![tracking symtpoms](/testing/user-stories/track-symptoms.png)


- 'As a key worker, I want to browse through patients' symptoms, so that I can speed up diagnosis. '

#### How this has been achieved
A user can present a screenshot of their symptoms, which have all been saved and easily found on their profile page. 

- 'As a recent self isolater, I want to update the symptoms I have had, so that I can find out how far from recovery I am.'

#### How this has been achieved
![Updating symtpoms](/testing/user-stories/update-symptom(1).png)
![Updating symtpoms](/testing/user-stories/update-symptom(2).png)
![Updating symtpoms](/testing/user-stories/update-symptom(3).png)
![Updating symtpoms](/testing/user-stories/update-symptom(4).png)
![Updating symtpoms](/testing/user-stories/updated-symptom.png)

A user can update their symtpoms and see it listed with their other symptoms, once saved.

- 'As a recent self isolater, I want to read through other peoples symptoms and compare, so that I can find out if my symptoms are typical.'

#### How this has been achieved
![Readable symptoms](/testing/user-stories/readable-symptoms(1).png)
![Readable symptoms](/testing/user-stories/readable-symptoms(2).png)
- users can see the list of symtpoms on the homepage and will be able to see if the entries have been made by themselves or others from the 'created by:' and the absence of the edit and delete buttons. 
![Readable symptoms](/testing/user-stories/readable-symptoms(3).png)
- A user can even search through the list and see if other users have entered symptoms with keywords that the user was planning on using in their symptom name/ description!

![Readable symptoms](/testing/user-stories/readable-symptoms(4).png)
- In the testing of this user story, i was prompted to create an if statement to provide the user with feedback if their searched keyword was not present in any of the symptom entries. 

![Readable symptoms](/testing/user-stories/readable-symptoms(5).png)
![Readable symptoms](/testing/user-stories/readable-symptoms(6).png)
- If the user has searched a keyword that is present somewhere in the symptoms, that will also be displayed. 
- I was very happy with the functionality of the search box. 

## WW3 HTML validation 
## WW3 CSS validation 
## PEP8 validation 
## Javascript validation 
## compatability