# FORPRODE GenAI Bootcamp — Notebook Guide

A plain-language guide to every notebook in **Week 4** and **Week 5** of the bootcamp.

---

## How to read this guide

Each notebook entry explains:
- **What it does** — the big picture in simple words
- **The problem it solves** — why we built it
- **Key concepts** — explained simply
- **Expected output** — what you see when you run it

---

## Week 4

### Day 1

#### ExerciseXP — `week4/Day1/ExerciceXP/ExercisesXP_Student.ipynb`

**What it does**
Five written exercises where you design a machine learning project on paper — no code yet.

**The problem it solves**
Before writing any code, a data analyst needs to think: *What am I trying to predict? What data do I need? Which model should I pick?* This notebook trains that planning skill.

**Key concepts (simply explained)**
- **Problem statement** — A clear one-sentence description of what the model should predict and why it matters.
- **Feature selection** — Choosing the right columns from your data. If you want to predict loan defaults, "credit score" matters. "Zip code" probably doesn't.
- **Supervised vs unsupervised vs reinforcement learning** — Supervised = you have right answers to learn from. Unsupervised = you find hidden groups. Reinforcement = the model learns by trying things and getting rewards.
- **Evaluation metrics** — Accuracy, Precision, Recall, F1, ROC-AUC. Each tells you something different about how well the model works.

**Expected output**
Text answers in markdown cells. No graphs. This is a planning/thinking exercise.

---

### Day 2

#### ExerciseXP — `week4/Day 2/ExerciceXP/ExercisesXP_Diabetes_Student.ipynb`

**What it does**
Builds a real Logistic Regression model that predicts whether a patient has diabetes from 8 health measurements.

**The problem it solves**
Doctors need tools to flag patients who might have diabetes early so they can get treatment. We train a model on 100,000 patient records to do this automatically.

