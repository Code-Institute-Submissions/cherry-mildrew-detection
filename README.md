## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created them a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.

## Epics and User Stories 

To help prepare for this project I have broken it into 5 epics and the user stories attached with each epic.

### Information gathering and data collection
* As a data collector I must ensure that the data used is of sufficient quantity and quality. As Garbage in results in garbage out. 

### Data visualisation, cleaning and preparation
* As a data user I must ensures images are resized to ensure a smoother push to GitHub
* As a data user I must create a plot to distinguish contrast between powdery mildrew leaves and normal leaves

### Model training, optimisation and validation
* As a user I want a degree of 97% accuracy

### Dashboard plannning, designing and development
* As a user I want a Project summary page, showing the project dataset summary and clients requirements
* As a user I want a page listing all findings related to the study to visually differentiate a cherry leaf that is helathy and one that isn't
* As a user I want to be able to download a set of cherry leaf images for live predictions
* As a user I want to be able to upload (multiple) images and for each image it will produce a prediction on whether the cherry leaf is healthy or not

### Dashboard deployment and release
* As a user I want the Dasboard to be easy to use and clear to understand

## Hypothesis and how to validate?

### Hypothesis  

* We suspect that leaves that are infected by the powdery mildrew have a lighter colour and patches across the leaf compared to a healthier leaf.

### Validation

An average image study and variability images study will help to investigate. There needs to be a 97% degree of accuracy.  
We will create a binary classification model:

* Cherry leaves **with** Mildrew - 1 powdery mildew

* Cherry leaves **without** Mildrew - 0 healthy


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks.


## ML Business Case
* In the previous bullet, you potentially visualized a ML task to answer a business requirement. You should frame the business case using the method we covered in the course.


## Dashboard Design
---
As set out by the client a dashboard is required to present the models and data.

I shall include a side navigation bar with links to the 5 pages I intend to create.   
1. Summary of project, showing the project dataset summary and the client's requirements.  
2. My findings related to a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew  
3. A page allowing the user to download the images of the cherry leaves from Kaggle and a file uploader to upload users own images and a table with the image name and prediction result.  
4. My project hypothesis and how I validated across the project  
5. Technical page displaying your model performance

### Page 1: Summary of the project

* General Information  
      * Cherry Mildew is caused by Podosphaera clandestina, an obligate biotrophic fungus.
      * Project data set- Contains 4208 images divided equally between healthy and powdery mildew.
      * Link to additional information
      * Business Requirements

### Page 2: Cherry Leaf visualiser  

* It will answer business requirement 1. 
   * Difference between average and variability image
   * Difference between average healthy leaf and a leaf containing powdery mildew
   * Image Montage  


### Page 3: Mildew Detection 

* It will answer business requirement 2.
   * Link to download cherry leaves dataset
   * User interface to upload files/images. It will then display the image uploaded and include a prediction statement as to whether the image is an healthy leaf or contains cherry mildew.
   * Table with image name and prediction result
   Download button to download the table

### Page 4: Hypothesis and Validation

* The project hypothesis is shown in a success box, desribing the conclusion and how it was validated.

### Page 5: ML performance 

* Label frequencies for Train, validation and Test sets.
* History of Model- Accuracy and Loss
* Evaluation result of Model


## Unfixed Bugs
* All bugs were fixed as I went along. I did however create this repository after creating one earlier with the first and second notebooks already created. This was due to an issue when restarting my notebooks and the dat being lost. I wasnt able to resolve it on my old repository therefore I created this one and copied the work I had done previously onto this one, to ensure i met my project deadline. 

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) on how you used these libraries.


## Credits 

* Alot of this came from the First walkthrough project from the @codeinstitute program- Detecting Malaria.

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site
