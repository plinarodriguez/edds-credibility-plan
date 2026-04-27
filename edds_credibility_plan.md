# EDDS Credibility Plan

 The EDDS Credibility Plan defines the question of interest, context of use, risk, and evidence requirements for establishing confidence in the computational model.

## Question of Interest

The primary question of interest for this study is:

> How accurately can a computational model predict the thermal response of fluid within a simplified EDDS geometry under controlled operating conditions?

Quantities of Interest (QoIs):

- Bulk fluid temperature near the outlet  
- Temperature distribution along the pipe  
- Temperature rise due to applied heating  

These quantities are selected to reflect the thermal behavior relevant to device performance.

## Context of Use

The computational model is used to simulate conjugate heat transfer within a simplified EDDS geometry.

This model is intended for:

- Understanding thermal behavior under controlled conditions  
- Supporting methodological development in verification, validation, and reproducibility  
- Demonstrating credibility assessment workflows  

The model is **not** intended for direct regulatory decision-making in its current form.

## Risk Assessment



#### Model Influence

The model provides insight into thermal behavior but is not the sole basis for decision-making.

- Model influence is considered: `Moderate`



#### Decision Consequence

The consequences of incorrect predictions in this context are limited to research conclusions and methodological development.

- Decision consequence is considered: `Low to Moderate`



#### Overall Risk

Based on model influence and decision consequence:

> **Risk Level: Moderate**

This level of risk motivates a structured verification approach and future validation efforts.

## Credibility Goals - VVUQ 
Credibility goals incorporate gradations of rigor aligned with model risk, specifying increasing levels of evidence needed to support confidence in model predictions.


## Verification
Verification ensures that the computational model is solved correctly by confirming proper implementation of the governing equations.


### Code


#### Software Quality Assurance(SQA)
- Very little or no SQA procedures were specified or followed;
- `SQA procedures were specified and documented;`
- In addition to the specified SQA procedures, the software anomaly list and the software development environment are fully understood and the impact on the COU is analyzed and documented; quality metrics are tracked.



#### Numerical Code Verification 
- `NCV was not performed;`
- The numerical solution was compared to an accurate benchmark solution from another verified code;
- Discretization error was quantified by comparison to an exact solution and a grid convergence study demonstrated that the numerical solution asymptotically approaches the exact solution as the discretization was refined;
- In addition to the quantification of discretization error and the execution of a grid convergence study, the observed order of accuracy was quantified and compared to the theoretical order of accuracy.



### Calculation (Solution)


#### Discretization Error
- No grid or time-step convergence analysis was performed to estimate the discretization error;
- `Applicable grid or time-step convergence analyses were performed and their respective convergence behaviors were observed to be stable, but the discretization error was not estimated;`
- Applicable grid or time-step convergence analyses were performed and discretization error was estimated.



#### Numerical Solver Error 
- `No solver parameter sensitivity was performed;` 
- No solver parameter sensitivity was performed.  Solver parameters were established based on values from a previously verified computational model;
- Problem-specific sensitivity study was performed on solver parameters, confirming that changes in simulation results due to changes in the solver parameters were negligible relative to the model accuracy goal.



#### Use Error
- Inputs and outputs were not verified;
- Key inputs and outputs were verified by the practitioner;
- `Key inputs and outputs were verified by internal peer review;`
- Key inputs and outputs were verified by reproducing simulations as part of an external peer review.



## Validation 
Validation assesses how well the computational model represents physical reality by comparing model predictions to physical experiments or observed data.


### Computational Model 


#### Model Form 
- Influence of model form assumptions was not explored;
- `Influence of expected key model form assumptions was explored;`
- Comprehensive evaluation of model form assumptions was conducted.



#### Model Input


##### Quantification of Sensitivities
- Sensitivity analysis was not performed;
- `Sensitivity analysis on expected key parameters was performed;`
- Comprehensive sensitivity analysis was performed.



##### Quantification of Uncertainties
- Uncertainties were not identified; 
- `Uncertainties on expected key inputs were identified and quantified, but were not propagated to quantitatively assess the effect on the simulation results;`
- Uncertainties on all inputs were identified and quantified, and were propagated to quantitatively assess the effect on the simulation results.



### Comparator


#### Test Samples


##### Quantity 
- A single sample was used;
- `Multiple samples were used, but not enough to be statistically relevant;`
- A statistically relevant number of samples were used.



##### Measurement 
- Test samples were not measured and/or characterized;
- One or more key characteristics of the test samples were measured;
- `All key characteristics of the test samples were measured.`



##### Range of Characteristics 
- `Sample(s) with a single set of characteristics was included;`
- Samples representing a range of characteristics near nominal were included;
- Samples representing the expected extreme values of the parameters were included;



##### Uncertianty of Test Sample Measurements
- Sample(s) were not characterized or characterized with gross observations, and measurement uncertainty was not addressed;
- Uncertainty analysis incorporated instrument accuracy only;
- `Uncertainty analysis incorporated instrument accuracy and repeatability (i.e., statistical treatment of repeated measurements);`
- Uncertainty analysis incorporated a comprehensive uncertainty quantification, which included instrument accuracy, repeatability, and other conditions affecting the measurements.



#### Test Conditions


##### Quantity 
- A single test condition was examined;
- `Multiple (2-4) test conditions were examined;`
- More than four test conditions were examined.



##### Measurement 
- Test conditions were qualitatively measured and/or characterized;
- One or more key characteristics of the test conditions were measured;
- `All key characteristics of the test conditions were measured.`



##### Range of Characteristics
- A single test condition was examined;
- Test conditions representing a range of conditions near nominal were examined;
- Test conditions representing the expected extreme conditions were examined;
- `Test conditions representing the entire range of conditions were examined`



##### Uncertainty of Test Condition Measurements
- Test condition(s) were not characterized or characterized with gross observations, measurement uncertainty was not addressed;
- Uncertainty analysis incorporated instrument accuracy only;
- `Uncertainty analysis incorporated instrument accuracy and repeatability (i.e., statistical treatment of repeated measurements);`
- Uncertainty analysis incorporated a comprehensive uncertainty quantification, which included instrument accuracy, repeatability, and other conditions affecting the measurements.




### Assessment 


#### Equivalency of Input Parameters 
- The types of some inputs were dissimilar;
- The types of all inputs were similar, but the ranges were not equivalent;
- `The types and ranges of all inputs were equivalent.`



#### Output Comparison 


##### Quantity 
- Single output was compared;
- `Multiple outputs were compared.`



##### Equivalency of Output Parameters
- Types of outputs were dissimilar;
- Types of outputs were similar;
- `Types of outputs were equivalent.`



##### Rigor of Output Comparison 
- Visual comparison was performed;
- `Comparison performed by determining the difference between computational results and experimental results;`
- Uncertainty in the output of the computational model or the comparator was used in the output comparison;
- Uncertainty in the output of the computational model and the comparator were used in the output comparison.



##### Agreeement of Output Comparisons 
- The level of agreement of the output comparison was not satisfactory for key comparisons;
- `The level of agreement of the output comparison was satisfactory for key comparisons, but not all comparisons;`
- The level of agreement of the output comparison was satisfactory for all comparisons.