**Key concepts (simply explained)**
- **Logistic Regression** — Despite the name, it's a classification model. It outputs a probability between 0 and 1 ("this patient is 82% likely to have diabetes").
- **Pipeline** — A chain of steps that first cleans the data, then trains the model. Using a pipeline prevents a common mistake called *data leakage* (accidentally learning from test data).
- **OneHotEncoder** — Turns a text column like `gender = "Male"` into a number column `gender_Male = 1`. The model can only work with numbers.
- **StandardScaler** — Puts all number columns on the same scale (average 0, range ±1) so no single column dominates the model just because it has bigger numbers.
- **Confusion matrix** — A 2×2 table showing how many patients were correctly and incorrectly classified. The dangerous mistake here is a *False Negative* (telling a diabetic patient they're healthy).
- **ROC-AUC** — A single number (0 to 1) that measures how good the model is. Our model achieves ~0.96, which is excellent.

**Expected output**
- Printed dataset stats and class counts (91,500 healthy vs 8,500 diabetic)
- A bar chart comparing Accuracy, Precision, Recall, F1
- A confusion matrix heatmap
- A 2D decision boundary plot (using only 2 features)
- A ROC curve with AUC score

---

### Day 4

#### DailyChallenge — `week4/Day4/DailyChallenge/DailyChallenge (1).ipynb`
#### (same notebook) ExerciseXP — `week4/Day4/ExerciseXP/DailyChallenge.ipynb`

> Note: These two files contain identical code.

**What it does**
Predicts which bank customers are about to close their account (*churn*), then recommends which customers the bank should call first.

**The problem it solves**
Keeping an existing customer costs far less than finding a new one. If a bank can spot unhappy customers before they leave, it can offer them deals to stay.

**Key concepts (simply explained)**
- **Churn** — When a customer stops using a service (closes their bank account, cancels a subscription, etc.).
- **Three models compared** — Logistic Regression (simple, fast), Random Forest (many decision trees voting together), Gradient Boosting (trees learning from each other's mistakes). We pick the best one.
- **GridSearchCV** — Automatically tries many combinations of model settings to find the best ones. Think of it as a robot that tests 144 different configurations of the same model.
- **Feature importance** — After training, the Random Forest tells us which columns (Age, Balance, Geography…) were most useful for the prediction.
- **ROC curve** — A graph that shows how many real churners we catch vs. how many non-churners we falsely flag, at different sensitivity levels.

**Expected output**
- Printed metrics for all 3 models
- ROC curve comparing all 4 models (3 base + 1 tuned)
- Confusion matrix for the best model
- Feature importance bar chart
- Histogram of predicted churn probabilities
- Business summary: how many customers were correctly identified and estimated savings

---

#### ExerciseXP — `week4/Day4/ExerciseXP/ExerciceXP.ipynb`

**What it does**
Analyzes airline traffic data to find patterns and predict the total number of passengers.

**The problem it solves**
Airlines need to forecast passenger demand to plan their fleet, staffing, and schedules. This notebook builds both a simple and a multiple linear regression model and compares them.

**Key concepts (simply explained)**
- **Hypothesis test (t-test)** — A statistical question: "Are domestic passengers and international passengers really different in number, or could the difference be random chance?" The t-test gives a yes/no answer with a confidence level.
- **Pearson correlation** — Measures how strongly two columns move together. 1 = perfect positive link, 0 = no link, -1 = opposite link. Here, total flights and total passengers are very strongly correlated.
- **Simple linear regression** — Predicts one thing (passengers) from one other thing (flights). Works like `y = a × x + b`.
- **Multiple linear regression** — Uses several columns at once to make a better prediction.
- **R² score** — Tells you "what percentage of the variation in the real data can my model explain?" R² = 0.95 means the model explains 95% of the ups and downs in passenger numbers.
- **Residuals** — The difference between what the model predicted and what actually happened. A good model has residuals scattered randomly around zero.

**Expected output**
- Correlation heatmap
- Hypothesis test p-values (printed)
- Two regression plots (predicted vs actual, residuals)
- Comparison table: simple vs multiple regression (R², RMSE, MAE)

---

### Day 5

#### DailyChallenge — `week4/Day5/DailyChallenge/DailyChallenge.ipynb`

**What it does**
Predicts each Pokémon's battle win rate using their stats (HP, Attack, Speed, etc.) and compares three different ML models. Then uses PCA to visualize all Pokémon in 2 dimensions.

**The problem it solves**
Given a Pokémon's statistics, can we predict how often it wins battles? This is a *regression* problem (predicting a continuous number between 0 and 1).

**Key concepts (simply explained)**
- **Win rate calculation** — For each Pokémon, we count how many battles it won and divide by how many it fought.
- **One-hot encoding** — Pokémon types (Fire, Water, Grass…) are text. We convert each type to a column of 0s and 1s so the model can work with them.
- **Three regression models**: Linear Regression (draws straight lines), Random Forest (many trees averaging their guesses), XGBoost (trees that each fix the previous tree's mistakes).
- **MAE (Mean Absolute Error)** — On average, how far off is the model's predicted win rate from the real one?
- **PCA (Principal Component Analysis)** — Imagine squashing 50 dimensions down to 2 so you can draw a scatter plot. PCA finds the two directions that keep the most variation from the original data. Points that cluster together are Pokémon with similar stats.
- **Variance explained** — The first two PCA components together explain ~X% of the total variation. The higher this number, the less information is lost in the squash.

**Expected output**
- Correlation heatmap
- Scatter matrix (PairGrid) colored by win rate category
- Bar chart comparing MAE for all 3 models
- PCA scree plot (variance per component) and cumulative variance curve
- 2D scatter plot of Pokémon colored by win rate

---

#### MiniProject — `week4/Day5/MiniProject/Mini_Projet.ipynb`

**What it does**
Predicts whether a patient has heart disease using Logistic Regression on the UCI Heart Disease dataset.

**The problem it solves**
Heart disease is one of the leading causes of death worldwide. A model that flags high-risk patients from routine clinic data could help doctors prioritize further testing.

**Key concepts (simply explained)**
- **Binary target from multi-class** — The original `num` column has values 0–4 (no disease to severe). We simplify it to 0 (healthy) vs 1 (has disease).
- **Missing value imputation** — Some columns have gaps. We fill numeric gaps with the *median* (middle value) and categorical gaps with the *mode* (most common value).
- **LabelEncoder** — Converts text categories (like "male"/"female") to numbers (0/1).
- **class_weight='balanced'** — When healthy patients outnumber sick ones, the model naturally learns to always predict "healthy." Setting `class_weight='balanced'` forces it to pay more attention to the minority class.
- **Coefficient analysis** — After training, each feature gets a weight. Positive weight = increases heart disease risk. Negative weight = protective factor.
- **Normalized confusion matrix** — Shows percentages instead of raw counts, making it easier to see if one class is being confused more than the other.

**Expected output**
- Distribution plots for numeric and categorical features
- Correlation heatmap
- Training metrics (accuracy, precision, recall, F1)
- Confusion matrix (raw + normalized)
- Feature coefficient bar chart (green = increases risk, red = decreases risk)
- ROC curve with AUC score

---

## Week 5

### Day 1

#### DailyChallenge — `week5/Day1/DailyChallenge/DailyChallenge.ipynb`

**What it does**
Trains a neural network from scratch to recognize handwritten digits (0–9) from the famous MNIST dataset, then analyzes which digits the model struggles with.

**The problem it solves**
Reading handwritten numbers automatically is used in postal services, bank check processing, and phone apps. MNIST is the classic "hello world" of deep learning.

**Key concepts (simply explained)**
- **MNIST** — A dataset of 70,000 grayscale images, each 28×28 pixels, each showing one handwritten digit. 60,000 for training, 10,000 for testing.
- **Normalization** — Pixel values go from 0–255. Dividing by 255 puts them in the 0–1 range, which makes training faster and more stable.
- **One-hot encoding for labels** — Instead of the label `7`, the model sees `[0,0,0,0,0,0,0,1,0,0]` — a vector with a 1 in position 7. This tells the model "this image is definitely a 7, not any other digit."
- **Dense (Flatten → 256 → 128 → 10)** — We flatten the 28×28 image into 784 numbers, pass them through two hidden layers (256 and 128 neurons), and end with 10 outputs (one per digit).
- **Softmax** — The final activation turns the 10 raw outputs into probabilities that add up to 1. The digit with the highest probability is the prediction.
- **Epoch** — One full pass through all 60,000 training images. We train for 10 epochs.

**Expected output**
- Grid of 10 example MNIST images with their labels
- Training and validation loss/accuracy curves over 10 epochs
- Final test accuracy (typically ~98%)
- Confusion matrix (10×10 heatmap)
- Per-digit accuracy scores (which digits are hardest?)
- Grid of 10 misclassified images showing true vs. predicted label

---

#### ExerciseXP — `week5/Day1/ExerciseXP/ExerciceXP.ipynb`

**What it does**
Six exercises covering deep learning theory (written answers) and hands-on coding with MNIST.

**The problem it solves**
Building a strong conceptual foundation before diving into complex architectures. You need to understand *why* neural networks work before you can design good ones.

**Key concepts (simply explained)**
- **Perceptron** — The simplest possible neural network: one neuron that takes inputs, multiplies each by a weight, adds a bias, and outputs 0 or 1. Like a light switch that turns on when conditions are strong enough.
- **Activation functions** — Without them, stacking layers is pointless (a stack of linear functions is still just one linear function). ReLU, Sigmoid, and Tanh add non-linearity so the network can learn curved patterns.
- **Backpropagation + gradient descent** — How a network learns. After each prediction, we compute the error and work backwards through the network, nudging each weight slightly in the direction that reduces the error.
- **Forward propagation** — Computing the output from input: multiply inputs by weights, add bias, apply activation. Like running water downhill through the network.
- **Learning rate** — Controls how big each nudge is. Too large → the model overshoots and never settles. Too small → takes forever to learn.

**Expected output**
- Written answers in markdown cells (Exercises 1, 2, 4, 5 written)
- MNIST model trained and evaluated (Exercises 3 and 6)
- Final test accuracy printed

---

### Day 2

#### DailyChallenge — `week5/Day2/DailyChallenge/DailyChallenge.ipynb`

**What it does**
Uses a neural network to classify points arranged in two concentric circles — something a simple straight line cannot separate.

**The problem it solves**
Demonstrates why we need *hidden layers* and *non-linear activations*. A single-neuron model completely fails. Adding layers + ReLU solves it.

**Key concepts (simply explained)**
- **make_circles dataset** — Two circles, one inside the other, each with a different label. You cannot separate them with a straight line — you need a curved boundary.
- **Linear model failure** — A single `Dense(1, sigmoid)` layer draws a straight line and gets ~50% accuracy (no better than flipping a coin).
- **Non-linear model success** — Adding two hidden layers with ReLU allows the network to draw a curved circle as its decision boundary.
- **Decision boundary** — The line (or curve) in the data space where the model switches from predicting class 0 to class 1. We plot this as a colored background behind the data points.
- **Adam optimizer** — A smarter version of gradient descent that adapts the learning rate for each parameter automatically. Converges faster than basic SGD.
- **80/20 train-test split** — We hold back 20% of the data to check if the trained model generalizes (works on data it has never seen).

**Expected output**
- Scatter plot of the circular dataset
- Basic model accuracy (~50%)
- Improved model accuracy (~99%)
- Decision boundary visualization (train and test sets side by side)

---

#### ExerciseXP — `week5/Day2/ExerciseXP/ExerciceXP.ipynb`

**What it does**
Demonstrates overfitting and underfitting by fitting polynomials of increasing complexity to noisy data.

**The problem it solves**
One of the most important lessons in machine learning: a model can be *too simple* (misses the pattern) or *too complex* (memorizes noise instead of learning the pattern). Finding the sweet spot is the job.

**Key concepts (simply explained)**
- **Noisy data** — Real data always has measurement errors. Here, `y = -x² + noise`. The true shape is a parabola, but the points don't sit perfectly on it.
- **Underfitting (degree 1)** — A straight line trying to fit a curved parabola. Train error and test error are both high.
- **Good fit (degree 7)** — The curve passes near most points without chasing noise. Train error is low, test error is also low.
- **Overfitting (degree 11)** — A wiggly polynomial that passes through every training point perfectly but goes wild between them. Train error is near zero, test error explodes.
- **RMSE (Root Mean Squared Error)** — Square root of the average squared error. Measures "how far off, on average, are my predictions?"
- **RMSE vs degree plot** — The key diagnostic: train RMSE always decreases as degree increases. Test RMSE first decreases then increases. The bottom of the test curve is the optimal degree.

**Expected output**
- Scatter plot of the noisy data
- Three fitted curves: degree 1, 7, and 11
- Table of train/test MSE for all three
- RMSE vs degree plot (log scale) for degrees 1–11
- Printed optimal degree (should be near 2, the true model)

---

### Day 3

#### DailyChallenge — `week5/Day3/DailyChallenge/DailyChallenge.ipynb`

**What it does**
Compares a fully-connected Dense network against a CNN (Convolutional Neural Network) on MNIST digit recognition.

**The problem it solves**
Dense networks treat each pixel independently and ignore spatial structure. A CNN knows that nearby pixels are related (they form edges, curves, shapes) and exploits this to learn more efficiently.

**Key concepts (simply explained)**
- **Dense network (Flatten → 128 → 64 → 10)** — Flattens the 28×28 image to 784 numbers and processes them without any sense of where each pixel is.
- **CNN (Conv2D → MaxPool → Conv2D → MaxPool → Conv2D → Dense → Dropout → Softmax)** — Applies small filters that slide across the image looking for features like edges, then pools the results to reduce size.
- **Conv2D** — A small matrix (e.g., 3×3) that slides over the image and detects patterns. Different filters detect different things (vertical edges, horizontal edges, curves).
- **MaxPooling** — Shrinks the image by keeping only the maximum value in each 2×2 block. Reduces computation and makes the model more robust to small shifts.
- **Dropout** — Randomly switches off 50% of neurons during training. Forces the network to learn redundant representations and reduces overfitting.
- **Parameter count** — Dense model has ~100K parameters. CNN achieves higher accuracy with ~93K parameters by reusing filter weights across the image.

**Expected output**
- Model summaries for both architectures
- Side-by-side training curves (accuracy and loss) for Dense vs CNN
- Comparison table: Dense accuracy vs CNN accuracy
- Grid of 10 test images with Dense and CNN predictions
- Probability bar charts (CNN confidence) for each test image
- Grid of misclassified examples from the CNN

---

#### ExerciseXP — `week5/Day3/ExerciseXP/ExerciceXP.ipynb`

**What it does**
Trains a CNN to classify 14 species of flowers from photos, with full data augmentation, hyperparameter tuning, and model saving.

**The problem it solves**
Image classification in the real world: similar-looking species (Calendula vs California Poppy are both orange/yellow), variable lighting, different backgrounds. This project covers the complete professional workflow.

**Key concepts (simply explained)**
- **ImageDataGenerator** — Automatically creates new training images by rotating, flipping, zooming, and shifting existing ones. This makes the model more robust when it sees new photos at a different angle.
- **4-block CNN architecture** — Each block has two Conv2D layers + BatchNorm + MaxPool + Dropout. Filter count doubles with each block (32→64→128→256) to detect progressively more complex features.
- **BatchNormalization** — After each convolution, this layer rescales the outputs to have consistent mean and variance. Makes training faster and more stable.
- **GlobalAveragePooling2D** — Instead of flattening the final feature maps to a long vector, it averages each feature map to a single number. More compact and less prone to overfitting.
- **EarlyStopping** — Automatically stops training when validation loss stops improving (patience=7 epochs). Prevents wasted computation and overfitting.
- **ReduceLROnPlateau** — Halves the learning rate when training stalls. Like slowing down your steps when you're close to the bottom of a valley.
- **confusion matrix (14×14)** — Shows which flowers are confused with which. Expect Calendula/Poppy confusion (both orange) and Daisy/Black-eyed Susan confusion (similar shape).

**Expected output**
- Image count bar chart per species
- 3×3 grids of example images for each of 14 species
- Training accuracy and loss curves
- 14×14 confusion matrix heatmap
- Per-class accuracy bar chart (green ≥70%, orange 50–70%, red <50%)
- Grid of 16 predictions (green border = correct, red border = wrong)
- Saved model files (`flower_cnn_model.h5`, `flower_cnn_savedmodel/`)

---

### Day 4

#### DailyChallenge — `week5/Day4/DailyChallenge/DailyChallenge.ipynb`

**What it does**
Predicts Apple (AAPL) stock prices for the next day using an LSTM (Long Short-Term Memory) neural network built in **PyTorch**.

**The problem it solves**
Stock prices are time series: each day's price depends on the days before it. LSTMs are designed specifically to learn patterns in ordered sequences, making them popular (though not perfect) for financial forecasting.

**Key concepts (simply explained)**
- **LSTM (Long Short-Term Memory)** — A special type of neural network layer that has a "memory" — it remembers information from many steps back in a sequence. Regular dense layers forget the past.
- **Sliding window (sequence length = 60)** — To predict today's price, we feed the model the past 60 days of data. We slide this 60-day window through the entire dataset to create thousands of training examples.
- **MinMaxScaler** — Scales all feature values to the range [0, 1]. Essential for LSTMs because large number ranges can destabilize training.
- **Train / Validation / Test split (70/15/15)** — We split chronologically (not randomly) because randomly shuffling time series would let the model "see the future" during training.
- **PyTorch DataLoader** — Efficiently loads batches of data during training. Batch size = 64 means the model sees 64 sequences at a time before updating its weights.
- **R² score** — For regression, this tells us "what fraction of the price movement does my model explain?" R² = 0.9 means the model tracks 90% of the price variation.
- **MSE loss** — The training objective: minimize the average squared difference between predicted and actual prices.

**Expected output**
- Printed data loading stats (number of samples, date range)
- Training loss per epoch (printed every 10 epochs)
- Test R² score
- Plot: actual vs. predicted prices on the test period
- Training/validation loss curves
- Saved model file (`lstm_model.pth`)

---

#### ExerciseXP — `week5/Day4/ExerciseXP/ExerciseXP.ipynb`

**What it does**
Predicts future household electricity consumption using an LSTM built in **TensorFlow/Keras**, trained on 2 million real measurements from a French home.

**The problem it solves**
Energy companies and smart home systems need to forecast power consumption to balance supply and demand on the grid. This is a multivariate time series forecasting problem.

**Key concepts (simply explained)**
- **UCI Household Power Consumption dataset** — 2,075,259 minutes of real electricity data from a single house in Sceaux, France (2006–2010). 7 measurements per minute: global power, voltage, current, and 3 sub-metering channels.
- **Missing values (`?`)** — The dataset uses `?` for missing readings. We replace these with the column mean.
- **Resampling (`resample('1D')`)** — Aggregates per-minute data to daily totals/averages. Reduces noise and makes patterns easier to see.
- **Windowing** — We cut the time series into overlapping 48-step windows (48 minutes = 48 past measurements). Each window becomes one training example; the next step is the label.
- **LSTM with Keras (Input → LSTM(64) → Dense(1))** — A lightweight LSTM that reads a 48-step sequence of 7 measurements and predicts the next value of Global_active_power.
- **EarlyStopping + ReduceLROnPlateau** — Same as Day 3 flower project: stop early when improvements stop, reduce learning rate when stuck.
- **MAE and MSE** — The two error metrics reported on the test set.

**Expected output**
- Dataset shape (2,075,259 rows × 7 columns)
- Missing values before and after imputation
- Daily sum and daily mean plots for Global_active_power
- Daily mean and std plots for Global_intensity
- Window shapes: train `(1,660,159, 48, 7)`, test `(415,004, 48, 7)`
- LSTM model summary
- Training + validation loss curve
- Final test MAE and MSE

---

## Quick Reference — Concepts by Frequency

| Concept | Where it appears |
|---|---|
| Train/Test split | Every notebook |
| StandardScaler / MinMaxScaler | Bank churn, Air traffic, Diabetes, Heart disease, Stock LSTM, Power LSTM |
| ROC curve + AUC | Bank churn, Diabetes, Heart disease |
| Confusion matrix | Diabetes, Bank churn, Heart disease, MNIST (all), Flowers |
| Feature importance | Bank churn (Random Forest), Heart disease (coefficients) |
| Logistic Regression | Diabetes, Heart disease, make_circles (basic model) |
| Random Forest | Bank churn, Loan prediction |
| Neural network (Dense) | MNIST, make_circles |
| CNN | MNIST comparison, Flower classification |
| LSTM | Stock price, Household power |
| PCA | Pokémon win rate |
| Polynomial regression | Overfitting/underfitting exercise |
| Data augmentation | Flower classification |
| GridSearchCV | Bank churn |
| Hypothesis testing | Air traffic |

---

## Running the notebooks

1. Open a terminal in the bootcamp folder
2. Run `jupyter notebook` or open in VS Code
3. Each notebook has its own data — check if a CSV or zip file is in the same folder
4. Run cells top to bottom — some cells depend on variables defined in earlier cells

For notebooks that use `yfinance` or `tensorflow`, make sure these packages are installed:
```
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow torch yfinance xgboost
```
