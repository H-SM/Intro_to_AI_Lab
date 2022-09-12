#lab 3 bayesian final
import pgmpy.models
import pgmpy.inference
import pgmpy.factors.discrete
alarm_model=pgmpy.models.BayesianNetwork([("Burglary","Alarm"),("Earthquake","Alarm"),("Alarm","John"),("Alarm","Mary")])

cpd_burglary=pgmpy.factors.discrete.TabularCPD("Burglary",2 , [[0.99],[0.01]])
cpd_earthquake=pgmpy.factors.discrete.TabularCPD("Earthquake", 2, [[0.99],[0.01]])
cpd_alarm=pgmpy.factors.discrete.TabularCPD("Alarm", 2,   [[0.99,0.71,0.06,0.05],[0.01,0.29,0.94,0.95]],evidence=["Burglary","Earthquake"],evidence_card=[2,2])
cpd_john=pgmpy.factors.discrete.TabularCPD("John", 2,[[0.95,0.1],[0.05,0.9]],evidence=["Alarm"],evidence_card=[2])
cpd_mary=pgmpy.factors.discrete.TabularCPD("Mary", 2,[[0.1,0.7],[0.9,0.3]],evidence=["Alarm"],evidence_card=[2])
alarm_model.add_cpds(cpd_alarm,cpd_burglary,cpd_earthquake,cpd_john,cpd_mary)
print("probability distribution , P(Burgalary)")
print(cpd_burglary)
print()
print("probability distribution , P(Earthquake)")
print(cpd_earthquake)
print()
print("probability distribution , P(Alarm | burgalary, Earthquake)")
print(cpd_alarm)
print()
print("probability distribution , P(JohnCalls | Alarm)")
print(cpd_john)
print()
print("probability distribution , P(MaryCalls | Alarm)")
print(cpd_mary)
print()

#plot the model 

#perform variable elements for interference 
#variable elimination (VE)
infer=pgmpy.inference.VariableElimination(alarm_model)
#calculate th prob of a burgalary if john and Mary calls (0:True,1:False)
posterior_probablity=infer.query(['Burglary'],evidence={'John':0,'Mary':0})
#print posterior probablity
print('Posterior probability of Burglary if John and Mary Calls')
print(posterior_probablity)
print()

posterior_probablity=infer.query(['Alarm'],evidence={'Burglary':0,'Earthquake':0})
#Calculate the prob of alarm starting if there is a burgalary and earthquake
print('posterior probability for bugalary and earthquake if alarm goes out')
print(posterior_probablity)
print()
