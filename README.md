# California Housing Value Prediction

![Image](https://i0.wp.com/studentwork.prattsi.org/infovis/wp-content/uploads/sites/3/2021/05/housing.jpg?resize=840%2C382&ssl=1)

Para este proyecto, se utilizó el dataset [California Housing Prices](https://github.com/ageron/handson-ml/tree/master/datasets/housing), el cual contiene información de un **censo realizado en California en el año 1990**. Las columnas de la tabla son las siguientes:

* longitude
* latitude
* housing_median_age
* total_rooms
* total_bedrooms
* population
* households
* median_income
* median_house_value
* ocean_proximity

El proyecto consiste en **entrenar el dataset** para poder predecir el valor de una casa con base en diferentes features.

Los modelos utilizados fueron:
* Linear Regression
* Decision Tree
* Random Forest
* SVM

El modelo con el **mejor estimator** fue utilizado para crear una aplicación en Streamlit donde el usuario ingresa los valores para poder obtener el valor de la casa predecido por el modelo escogido. 

Para poder correr la aplicación, se debe clonar el repositorio y correr el siguiente comando:

```
streamlit run app.py
```

También se puede acceder a este [link](https://mus1cian-california-housing-prediction-app-kgoff3.streamlit.app/) para ir directamente a la aplicación web de Streamlit.