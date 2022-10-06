## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created them a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from Farmy & Foods crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and one that contains powdery mildew.
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

* We suspect that leaves that are infected by the powdery mildrew have a lighter colour and patches across the leaf.
* Powdery mildew affected leaves edges to be distorted and folded compared to a healthier leaf.

### Validation

An average image study and variability images study will help to investigate. There needs to be a 97% degree of accuracy.  
We will create a binary classification model:

* Cherry leaves **without** Mildrew - 0 healthy

* Cherry leaves **with** Mildrew - 1 powdery mildew



## Rationale to map the business requirements to the Data Visualizations and ML tasks

### * Business Requirement 1: Data Visualisation
* I will display the "mean" and "standard deviation" for images containing healthy leaves and leaves containing powdery mildew.
* I will show the difference between an average healthy leaf compared to a leaf containing powdery mildew
* There will be an image montage showing all healthy leaf or a leaf containing powdery mildew 

### * Business Requirement 2: Predicting and classifying images
* Predict if a given image contains a leaf that is affected by the powdery mildew or is healthy
* Build a ML model to predict future images with cherry leaves contained and classify them with a Neural Network that maps relationships. 


## ML Business Case
* From a given dataset of images I must create a ML model to predict if a cherry leaf is healthy or has a powdery mildew on it. It will be a fully supervised model.  
* The purpose of this is to speed up the time it takes to detect whether or not a leaf is healthy. Currently it takes around 30 minutes on each tree to visually verify and then a further minute to apply a compund to kill the fungus.
* A success metric has been set at 97% Accuracy on the test set or above as the cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.
* The client will benefit by not supplying the market with a product of poor quality by the creation of this model. 
* The training data can be found from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). This contains 4208 Images. All images are uniformed at (256,256,256,3). To ensure the performance is not affected we will reduce the image shape to something around 30x30.


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
* Another bug appears when uploading leaves that have powdery mildew on them. It would cause an issue with the bar plot and duplicate the powdery mildew column. This wouldn't happen with a healthy leaf and I am really unsure as to why this is happening. 

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
* numpy  
     * Used to handle multi-dimentional arrays to operate on them including mathematical functions.
* pandas  
     * Used to structure the data in tables. Also used for data cleaning
* matplotlib 
     * Used to visualise the data (along with Seaborn)
* Seaborn 
     * Used to visulaise the scatterplots/ bar plots and set themes and colour style
* Joblib
     * Used to pipeline the python objects containing models ready to be used to visualise.
* Shutil
     * Supports file copying and removal
* random
     * Used to generate random numbers
* Tensorflow
     * Used to create machine learning models; focusing on deep neural networks.
* Scikit-learn
     * Used to provide the tools needed for machine learning modeling.
* Streamlit
     * Used to create the dashboard. It connects the back-end information to the front end.
* Plotly
     * Used to create visulaisations within Jupyter notebooks to present the data. Can be found on Mildew detector page on the dashboard

## Credits 

* Alot of this came from the First walkthrough project from the @codeinstitute program- Detecting Malaria.

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site
