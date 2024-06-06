# Triadic-Optimization
Inspired by the ancient Greek mathematician Aristarchus, implements a modern approach to simplifying and optimizing processes, with a focus on AI training. Drawing from Aristarchus's "Simple Method of Three," we aim to streamline complex methodologies into efficient and effective solutions for AI model development and training


## Understanding the Relationship Between Model Predictions and Data Averages

In machine learning, understanding the relationship between the predictions of a model and the underlying data is crucial for effective model development and interpretation. One interesting relationship to explore is the connection between the average of the data points and the predictions made by the model.

## The Concept

Consider the following mathematical expression:

![triadic-rules](https://github.com/rizitis/Triadic-Optimization/blob/main/triadic-rules.png)


This equation represents the average of an infinite number of data points \( y_i \), denoted by \( \mu \). Here, \( n \) represents the number of data points, and \( y_i \) represents each individual data point.

## Link to Model Predictions

Interestingly, this concept can be linked to the predictions made by a machine learning model. If a model is trained to predict values based on certain features \( x_1, x_2, ..., x_m \), it can be represented as:

![predict](https://github.com/rizitis/Triadic-Optimization/blob/main/model-predict.png)


In this equation, \( y \) represents the predicted value, \( w_0 \) is the bias term, and \( w_1, w_2, ..., w_m \) are the weights corresponding to the features \( x_1, x_2, ..., x_m \).

## Connecting the Dots

Now, let's connect the average concept with the model predictions. If a model is trained effectively, it should ideally produce predictions that are close to the average of the data points. In other words, the average of the predicted values should approach the true average of the data.

By understanding this relationship, we can gain insights into how well a model captures the underlying patterns in the data. If the model's predictions deviate significantly from the average of the data, it may indicate issues with the model's performance or the need for further investigation into the data.

In conclusion, exploring the relationship between the average of the data and the predictions made by a model can provide valuable insights into the effectiveness and reliability of the model in capturing the underlying data distribution.

<br>*READ: explain.txt and praxis.txt*

## WHY?

### Preference for the Representative Sample (1/3 of the data)

#### Advantages:

**Economy of Computational Resources:**
- Less usage of processing power and memory.
- Lower cost in terms of time and energy for training the model.

**Faster Training:**
- Training can be completed in significantly less time, allowing for quicker development and testing of models.

**Easier Data Management:**
- Smaller data volume means easier storage and management.
- Reduced complexity in the data cleaning and preprocessing process.

**Efficiency and Effectiveness:**
- If the deviation in the result is small, nearly the same results are achieved with fewer resources.
- Avoids overfitting that can occur with excessive use of data.

#### Disadvantages:

**Potential Insufficiency in Covering Rare Cases:**
- Although the sample is representative, it may not include all rare cases or anomalies present in the full dataset.

**Need for Sample Reliability:**
- High accuracy and diligence are required in selecting the representative sample to ensure it is truly representative.

### Conclusion

If the representative sample provides results with small deviation from those that would be achieved with a larger amount of data, the use of the representative sample is preferred. The savings in resources, faster training, and easier data management outweigh the minor potential disadvantages.

However, it must always be ensured that the sample is truly representative and that no significant information or rare cases that could affect the model's performance in a production environment are omitted.


### Computational Resources

**Training Time:**
- Reducing the data to 1/3 can decrease the training time by approximately 1/3 to 1/2, depending on the efficiency of the processing infrastructure and the complexity of the model.

**Processing Power:**
- Fewer data require less processing power, allowing the use of fewer processors or less powerful processors for model training.

**Memory (RAM):**
- Using less data reduces the required memory during training, allowing the use of systems with smaller memory.

### Storage Resources

**Storage Space:**
- Storing 1/3 of the data requires about 1/3 of the storage space that would be required for 70-80% of the data. This saves space on hard drives or data warehouses.

### Energy Resources

**Energy Consumption:**
- Reducing processing power and training time leads to a significant reduction in energy consumption, which is particularly important for environmental reasons and operational costs.

### Human Resources

**Development Time:**
- Faster training allows engineers and data scientists to iterate more quickly through training and optimization cycles of the model.

**Data Analysis and Management:**
- Smaller data volume makes the data cleaning, analysis, and preparation process easier, reducing the time spent by the data team.

### Financial Resources

**Infrastructure Cost:**
- Less data and shorter training time reduce infrastructure costs, such as the need for more or more powerful servers and the consumption of cloud resources.

**Operational Cost:**
- Reduced energy consumption and shorter training time result in lower operational costs.

### Overall Efficiency

Using a highly accurate representative sample can improve efficiency in many areas, offering resource savings and faster development without significant loss of model accuracy. Especially if the deviation in model performance is small, the benefits of resource savings can outweigh the potential drawbacks.

