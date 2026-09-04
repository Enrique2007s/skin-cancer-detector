
## Dataset Content

The dataset contains a total of 3297 images of both malignant and benign labels. All images have a size of 224x224px.

## Business Requirements
* The client is interested in identifying non malignant and malignant skin cancer in patients through a machine learning application, used as a second opinion.
  
* The client is interested in knowing if benign and malignant skin lesions can be differentiated visually

* The client is interested in significantly shortening diagnosis time for skin cancer.

* The client is interested in reducing deaths caused by skin cancer by making skin cancer screening more accessible and efficient.

## Hypothesis and how to validate?
  * Hypothesis 1: The dataset is balanced between malignant and non-malignant classes.
- Validation process: Plot the class distribution. If the counts are approximately equal(-10% difference), the hypothesis is validated.

  * Hypothesis 2: There is a visual difference between malignant and non-malignant average images
- Validation process: Compute and display the average image for each class. If they appear visually different(like in colour or shape), the hypothesis is supported.


## The rationale to map the business requirements to the Data Visualizations and ML tasks
* Business requirement 1: Model creation and reliability
  - We will inspect the data given to ensure there is enough(in this case, there was not).

* Business requirement 2: Visual differentiation between malignant and benign
  - We will create a series of images(montages) that will display benign and malignant skin lesions.
  - We will also create image plots showing the average variability in both malignant and benign skin lesions.
  - Lastly, we will create a plot showing the difference between a malignant and benign skin lesion.


## ML Business Case
### Predict Skin Lesions (Classification: Convolutional Neural Network)
- We want to create a ML model to predict if a skin lesion is malignant or benign based on previous data from the ISIC Archive. The model will classify an image as a class(malignant or benign), therefore it will be a classification model. Convolutional Neural Networks (CNNs) work exceptionally well with images because their architecture mimics how the real visual world is structured, so this will be the model we will work with.

* The ideal outcome is to have:
  - Accuracy: 70-85%
  - Specificity: 75-80%
  - Precision: about 65% (When the model says "Cancer", it's right about 2 out of 3 times)
(sadly, this was not possible due to the small dataset used)

## Dashboard Design
* Page Summary: Contains small talk about skin cancer and places the user can read more information such as the ISIC Archives or the SCF. It also contains the business requirements

* Skin Visualizer: Shows checkboxes where each shows data visualization, such as
  - Difference between average and variability
  - Difference between benign and malignant skin lesions
  - Malignant image montage
  - Benign image montage

* Skin Lesion Detector: This page answers the second business requirement by predicting whether a skin lesion is malignant or not.

* Hypothesis: Here, the hypothesis is stated(if benign and malignant skin lesions can be differentiated).

* ML Performance: Here we see:
  - Label frequencies between sets
  - Model performance metrics
  - What the plots actually mean


## Unfixed Bugs
Only thing that truly bugged the developer was the model's inability to effectively learn to label benign and malignant skin lesions. Apart from that, no bugs have been found

## Deployment
### Heroku

* The App live link is: [https://YOUR_APP_NAME.herokuapp.com/ ](https://skin-cancer-detector-fe29380e893f.herokuapp.com/)
* Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries\
joblib == used for saving models\
keras == Used for building/training neural networks\
matplotlib.pyplot(smaller part of matplot) == creates charts, graphs, and plots\
numpy == mathematical operations\
pandas == mathematical operations\
pillow == reading images\
plotly == plotting images\
scikit-learn == building the ML model\
seaborn == data visualization\
streamlit == creating app/dashboard\
tensorflow == transforming data into arrays for ML model learning\


## Credits 

Credits are due to many sources, such as:/ DeepSeek(AI)/ Emmett(AI)/ online tutorials explaining how CNN models work(Indian people really explain these models well)/ the malaria walkthrough project(some codeblocks, such as the more complex backend blocks were used in my project)


## Acknowledgements (optional)
* I would like to thank everyone who has helped me throughout the whole year I have been with Code Institute. I have learnt a lot with this group and really appreciate the kindness and amazing conversations I have had. I would also like to thank my parents for being supportive throughout my whole journey in Full-Stack Development and Machine Learning. Without them, this would not have been possible.

## Notes

I believe I have the best story to tell when working with this project.\
First, I was working normally with this project in a forked repository. Then, suddenly, everything stopped working, saying thinsg such as "[library] could not be resolved" in yellow writing, so I tried looking for ways to resolve this. I could not continue on for some reason as the code blocks would refuse to run correctly. I spent a whole day fixing this, and could not, so in the end I just made a new repository using the template from CI as a template(yes, the green template button on the top right). After that, everything seemed to work again!\
Then, when I tried working on the model, I started obtaining horrendous looking graphs. I have a few notes I will rewrite onto this readme:

1-) I had to reduce my batch size because I kept on receiving an Allocation of "series of numbers" exceeds 10% of my system memory. I felt that this called me poor in so many different ways haha.\
2-) After about three models, I continued lowering the learning rate and added gradient clipping to prevent val_loss spiking from 0.5 to 1.04
3-) After various tries, I saw the model was still learning nothing, so I loosened the constraints it had by having higher learning rate and gentler clipping(clipnorm). I also removed the 4th block this time.
4-) Finally, I made the augmented images be less different. In other words, making the differences slightly less subtle.
5-) I ended up removing another block in the model in hopes of being able to get a higher score for loss and accuracy. I also removed clipping, added stronger regularization.
6-) Finally, after making my model much simpler, I saw improvements and the model had actually learnt better than before. I had increased class weights to force learning malignant, I also had played around with the kernel, but sadly, the model still was not able to learn effectively.

This goes to show how important data is to be able to teach ML models how to differentiate between two classes. In other words, garbage in, garbage out. Diamonds in, Diamonds out.
